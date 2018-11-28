//
//  main.cpp
//
//  Created by Prateek Sachdev 
//  Copyright (c) 2013 Prateek Sachdev. All rights reserved.
//
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <cstring>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <iostream>

using namespace std;

typedef vector<int > vd;

#define sd(n) scanf("%d",&n)
#define sc(n) scanf("%c",&n)
#define sf(n) scanf("%f",&n)
#define ss(n) scanf("%s",n)
#define pd(n) printf("%d\n",n)
#define pb push_back

#define SIEVE(a) ({int b=ceil(sqrt(a));vd d(a,0);vd e;int f=2;e.pb(2);e.pb(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.pb(c);}}e;})
template<class T> inline vector<pair<T,int> > FACTORISE(T n){vector<pair<T,int> >R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline T TOTIENT(T n) {vector<pair<T,int> > R=FACTORISE(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}

// vd v=SIEVE(2100);
// int n=TOTIENT(num);

char s[4][4];
int win(char ch)
{

	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if((s[i][0]==ch || s[i][0]=='T') && (s[i][1]==ch || s[i][1]=='T') && (s[i][2]==ch ||  s[i][2]=='T') &&  (s[i][3]==ch ||  s[i][3]=='T'))
				return 1;
			if((s[0][i]==ch || s[0][i]=='T') && (s[1][i]==ch || s[1][i]=='T') && (s[2][i]==ch || s[2][i]=='T') && (s[3][i]==ch ||  s[3][i]=='T'))
				return 1;
		}

	}
	if((s[0][0]==ch || s[0][0]=='T') && (s[1][1]==ch ||s[1][1]=='T') && (s[2][2]==ch || s[2][2]=='T') && (s[3][3]==ch || s[3][3]=='T') )
		return 1;
	if((s[0][3]==ch || s[0][3]=='T') && (s[1][2]==ch || s[1][2]=='T') && (s[2][1]==ch || s[2][1]=='T') && (s[3][0]==ch || s[3][0]=='T') )
		return 1;
	else return 0;
}

int main()
{	
	int countx=0;
	int counto=0;
	int countt=0;
	int wx,wo;
	char ch,nl;

	int t;
	sd(t);
	int caseno=0;
	while(t--)
	{
		caseno++;
		sc(nl);//newline
		countx=0;
		counto=0;
		countt=0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			sc(s[i][j]);
			countx+=s[i][j]=='X';
			counto+=s[i][j]=='O';
			countt+=s[i][j]=='T';
		//	if(s[i][j]=='0')
		//		printf("found\n");
			
		}
		sc(ch);

	}
	
	wx=win('X');
	wo=win('O');

	if(wx)
		cout << "Case #"<< caseno << ": X won" << endl;
	else if(wo)
		cout << "Case #"<< caseno << ": O won" << endl;
	else if(countx+countt+counto==16)
		cout << "Case #"<< caseno << ": Draw"<< endl;
	else
		cout<< "Case #"<< caseno << ": Game has not completed" << endl;
	}
	return 0;

}



