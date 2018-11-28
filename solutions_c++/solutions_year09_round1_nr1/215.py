#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
//typedef long long LL;
//typedef __int64 LL;

string conv(int n,int base)
{
	string ret;
	while(n)
	{
		ret+=n%base+'0';
		n/=base;
	}
	return ret;
}

int flag[100006];

int ishappy(int n,int base,int iter)
{
	int k=n,i;
	while(1)
	{
		string now=conv(k,base);
		int sum=0;

		if(now.size()<2)
			if(now[0]=='1')
					return 1;
		
		for(i=0;i<now.size();i++)
			sum+=(now[i]-'0')*(now[i]-'0');
		k=sum;
		if(flag[k]==iter)
			return 0;
		flag[k]=iter;
	}
	return 0;
}
char line[1000];


int main()
{
	int i,j,k,tests,cs=0,iter=0;
	
	//freopen("D:\\gcj\\Asmall.in","r",stdin);
	freopen("D:\\gcj\\Asmall.out","w",stdout);

//	while(cin>>j>>k)
	//	printf("%d\n",ishappy(j,k,++iter));

	scanf("%d%*c",&tests);
	while(tests--)
	{
		gets(line);
		vi all;

		istr(line);

		while(sin>>k)
			all.push_back(k);

		int n=all.size(),a,b;
		for(i=2;;i++)
		{
			for(j=0;j<n;j++)
				if(ishappy(i,all[j],++iter)==0)
					break;
			if(j==n)
				break;
		}	

		printf("Case #%d: %d\n",++cs,i);
	}

	return 0;
} 


