//============================================================================
// Name        : DA.cpp
// Author      : Loc Ngo
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

bool M[51];
int B[51];
int MM[51];
int N;

bool pureDFS(int v,int u,vector<int> V[51])
{
	MM[u] = true;
	for(int i=0;i<V[u].size();i++)
		if(!MM[V[u][i]])
		{
			if(V[u][i] == v)
				return true;
			if(pureDFS(v,V[u][i],V))
				return true;
		}
	return false;
}

bool remove(int u,int v,int uu, int vv,vector<int> A[51])
{
	vector<int> V[51];
	for(int i=1;i<=N;i++)
		for(int j=0;j<A[i].size();j++)
			if(i==u&&A[i][j]==v)
				continue;
			else
				V[i].push_back(A[i][j]);
	fill(MM,MM+51,false);
	return pureDFS(vv,uu,V);
}

bool checkDifferentPath(int uu,int v,vector<int> A[51])
{
	int vv = v;
	while(true)
	{

		int u = B[v];
		if(remove(u,v,uu,vv,A))
			return true;
		if(u==uu)
			break;
		v = u;
	}
    return false;
}

bool DFS(int S,int u,vector<int> A[51])
{

	M[u] = true;
	for(int i=0;i<A[u].size();i++)
		if(!M[A[u][i]])
		{
			B[A[u][i]] = u;
			if(checkDifferentPath(S,A[u][i],A))
				return true;
			if(DFS(S,A[u][i],A))
				return true;
		}
	return false;
}

bool satisfy(int u,vector<int> A[51])
{

	fill(M,M+51,false);
	B[u] = 0;
	return DFS(u,u,A);
}

void process(int t)
{
	fout<<"Case #"<<t<<": ";
	fin>>N;
	vector<int> A[51];
	for(int i=1;i<=N;i++)
	{
		int K;
		fin>>K;
		for(int j=1;j<=K;j++)
		{
			int v;
			fin>>v;
			A[i].push_back(v);
		}
	}

	for(int i=1;i<=N;i++)
		if(satisfy(i,A))
		{
			fout<<"Yes\n";
			return;
		}
	fout<<"No\n";
}

int main() {
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
		process(i);

	return 0;
}
