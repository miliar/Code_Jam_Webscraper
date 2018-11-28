// b.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,R,K,N,n;
	cin>>T;
	vector<int> g;
	vector<int> getin;
	vector<int>::iterator git;
	int total,local;
	for (int i=0; i<T; i++)
	{
		cin>>R>>K>>N;
		g.clear();total=0;
		getin.clear();
		for (int j=0; j<N; j++)
		{
			cin>>n;
			g.push_back(n);
		}
		for (int k=0; k<R; k++)
		{
			local=0;
			git=g.begin();
			while ((local+(*git))<=K)
			{
				n=(*git);
				local+=n;
				g.erase(git);
				getin.push_back(n);	
				if (g.size()==0)
					break;
				git=g.begin();
			}			
			total+=local;
			g.insert(g.end(),getin.begin(),getin.end());
			getin.clear();
		}
		cout<<"Case #"<<i+1<<": "<<total<<endl;		
	}
	return 0;
}

