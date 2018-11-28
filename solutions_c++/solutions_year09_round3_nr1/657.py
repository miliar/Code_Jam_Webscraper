#include "stdafx.h"
#include <vector>
#include <math.h>
#include <string>
#include <set>
#include <iostream>
#include <map>
#include <algorithm>
#include <sstream>
using namespace std;

long long ord(char a)
{
	if ( (a>='0') && (a<='9') )
		return a-'0';
	return a-'a'+(long long)10;
}

long long stol(const string &S,long long K)
{
	long long res=0;
	for(int i=0;i<S.length();i++)
		res=res*K+ord(S[i]);
	return res;
}

int main(){

	freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);

	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		long long ANS=1000000000000000001;
		string S;
		cin>>S;
		
		set<char> QQQ;
		for(int j=0;j<S.length();j++)
			QQQ.insert(S[j]);
		int mink=max(QQQ.size(),(unsigned int)2);
		for(int K=mink;K<=36;K++)
		{
			vector<char> have;
			for(int j=0;j<min(K,10);j++)
				have.push_back(j+'0');
			for(char j='a';j<='z';j++)
			{
				if (have.size()==K)
					break;
				have.push_back(j);
			}
			reverse(have.begin(),have.end());
			map<char,char> Q;
			string res;
			res.push_back(have[have.size()-2]);
			have.erase(have.end()-2);
			Q[S[0]]=res[0];
			for(int j=1;j<S.length();j++)
			{
				if (Q.count(S[j]))
					res.push_back(Q[S[j]]);
				else
				{
					res.push_back(have.back());
					Q[S[j]]=have.back();
					have.pop_back();
				}
			}
			//reverse(res.begin(),res.end());
			long long VAL=stol(res,K);
			ANS=min(ANS,VAL);
			
		}
		printf("Case #%d: %lld\n",i+1,ANS); 
	}
	
	return 0;
}