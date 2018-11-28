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

string s,w="welcome to code jam";

int dp[20][600];
int len;

int doit(int wi,int si)
{
	if(wi==19)return 1;
	if(si>=len)return 0;
	if(dp[wi][si]!=-1)return dp[wi][si];
	int i,j,k,res=0;
	for(i=si;i<len;i++)
	{
		if(s[i]==w[wi])
			res += (doit(wi+1,i+1))%10000;
	}
	return dp[wi][si]=res%10000;

}

int main()
{
	int t,tc=1,i;
	cin>>t;
	while((getchar())!='\n');
	char buf[1000];
	while(t--)
	{
		i=0;
		char ch;
		while((ch=getchar())!='\n')
			buf[i++]=ch;
		buf[i]='\0';
		s = buf;
		len = s.size();
		memset(dp,-1,sizeof(dp));
		int res = doit(0,0);
	
		printf("Case #%d: ",tc++,res);
		if(res<10)printf("000");
		else if(res<100)printf("00");
		else if(res<1000)printf("0");
		printf("%d\n",res);
	}
}