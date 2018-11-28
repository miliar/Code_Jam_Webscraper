#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("ans.out");
	int n, Xcol[4], Ocol[4], Xdia, Odia, Xndia, Ondia;
	int o,x,win,flag;
	char Game[4][4];
	infile >> n;
	for(int cnt=1; cnt<=n; cnt++){
		win=-1;Xdia=0;Odia=0;flag=0;Xndia=0;Ondia=0;
		for(int i=0; i<4; i++){
			Xcol[i]=0;Ocol[i]=0;
		}
		for(int i=0; i<4; i++){
			x=0;o=0;
			for(int j=0; j<4; j++){
				infile >> Game[i][j];
				if(Game[i][j] == 'X' || Game[i][j] == 'T'){
					x++;
					Xcol[j]++;
					if(Xcol[j] == 4)win=0;
				}
				if(Game[i][j] == 'O' || Game[i][j] == 'T'){
					o++;
					Ocol[j]++;
					if(Ocol[j] == 4)win=1;
				}
				if(i==j && (Game[i][j] == 'X' || Game[i][j] == 'T'))
					Xdia++;
				if(i==j && (Game[i][j] == 'O' || Game[i][j] == 'T'))
					Odia++;
				if(i==3-j && (Game[i][j] == 'X' || Game[i][j] == 'T'))
					Xndia++;
				if(i==3-j && (Game[i][j] == 'O' || Game[i][j] == 'T'))
					Ondia++;
				if(Game[i][j] == '.')
					flag=1;
			}
			if(x==4) win=0;
			if(o==4) win=1;
		}
		if(Xdia==4)win=0;
		if(Odia==4)win=1;
		if(Xndia==4)win=0;
		if(Ondia==4)win=1;
		outfile  << "Case #" << cnt << ": ";
		if(win==1)
			outfile << "O won\n" << endl;
		else if(win==0)
			outfile << "X won\n" << endl;
		else if(win==-1 && flag==0)
			outfile << "Draw\n" << endl;
		else if(win==-1 && flag==1)
			outfile << "Game has not completed\n" << endl;
	}
	return 0;
}
