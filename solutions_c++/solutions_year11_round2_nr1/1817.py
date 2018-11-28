#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;
int numTeams;

class TeamStats
{
public:
	vector<short> wins;
	long numWins;
	long gamesPlayed;
	double winPercent;
	double OWP;
	double OOWP;
	
	TeamStats():numWins(0), gamesPlayed(0){}
	
	void readWins(ifstream* in)
	{
		char next;
		for (int i = 0; i < numTeams; i ++) 
		{
			*in >> skipws >> next;
			if(next == '1')
			{
				wins.push_back(1);
				numWins ++;
				gamesPlayed ++;
			}
			else if(next == '0')
			{
				wins.push_back(-1);
				gamesPlayed ++;
			}
			else
			{
				wins.push_back(0);
			}
		}
		winPercent = (double)numWins / (double)gamesPlayed;
	}
	double WPless(int team)
	{
		if(wins[team] == 1)
		{
			if(numWins > 0)	return (double)(numWins - 1) / (double)(gamesPlayed - 1);
			else return 0.0;
		}
		else {
			return (double)(numWins) / (double)(gamesPlayed - 1);
		}
	}
	double calc()
	{
		return (0.25 * winPercent) + (0.5 * OWP) + (0.25 * OOWP);
	}
	string print()
	{
		stringstream out;
		out << calc();
		return out.str();
	}
};

class Question
{
private:
	vector<TeamStats> teams;
	
public:
	Question(){}
	
	void read(ifstream* in)
	{
		teams = vector<TeamStats>(numTeams);
		for (int i = 0; i < numTeams; i ++) {
			teams[i].readWins(in);
		}
	}
	void calcAllOWP()
	{
		for (int i = 0; i < numTeams; i ++) {
			teams[i].OWP = calcOWP(i);
		}
	}
	void calcAllOOWP()
	{
		for (int i = 0; i < numTeams; i ++) {
			teams[i].OOWP = calcOOWP(i);
		}
	}
	double calcOWP(int team)
	{	
		double OWP = 0.0;
		for (int i = 0; i < numTeams; i ++) {
			if(teams[team].wins[i])
			{
				OWP += teams[i].WPless(team);
			}
		}
		return OWP / (double)(teams[team].gamesPlayed);
	}
	double calcOOWP(int team)
	{	
		double OOWP = 0.0;
		for (int i = 0; i < numTeams; i ++) {
			if(teams[team].wins[i])
			{
				OOWP += teams[i].OWP;
			}
		}
		return OOWP / (double)(teams[team].gamesPlayed);
	}
	void calc()
	{
		calcAllOWP();
		calcAllOOWP();
	}
	void print(ofstream* out)
	{
		for (int i = 0 ; i < numTeams; i ++) {
			*out << teams[i].print() << endl;
		}
	}
};

int main (int argc, char * const argv[]) {
    // insert code here...
	Question* answer;
	string file = "../../data/A-large";
	
	ifstream inputFile(string(file + ".in.txt").c_str());
	ofstream outputFile(string(file + ".out").c_str());
	
	int NumCases, Case;
	inputFile >> NumCases;
	
	for (Case = 1; Case <= NumCases; Case ++) 
	{
		inputFile >> numTeams;
		answer = new Question();
		answer->read(&inputFile);
		answer->calc();
		
		outputFile << "Case #" << Case << ":" << endl;
		answer->print(&outputFile);
		delete answer;
	}
	
    return 0;
}
