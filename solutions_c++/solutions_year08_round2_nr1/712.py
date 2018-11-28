// coded by Martin Tillmann for the Google Code Jam 08 contest.

#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
#include "bigint.h"
#include "bigint.c"
using namespace std;


int main()
{
string s;
getline(cin ,s);
int cases;
stringstream(s) >> cases;
for(int casecounter=0;casecounter<cases;casecounter++)
	{
	unsigned long n,A,B,C,D,x0,y0,M;
	cin >> s; stringstream(s) >> n;
	cin >> s; stringstream(s) >> A;
	cin >> s; stringstream(s) >> B;
	cin >> s; stringstream(s) >> C;
	cin >> s; stringstream(s) >> D;
	cin >> s; stringstream(s) >> x0;
	cin >> s; stringstream(s) >> y0;
	cin >> s; stringstream(s) >> M;
	unsigned long trees[n][2];
	trees[0][0]=x0; trees[0][1]=y0;
	unsigned long X=x0,Y=y0;
	for(unsigned long i=1;i<n;i++)
		{
		bigint bA(A);
		bigint bX(X);
		bigint bB(B);
		bigint bM(M);
		bX=(bA*bX+bB)%bM;
		X=bX;
		bigint bC(C);
		bigint bY(Y);
		bigint bD(D);
		bY=(bC*bY+bD)%bM;
		Y=bY;
		trees[i][0]=X; trees[i][1]=Y;
		}
	unsigned long erg=0;
	for(unsigned long first=0;first<n;first++) {
	for(unsigned long second=0;second<n;second++) {
	for(unsigned long third=0;third<n;third++)
		{
		if(first==second || first==third || second==third) continue;
		int xa=trees[first][0]%3;
		int xb=trees[second][0]%3;
		int xc=trees[third][0]%3;
		int ya=trees[first][1]%3;
		int yb=trees[second][1]%3;
		int yc=trees[third][1]%3;
		if(((xa+xb+xc)%3)==0 && ((ya+yb+yc)%3)==0) erg++;
//		unsigned long testX=trees[first][0]+trees[second][0]+trees[third][0];
//		unsigned long testY=trees[first][1]+trees[second][1]+trees[third][1];
//		if(((testX%3)==0) && ((testY%3)==0)) erg++;
		}}}
//	if((erg%6)!=0) cout << "WTF" << endl;
	erg=erg/6;
	cout << "Case #" << casecounter+1 << ": " << erg << "\n";
	}
return 0;
}
