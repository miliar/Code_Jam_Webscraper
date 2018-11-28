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
#define ALL(t) t.begin(),t.end()
#define FORnm(i,n,m) for (int i=n; i<=(int)(m); i++)
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

int dx[]={1,1,0,-1},dy[]={0,1,1,1};
#define MAXIMO 10000

int main()
{
//	FILE *fp=fopen("D-small-attempt3.in", "r"), *ofp=fopen("respuestaS.out", "w");
	FILE *fp=fopen("D-large.in", "r"), *ofp=fopen("respuestaL.out", "w");
	int i, j, tc,T,N,a,max;
	float res;
	fscanf(fp, "%d", &T);
	deque<int> Nums;
	FORnm(tc,1,T)
	{
	 	Nums.clear();					 
		fscanf(fp, "%d", &N);
		forn(i,N)
		{
		  fscanf(fp, "%d", &a); 
	    Nums.pb(a);
		}
		res=0.0;
		forn(i,Nums.size())
		  if(Nums[i]!=i+1)
		    res++;
		// print cases
		fprintf(ofp, "Case #%d: %.6f\n", tc, res);
	}
	return 0;
}

