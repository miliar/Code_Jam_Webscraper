/*
 * main.cpp
 *
 *  Created on: May 21, 2011
 *      Author: stefan
 */

#include <iostream>
#include <fstream>
#include <limits.h>
#include <map>
#include <vector>

using namespace std;

#define INFINITY INT_MAX

struct team{
	vector<team*> teams_won;
	vector<team*> teams_lost;
	vector<team*> teams_not_played;

	double wp;
	double owp;
	double oowp;

	double rpi(){
		return 0.25*wp + 0.5*owp + 0.25*oowp;
	}

	team() : wp(0.0), owp(0.0), oowp(0.0) { }
};

int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in>>T;

	for(int caseNo = 1; caseNo <= T; caseNo++){
		int N;
		in>>N;

		map<int, team*> teams;
		for(int i = 0; i < N; i++){
			team* t = new team();
			teams.insert(make_pair(i, t));
		}

		// read teams & compute wp
		for(int i = 0; i < N; i++){
			team* current_team = teams.at(i);

			for(int j = 0; j < N; j++){
				team* game_team = teams.at(j);

				char c;
				in>>c;

				switch(c){
				case '.':
					current_team->teams_not_played.push_back(game_team);
					break;
				case '1':
					current_team->teams_won.push_back(game_team);
					break;
				case '0':
					current_team->teams_lost.push_back(game_team);
					break;
				default:
					cerr<<"invalid character!"<<endl;
				}
			}

			if(current_team->teams_won.size() + current_team->teams_lost.size() > 0){
				current_team->wp = (double)current_team->teams_won.size() /
						((double)current_team->teams_won.size() +
						(double)current_team->teams_lost.size());
			}
		}


		// compute owp
		for(int i = 0; i < N; i++){
			team* current_team = teams.at(i);

			double owp = 0.0;
			vector<team*>::iterator it;
			for(it = current_team->teams_lost.begin(); it != current_team->teams_lost.end(); it++){
				if((*it)->teams_won.size() + (*it)->teams_lost.size() > 0)
					owp += ((double)(*it)->teams_won.size() - 1) / ((double)(*it)->teams_won.size() - 1 + (*it)->teams_lost.size());
			}

			for(it = current_team->teams_won.begin(); it != current_team->teams_won.end(); it++){
				if((*it)->teams_won.size() + (*it)->teams_lost.size() - 1 > 0)
					owp += ((double)(*it)->teams_won.size()) / ((double)(*it)->teams_won.size() + (*it)->teams_lost.size() - 1);
			}

			if(current_team->teams_lost.size() + current_team->teams_won.size() > 0)
				current_team->owp = owp / (current_team->teams_lost.size() + current_team->teams_won.size());

		}

		// compute oowp
		for(int i = 0; i < N; i++){
			team* current_team = teams.at(i);

			double oowp = 0.0;
			vector<team*>::iterator it;
			for(it = current_team->teams_lost.begin(); it != current_team->teams_lost.end(); it++){
				oowp += ((*it)->owp);
			}

			for(it = current_team->teams_won.begin(); it != current_team->teams_won.end(); it++){
				oowp += ((*it)->owp);
			}

			if(current_team->teams_lost.size() + current_team->teams_won.size() > 0)
				current_team->oowp = oowp / (current_team->teams_lost.size() + current_team->teams_won.size());

		}

		out.precision(12);
		//cout.precision(12);

		//cout<<"Case #"<<caseNo<<": "<<endl;
		out<<"Case #"<<caseNo<<": "<<endl;
		for(int i = 0; i < N; i++){
			team* current_team = teams.at(i);
			//cout<<current_team->rpi()<<endl;
			out<<current_team->rpi()<<endl;
		}
	}

	out.close();
	in.close();

	return 0;
}
