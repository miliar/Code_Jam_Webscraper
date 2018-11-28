#include<vector>
#include<map>
#include<set>
#include <iostream>
#include "basetsd.h"
#include <algorithm>
#include "queue"
#include "math.h"
#include<string>
#include "assert.h"
#include<stack>

using namespace std;


//To take variable num of things as inp...
void t1()
{
	int nt;
	cin >> nt;
	string temp;
	getline(cin,temp);
	for (int tc=0;tc<nt;++tc)
	{
		string str;
		getline(cin,str);
		char *pch; 
		pch = strtok((char*)str.c_str()," ");
		while (pch != NULL)
		{
			int i = atoi(pch);
			pch = strtok(NULL," ");
			cout << i << "\n";
		}
		
	}
}

//int dp[101][101];
//
//int GetMinBribe(int k, int l, vector<int>& B,vector<bool> flag)
//{
//	if (dp[k][l] != -1)
//	{
//		return dp[k][l];
//	}
//	if (k > l)
//	{
//		dp[k][l] = 0;
//		return 0;
//	}
//	if (k == l)
//	{
//		int ind = B[k];
//		dp[k][l] = B[k+1]-B[k-1];
//		return dp[k][l];
//	}
//	long minB =  1000000000000;
//	for (int z=k;z<=l;++z)
//	{
//		int bb = GetMinBribe(k,z-1,B) + GetMinBribe(z+1,l,B)
//		if ()
//		{
//		}
//	}
//}
//
//void func()
//{
//	int nT;
//	cin >> nT;
//	for (int i=0;i<101;++i)
//		for(int j=0;j<101;++j)
//			dp[i][j] = -1;
//
//
//	for (int tc=0;tc<nT;++tc)
//	{
//		int P;
//		int Q;
//		cin >> P;
//		cin >> Q;
//		vector<int> B(Q+2,0);
//		vector<bool> flag(Q+1,false);
//		B[0] = 1;
//		B[Q+1] = P;
//		for(int i=1;i<=Q;++i)
//			cin >> B[i];
//		GetMinBribe(1,Q,B,flag);
//	}
//}

void One()
{
	int nT;
	cin >> nT;
	string str;
	getline(cin,str);
	for (int tc=0;tc<nT;++tc)
	{
		string tmp;
		getline(cin,tmp);
		set<char> s;
		for (int i=0; i<tmp.size(); ++i)
			s.insert(tmp[i]);
		
		int distsymb = s.size();
		if(distsymb == 1)
			distsymb=2;
		map<char,int> mp;
		
		mp.insert(make_pair(tmp[0],1));
		int k=1;
		while (tmp[k] == tmp[0]) 
		  k++;
		if (k<tmp.size())
			mp.insert(make_pair(tmp[k],0));	
		
		int next = 2;
		for (int i=k+1;i<tmp.size();++i)
		{
			if (mp.find(tmp[i]) == mp.end())
			{
				mp.insert(make_pair(tmp[i],next));
				next++;
			}
		}
		unsigned long long int lng=0;
		for(int i=0;i<tmp.size();++i)
		{
			int val = mp[tmp[i]];
			lng += (unsigned long long int)(val * pow((double)distsymb,(double)tmp.size()-i-1));
		}
		cout << "Case #"<<tc+1<<": "<<lng<<"\n";
	}
}
int main()
{

	One();
	return 0;
}