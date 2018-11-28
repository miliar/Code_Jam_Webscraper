// CodeJam2011R1A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
#include <sstream>

using std::vector;
using std::string;
//using std::map;
using std::pair;
using std::make_pair;
//using std::priority_queue;
using std::cin;
using std::cout;
using std::endl;
using std::istringstream;

int abs(int);
int _tmain(int argc, _TCHAR* argv[])
{
	
	std::ifstream ifstr;
	std::ofstream ofstr;
	ifstr.open("C://Users//Simon//College//CodeJam11//11//A-large.in");
	ofstr.open("C://Users//Simon//College//CodeJam11//11//outtest.txt");
	int n, m, posor, posblu, time, val;
	string col;
	
	ifstr>>n;
	for(int i = 0; i < n; ++i){
		vector<pair<int,int>>blues;
		vector<pair<int,int>>oranges;
		
		ifstr>>m;
		for(int j = 0; j < m; ++j){
			ifstr>>col;
			ifstr>>val;
			if(col=="O"){
				oranges.push_back(make_pair(j,val));
			}
			else{
				blues.push_back(make_pair(j,val));
			}
		}
		vector<pair<int,int>>::const_iterator bluit = blues.begin();
		vector<pair<int,int>>::const_iterator orit = oranges.begin();
		/*cout<<endl;
		for(vector<pair<int,int>>::const_iterator b = blues.begin(); b!=blues.end(); ++b){
			cout<<"B: "<<b->first<<":"<<b->second<<endl;
		}
		for(vector<pair<int,int>>::const_iterator o = oranges.begin(); o!=oranges.end(); ++o){
			cout<<"O: "<<o->first<<":"<<o->second<<endl;
		}
		cout<<endl;*/
		posor = posblu = 1;
		time = 0;

		while(bluit!=blues.end() && orit!=oranges.end()){
			if(bluit->first < orit->first){
				while(posblu != bluit->second){
					posblu += posblu < bluit->second ? 1 : -1;
					if(posor != orit->second){
						posor += posor < orit->second ? 1 : -1;
					}
					++time;
				}
				++time;	//press button
				if(posor != orit->second){
					posor += posor < orit->second ? 1 : -1;
				}
				++bluit;
			}

			else{
				while(posor != orit->second){
					posor += posor < orit->second ? 1 : -1;
					if(posblu != bluit->second){
						posblu += posblu < bluit->second ? 1 : -1;
					}
					++time;
				}
				++time;	//press button
				if(posblu != bluit->second){
					posblu += posblu < bluit->second ? 1 : -1;
				}
				++orit;
			}
			//cout<<"posor: "<<posor<<endl;
			//cout<<"posblu: "<<posblu<<endl;
		}

		while(bluit!=blues.end()){
			while(posblu != bluit->second){
				posblu += posblu < bluit->second ? 1 : -1;
				++time;
			}
			++time;
			++bluit;
			//cout<<"posblu: "<<posblu<<endl;
		}
		while(orit!=oranges.end()){
			while(posor != orit->second){
				posor += posor < orit->second ? 1 : -1;
				++time;
			}
			++time;
			++orit;
			//cout<<"posor: "<<posor<<endl;
		}
		ofstr<<"Case #"<<i+1<<": "<<time<<endl;
	}

	int exit;
	cin>>exit;
	return 0;
}

int abs(int a){
	return a < 0 ? -a : a;
}