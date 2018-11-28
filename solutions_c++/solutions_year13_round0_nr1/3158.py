/*
 * gcj1.cpp
 *
 *  Created on: 2013/04/13
 *      Author: DO
 */

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<algorithm>
#include<functional>
#include<utility>
#include<cmath>
#include<complex>
#include<iomanip>

using namespace std;

#define REP(i,s,e) for(int i=int(s);i<=int(e);i++)
#define rep(i,n) for(int i=0;i<int(n);i++)
#define pi 3.14159265358979


int main(void){

	int t;
	cin >> t;

	rep(i,t){

	char b[5][5];
	rep(j,4)
	rep(k,4)
	cin >> b[j][k];

	bool f=false; int d=0;
	rep(j,4){
		int x1=0,o1=0,s1=0,
		    x2=0,o2=0,s2=0;
		rep(k,4){
			if(b[j][k]=='X') x1++;
			if(b[j][k]=='O') o1++;
			if(b[j][k]=='T') s1++;

			if(b[k][j]=='X') x2++;
			if(b[k][j]=='O') o2++;
			if(b[k][j]=='T') s2++;

			if(b[k][j]=='.') d++;
		}

		if(x1==4 || (x1==3 && s1==1)){
		cout << "Case #" << i+1 << ": " << "X won" << endl;
		f=true;
		break;
		}
		if(o1==4 || (o1==3 && s1==1)){
		cout << "Case #" << i+1 << ": " << "O won" << endl;
		f=true;
		break;
		}

		if(x2==4 || (x2==3 && s2==1)){
		cout << "Case #" << i+1 << ": " << "X won" << endl;
		f=true;
		break;
		}
		if(o2==4 || (o2==3 && s2==1)){
		cout << "Case #" << i+1 << ": " << "O won" << endl;
		f=true;
		break;
		}
	}



    if(!f){

	int x3=0,o3=0,s3=0,
	    x4=0,o4=0,s4=0;
	rep(j,4){

	if(b[j][j]=='X') x3++;
	if(b[j][j]=='O') o3++;
	if(b[j][j]=='T') s3++;

	if(b[j][3-j]=='X') x4++;
	if(b[j][3-j]=='O') o4++;
	if(b[j][3-j]=='T') s4++;
	}

	if(x3==4 || (x3==3 && s3==1)){
	cout << "Case #" << i+1 << ": " << "X won" << endl;
	f=true;
	}
	if(o3==4 || (o3==3 && s3==1)){
	cout << "Case #" << i+1 << ": " << "O won" << endl;
	f=true;
	}

	if(x4==4 || (x4==3 && s4==1)){
	cout << "Case #" << i+1 << ": " << "X won" << endl;
	f=true;
	}
	if(o4==4 || (o4==3 && s4==1)){
	cout << "Case #" << i+1 << ": " << "O won" << endl;
	f=true;
	}

    }


	if(!f && d==0)
	cout << "Case #" << i+1 << ": " << "Draw" << endl;

	if(!f && d!=0)
	cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;

	}

	return 0;
}



