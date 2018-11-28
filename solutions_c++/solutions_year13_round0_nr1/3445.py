//G:\tech\C++\Microsoft\Microsoft\Microsoft\Google-1-Tic-Tac-Toe-Tomek.cpp

#include "stdafx.h"
#include<iostream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

map<int,int> Xplayer;
map<int,int> Oplayer;

int combo[10][4]={{0,1,2,3},{4,5,6,7},{8,9,10,11},{12,13,14,15},{0,4,8,12},{1,5,9,13},{2,6,10,14},{3,7,11,15},{0,5,10,15},{3,6,9,12}};


int main()
{
	int T;
	ifstream in("d://test//G//A-large.in");
	ofstream out("d://test//G//output.txt");
	in>>T;
	for(int i=1;i<=T;i++)
	{
		Xplayer.clear();
		Oplayer.clear();
		char data[4][5];
		int flag=0;
		for(int a=0;a<4;a++){
			in>>data[a];
		}
		bool finished=true;	
		for(int a=0;a<4;a++){
			for(int b=0;b<4;b++){
				switch(data[a][b]){
				case 'X':Xplayer[4*a+b]=1;break;
				case 'O':Oplayer[4*a+b]=1;break;
				case 'T':Xplayer[4*a+b]=1;Oplayer[4*a+b]=1;break;
				case '.':finished=false;break;
				}
			}
		}
		bool Xwin=true,Owin=true;
		for(int a=0;a<10;a++){
			Xwin=true;
			for(int b=0;b<4;b++){
				if(Xplayer.count(combo[a][b])==0){
					Xwin=false;
					break;
				}
			}
			if(Xwin)
				break;
		}
		if(Xwin){
			flag=1;
		}
		else{
			for(int a=0;a<10;a++){
				Owin=true;
				for(int b=0;b<4;b++){
					if(Oplayer.count(combo[a][b])==0){
						Owin=false;
						break;
					}
				}
				if(Owin)
					break;
			}
			if(Owin){
				flag=2;
			}
			else if(finished){
				flag=4;
			}
			else{
				flag=3;
			}
		}
		out<<"Case #"<<i<<": ";
		switch(flag){
		case 1:out<<"X won"<<endl;break;
		case 2:out<<"O won"<<endl;break;
		case 3:out<<"Game has not completed"<<endl;break;
		case 4:out<<"Draw"<<endl;break;
		}
	}
	out.close();
	return 0;
}