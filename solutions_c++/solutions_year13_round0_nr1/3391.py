#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>
#include <cstring>
using namespace std;
void checks(char X, int &chkX1, int &chkO1, bool &T1){
	if(X == 'X')chkX1++;
	else if(X == 'O')chkO1++;
	else if(X == 'T')T1 = true;}
int main() {

	freopen("a.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tr; cin>>tr;
	int chkX1, chkX2, chkO1, chkO2;
	bool dots, T1, T2;

	char A[4][4];
	for(int hh = 0 ; hh < tr; hh++){

		for(int i =0 ; i < 4;i++)for(int j =0 ; j < 4;j++)cin>>A[i][j];

		dots = false;
		for(int i =0; i < 4; i++)
		{
			chkX1=0; chkX2=0; chkO1=0; chkO2=0;
			T1 = false;T2 = false;
			for(int j =0 ; j < 4; j++)
			{
				checks(A[i][j], chkX1, chkO1, T1);
				checks(A[j][i], chkX2, chkO2, T2);
				if(A[i][j] == '.' || A[j][i] == '.')dots = true;
			}

			if(chkX1 == 4 || chkX2 == 4 || (chkX1 == 3 && T1) || (chkX2 == 3 && T2)) {
				cout<<"Case #"<<hh+1<<": X won"<<endl;goto exits;}
			else if(chkO1 == 4 || chkO2 == 4 || (chkO1 == 3 && T1) || (chkO2 == 3 && T2)) {
				cout<<"Case #"<<hh+1<<": O won"<<endl; goto exits;}

		}
		chkX1=0; chkX2=0; chkO1=0; chkO2=0;
		T1 = false;T2 = false;
		for(int i =0 ; i < 4; i++)
		{checks(A[i][i], chkX1, chkO1, T1);
			checks(A[i][3-i], chkX2, chkO2, T2);}

		if(chkX1 == 4 || chkX2 == 4 || (chkX1 == 3 && T1) || (chkX2 == 3 && T2)) {
			cout<<"Case #"<<hh+1<<": X won"<<endl;goto exits;}
		else if(chkO1 == 4 || chkO2 == 4 || (chkO1 == 3 && T1) || (chkO2 == 3 && T2)) {
			cout<<"Case #"<<hh+1<<": O won"<<endl; goto exits;}

		if(!dots)
			cout<<"Case #"<<hh+1<<": Draw"<<endl;
		else
			cout<<"Case #"<<hh+1<<": Game has not completed"<<endl;
exits: continue;
	}
	return 0;
}