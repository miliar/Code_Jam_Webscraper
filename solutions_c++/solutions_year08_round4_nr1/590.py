#define inFileName "a-large.in"
#define outFileName "a-large.out"

#include <cstdio>
#include <iostream>
#include <fstream>

//FILE * f = fopen(inFileName,"rt");
//FILE * g = fopen(outFileName,"wt");
std::ifstream f(inFileName,std::ifstream::in);
std::ofstream g(outFileName,std::ofstream::out);

#include <strstream>
#include <sstream>

#include <cmath>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>

#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;
typedef __int64 ll;

#define all(v) (v).begin(),(v).end()
#define foreach(it, v, type) for(type::iterator it = (v).begin(); it != (v).end(); ++it)
#define forn(i,N) for(int i=0;i<(N); ++i)
#define pb push_back

//////////////////////////////////////////////////////////////////////////
int m,n,v;
VI G;
VI C;
VI L;
VI NewG;

int getV(int i)
{
	if (i>(m-1)/2) return L[i];
	if (NewG[i]) return getV(2*i) && getV(2*i+1);
	else return getV(2*i) || getV(2*i+1);
};

#define INF 1000000

int BestRes = INF;
VI changed;
map<int,int> res[2];

int getminChanges(int i,int val)
{
	if (i>(m-1)/2)
	{
		if (L[i]==val) return 0;
		else return INF;
	}

	if (res[val].find(i)!=res[val].end())
		return res[val][i];


	int bestSoFar = INF;
	if (G[i])  //and gate
	{
		if (val==1)
			bestSoFar = min(bestSoFar,getminChanges(2*i,1)+getminChanges(2*i+1,1)); 
		else 
			bestSoFar = min(bestSoFar,min(getminChanges(2*i,0),getminChanges(2*i+1,0)));
	}
	else
	{
		if (val==1)
			bestSoFar = min(bestSoFar,min(getminChanges(2*i,1),getminChanges(2*i+1,1))); 
		else 
			bestSoFar = min(bestSoFar,getminChanges(2*i,0)+getminChanges(2*i+1,0));
	}

	if (!C[i])
		return bestSoFar;
	
	G[i]=1-G[i];
	if (G[i])  //and gate
	{
		if (val==1)
			bestSoFar = min(bestSoFar,getminChanges(2*i,1)+getminChanges(2*i+1,1)+1); 
		else 
			bestSoFar = min(bestSoFar,min(getminChanges(2*i,0),getminChanges(2*i+1,0))+1);
	}
	else
	{
		if (val==1)
			bestSoFar = min(bestSoFar,min(getminChanges(2*i,1),getminChanges(2*i+1,1))+1); 
		else 
			bestSoFar = min(bestSoFar,getminChanges(2*i,0)+getminChanges(2*i+1,0)+1);
	}
	G[i]=1-G[i];
	res[val][i]=bestSoFar;
	return bestSoFar;
}

int main()
{
	int nTests; f>>nTests;
	string s;

	forn(TestIndex,nTests)
	{
		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<TestIndex+1<<": ";
		cout<<"Case #"<<TestIndex+1<<": ";
		f>>m>>v;
		G.resize(m+1);
		C.resize(m+1);
		L.resize(m+1);
		NewG.resize(m+1);

		for(int i=1;i<=(m-1)/2;i++)
			f>>G[i]>>C[i];
		
		for(int i=(m-1)/2+1;i<=m;i++)
			f>>L[i];

		changed.resize(m+1);
		forn(i,changed.size()) changed[i]=false;

		res[0].clear();
		res[1].clear();
		
		int BestRes= getminChanges(1,v);
		if (BestRes<INF)	
			g<<BestRes<<endl,
			cout<<BestRes<<endl;
		else
			g<<"IMPOSSIBLE"<<endl,
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
