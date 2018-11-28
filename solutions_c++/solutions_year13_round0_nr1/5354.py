/*
LANG: C++
ID: fox05711
PROG: a-small.cpp
*/
//==========================================
#include <iostream>
#include <cctype>
#include <map>
#include <set>
#include <sstream>
#include <cstring>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <list>
#include <cmath>
#include <algorithm>
#include <set>
#include <fstream>

using namespace std;
int main(){
	int t;
	char a[4][4];
	ifstream fin("A-small-attempt0.in");
	ofstream fout("a-small.out");
	fin>>t;
	for (int i=0;i<t;i++){
		for (int c=0;c<4;c++){
			for (int r=0;r<4;r++){
				fin>>a[c][r];
			}
		}
		int pri=0;
		bool end=false;
		for (int c=0;c<4;c++){
			int x=0;
			int o=0;
			int tt=0;
			for (int r=0;r<4;r++){
				if (a[c][r]=='X') x++;
				if (a[c][r]=='O') o++;
				if (a[c][r]=='T') tt++;
				if (a[c][r]=='.') pri++;
			}
			if (x==4 || (x==3 && tt==1)){
				fout<<"Case #"<<(i+1)<<": X won"<<endl;
				end=true;
				break;
			}
			if (o==4 || (o==3 && tt==1)){
				fout<<"Case #"<<(i+1)<<": O won"<<endl;
				end=true;
				break;
			}
		}
		if (!end){
			pri=0;
			for (int r=0;r<4;r++){
				int x=0;
				int o=0;
				int tt=0;
				for (int c=0;c<4;c++){
					if (a[c][r]=='X') x++;
					if (a[c][r]=='O') o++;
					if (a[c][r]=='T') tt++;
					if (a[c][r]=='.') pri++;
				}
				if (x==4 || (x==3 && tt==1)){
					fout<<"Case #"<<(i+1)<<": X won"<<endl;
					end=true;
					break;
				}
				if (o==4 || (o==3 && tt==1)){
					fout<<"Case #"<<(i+1)<<": O won"<<endl;
					end=true;
					break;
				}
			}
		}
		if (!end){
			pri=0;
			int x=0;
			int o=0;
			int tt=0;
			for (int c=0;c<4;c++){
				if (a[c][c]=='X') x++;
				if (a[c][c]=='O') o++;
				if (a[c][c]=='T') tt++;
				if (a[c][c]=='.') pri++;
			}
			if (x==4 || (x==3 && tt==1)){
				fout<<"Case #"<<(i+1)<<": X won"<<endl;
				end=true;
			}
			if (o==4 || (o==3 && tt==1)){
				fout<<"Case #"<<(i+1)<<": O won"<<endl;
				end=true;
			}
		}
		if (!end){
			pri=0;
			int x=0;
			int o=0;
			int tt=0;
			for (int c=0;c<4;c++){
				if (a[c][3-c]=='X') x++;
				if (a[c][3-c]=='O') o++;
				if (a[c][3-c]=='T') tt++;
				if (a[c][3-c]=='.') pri++;
			}
			if (x==4 || (x==3 && tt==1)){
				fout<<"Case #"<<(i+1)<<": X won"<<endl;
				end=true;
			}
			if (o==4 || (o==3 && tt==1)){
				fout<<"Case #"<<(i+1)<<": O won"<<endl;
				end=true;
			}
		}

		if (!end){
			if (pri==0) fout<<"Case #"<<(i+1)<<": Draw"<<endl;
			else fout<<"Case #"<<(i+1)<<": Game has not completed"<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}
