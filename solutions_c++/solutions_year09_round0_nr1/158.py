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

int l,d,n;
vs vocab;

int main()
{
	int i,j,k,tc=1;
	scanf("%d %d %d",&l,&d,&n);
	for(i=0;i<d;i++)
	{
		char buf[100];
		scanf("%s",buf);
		vocab.push_back(buf);
	}

	while(n--)
	{
		char buf[600];
		int t[30][20];
		scanf("%s",buf);
		memset(t,0,sizeof(t));
		int len = strlen(buf),mode=0,tok=0,res=0;
		for(i=0;i<len;i++)
		{
			if(buf[i]=='(')mode = 1;
			else if(buf[i]==')'){mode = 0;tok++;}
			else if(mode == 1)t[buf[i]-'a'][tok]=1;
			else if(mode == 0){t[buf[i]-'a'][tok]=1;tok++;}
		}
		for(i=0;i<d;i++)
		{
			for(j=0;j<l;j++)
			{
				if(t[vocab[i][j]-'a'][j]==0)break;
			}
			if(j==l)res++;
		}
		printf("Case #%d: %d\n",tc++,res);
	}
	return 0;
}