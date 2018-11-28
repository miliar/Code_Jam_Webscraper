#include<cstdio>
#include <cctype>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include <deque>
#include <math.h>
#include<stdio.h>
#include<memory.h>
using namespace std;


typedef stringstream ss;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long int64;

#define PI 3.14159265
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define FORnm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000

int main()
{
//	freopen("A-small-attempt3.in", "r", stdin);
//	freopen("respuestaS.out", "w+", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("respuestaL.out", "w+", stdout);


	int i, j, tc,m,n,b;
	int posiniB,posiniO;
	int cnt,indO,indB,indS,jump;
	vi B,O;
	vector<char> Sec;
	char t;
	cin >>m;
	
	FORnm(tc,1,m)
	{
	 	B.clear();O.clear();					 
	 	Sec.clear();
		cin >> n;
		cnt=0;
		indO=indB=indS=0;
		posiniB=1,posiniO=1;
		forn(i,n)
		{
		  cin >> t >> b;
		   ( t=='O')?O.pb(b):B.pb(b);
			 Sec.pb(t);
		}
		while( indO<O.size() ||  indB<B.size())
		{
		   if(Sec[indS++]=='O')
			 {
			 	  jump = abs(O[indO++]-posiniO)+1;
					posiniO=O[indO-1];								 
			 	  cnt +=jump;
			 	  if(B[indB]>posiniB)
					 {
					  if(B[indB]<=posiniB+jump )
					 	  posiniB=B[indB];
				 	  else
				 	    posiniB+=jump;
					 }
			    else
			    {
					  if(B[indB]>=posiniB-jump )
					 	  posiniB=B[indB];
				 	  else
				 	    posiniB-=jump;
					 }			 	  
				}			 
				else
				{
			 	  jump = abs(B[indB++]-posiniB)+1;	
					posiniB=B[indB-1];								  							 
			 	  cnt +=jump;
			 	  if(O[indO]>posiniO)
					 {
					  if(O[indO]<=posiniO+jump )
					 	  posiniO=O[indO];
				 	  else
				 	    posiniO+=jump;
					 }
			    else
			    {
					  if(O[indO]>=posiniO-jump )
					 	  posiniO=O[indO];
				 	  else
				 	    posiniO-=jump;
					 }			 	  
				}			 
		}
		// print cases
		cout<<"Case #"<<tc<<": "<< cnt<<endl;
	}
	return 0;
}
