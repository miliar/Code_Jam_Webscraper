#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <fstream>
using namespace std;
int ans=0;
vector<int> gates;
vector<int> trees;
vector<int> change;
//bool flag[200];
bool found=false;
int M,V;
int cal(){
	for (int i=gates.size()-1;i>=0;--i)
	{
		if (gates[i]==1)
		{
			trees[i]=trees[i*2+1]&trees[i*2+2];
		}
		else
		{
			trees[i]=trees[i*2+1]|trees[i*2+2];
		}
	}
	return trees[0];
}
void test(int n,int a){
	if (!found)
	{
		if (n==0)
		{
			if (cal()==V)
			{
				found=true;
				return ;
			}
		}
		if (a>=change.size())
		{
			return;
		}
		int index=change[a];
		gates[index]=1-gates[index];
		test(n-1,a+1);
		gates[index]=1-gates[index];
		test(n,a+1);
	}
}

int main()
{
	ifstream fin("in.in");
	ofstream fout("out.out");
	int N;
	fin>>N;



	for (int cc=1;cc<=N;++cc)
	{
		fin>>M>>V;
		trees.resize(M);
		gates.resize((M-1)/2);
		change.clear();
		for (int j=0;j<(M-1)/2;++j)
		{
			int a;
			fin>>gates[j];
			fin>>a;
			if (a==1)
			{
				change.push_back(j);
			}
		}
		for (int j=(M-1)/2;j<M;++j)
		{
			fin>>trees[j];
		}
		found=false;
		for (int i=0;i<=change.size();++i)
		{
			test(i,0);
			if (found)
			{
				ans=i;
				break;
			}
		}
		if (found)
		{
			fout<<"Case #"<<cc<<": "<<ans<<endl;
		}
		else
		{
			fout<<"Case #"<<cc<<": "<<"IMPOSSIBLE"<<endl;
		}



	
	}
	

	return 0;
}

