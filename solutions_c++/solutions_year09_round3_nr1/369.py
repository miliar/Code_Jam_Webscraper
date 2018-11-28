#include<stdlib.h>
#include<iostream>
#include<sstream>
#include<math.h>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<set>
#include<map>
#include<numeric>
#include<algorithm>
#include<stdio.h>

using namespace std;

#define for0(i,n) for((i)=0;(i)<(n);(i)++)
#define for1(i,n) for((i)=1;(i)<=(n);(i)++)
#define min2(a,b) (a)<(b)?(a):(b)
#define min3(a,b,c) ((a)<(b)?(a):(b))<(c)?((a)<(b)?(a):(b)):(c)
#define min4(a,b,c,d) min3(a,b,c)<d?min3(a,b,c):d
#define max2(a,b) (a)>(b)?(a):(b)
#define max3(a,b,c) ((a)>(b)?(a):(b))>(c)?((a)>(b)?(a):(b)):(c)
#define max4(a,b,c,d) max3(a,b,c)>d?max3(a,b,c):d

#define swap(a,b,t) t=a;a=b;b=t;

#define inf 1000000000
#define iss istringstream

#define vi vector<int>
#define vs vector<string>
#define vd vector<double>
#define ssc sscanf
#define sp sprintf
#define pb push_back
#define sortv(x) sort(x.begin(),x.end())

#define cname c
#define fname f
#define lvars  int l1=0,l2=0,l3=0,l4=0
#define tvars  int t1=0,t2=0,t3=0,t4=0

#define dec(c) (((c)>='0'&&(c)<=9))?((c)-'0'):(((c)>='a'&&(c)<='f')?(c)-'a'+10:(c)-'A'+10)

int main()
{
	int t,t1=1;
	cin>>t;
	while(t--)
	{
		char buf[100];
		cin>>buf;
		set<char> s;
		int l=strlen(buf),i,j,k,b;
		for0(i,l)
		{
			s.insert(buf[i]);
		}
		k=s.size();
		b= max(k,2);
		map<char,int> m;
		vector<int> num;
		vector<int> base;
		base.push_back(1);
		base.push_back(0);
		for(i=2;i<b;i++)base.push_back(i);
		for(i=0,j=0;i<l;i++)
		{
			if(s.find(buf[i])!=s.end())
			{
				m[buf[i]]=base[j];
				s.erase(buf[i]);
				j++;
			}
		}
		for0(i,l)
		{
			num.push_back(m[buf[i]]);
		}
		long long res=0LL;
		for(i=0;i<num.size();i++)
		{
			res = res*(long long)b+(long long)num[i];
		}
		printf("Case #%d: %lld\n",t1,res);
		t1++;
	}
	return 0;
}