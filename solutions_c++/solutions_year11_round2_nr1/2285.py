#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <math.h>

using namespace std;

vector<double> GetWinPer(vector<string> results, vector<int> games)
{
	vector<double> WPs;
	for (int k =0 ; k < results.size(); k++)
	{
	
		double count =0;
		for (int i =0 ; i< results[k].size(); i++)
		{
			if (results[k][i]=='1')
			{
				count++;
			}
		}
		WPs.push_back(count/(double)games[k]);
	}
	return WPs;
}
double GetWP(int ex, string results)
{
	//string
	int numofGames =0;
	int numOfWon = 0;
	for (int i =0 ; i< results.size();i++)
	{
		if (i != ex)
		{
			if (results[i]!='.')
			{
				numofGames++;
			}
			if (results[i]=='1')
			{
				numOfWon++;
			}
		}
	}

	return (double)numOfWon/(double)numofGames;
}

vector<double> GetOWP(vector<string> results)
{
	vector<double> OWPs;
	
	for (int i =0 ; i< results.size(); i++)
	{
		double WP =0;
		int num = 0;
		for (int j =0 ; j < results.size(); j++)
		{
			if (i != j && results[i][j]!='.')
			{
				 WP += GetWP(i,results[j]);
				 num++;
			}
		}
		OWPs.push_back(WP/(double)num);
	}
	return OWPs;
}
vector<double> GetOOWPs(vector<string> results, vector<double> OWPs)
{
	vector<double> OOWPs;

	for (int i =0 ; i< results.size(); i++)
	{
		double OWP =0;
		int num = 0;

		for (int j =0 ; j < results[i].size() ; j++)
		{
			if (i != j)
			{
				if (results[i][j]!='.')
				{
					num++;
					OWP+=OWPs[j];
				}
			}
		}
		OOWPs.push_back(OWP/(double)num);
	}
	return OOWPs;
}
vector<int> GetnumOFgames(vector<string> results)
{
	vector<int> games;
	for (int k =0 ; k < results.size(); k++)
	{
		int count =0;
		for (int i =0 ; i< results[k].size(); i++)
		{
			if (results[k][i]!='.')
			{
				count++;
			}
		}
		games.push_back(count);
	}
	return games;
}
void CalculateRPI(vector<string> results, int caseNUm,ofstream& out)
{
	vector<int> NumOFGames = GetnumOFgames(results);
	vector<double> WPs = GetWinPer(results,NumOFGames);
	vector<double> OWPs = GetOWP(results);
	vector<double> OOWPs = GetOOWPs(results,OWPs);
	out<<"Case #"<<caseNUm<<":"<<endl; 
	for (int i =0 ; i < results.size(); i++)// for each team
	{
		double WP = WPs[i];
		double OWP = OWPs[i];
		double OOWP = OOWPs[i];

		double RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;

		out<<RPI<<endl;
	}
}
int main()
{
	ifstream fin("A-large.in");
	ofstream out("outfile.out");

	int numOfTest;
	fin>>numOfTest;
	int numOfTeams;

	for (int i =0 ; i< numOfTest ;i++)
	{
		fin>>numOfTeams;
		
		vector<string> results;
		string temp;
		for (int j =0 ; j< numOfTeams; j++)
		{

			fin>>temp;
			results.push_back(temp);
		}
		CalculateRPI(results,i+1,out);
	}
	return 0;
}