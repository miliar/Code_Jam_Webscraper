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

#define M 10009
#define inf 1000000000
//typedef long long LL;
//typedef __int64 LL;

int fact[15],val[30];
int freq[105][30];
vector<string> all;
char line[100];
vi valid[15];

int eval()
{	
	int ret=0,i,j;

	for(i=0;i<all.size();i++)
	{
		int v=1;

		for(j=0;j<all[i].size();j++)
		{
			int d=all[i][j]-'a';
			v=(v*val[d])%M;
		}
		//printf("*%d\n",v);
		ret=(ret+v)%M;
	}
	return ret;
}

int arr[10],ans,n;

void solve(int pos,int k,int x,int f)
{
	int i,j;

	if(k==0)
	{
		int v=fact[x]/f;
		v=(v*eval())%M;
		ans+=v;
		ans%=M;
		return ;
	}

	if(pos==n) return ;

	for(i=1;i<=k;i++)
	{
		for(j=0;j<26;j++)
			val[j]+=freq[pos][j]*i;

	//	arr[x]=pos;
		solve(pos+1,k-i,x+i,f*fact[i]);

		for(j=0;j<26;j++)
			val[j]-=freq[pos][j]*i;
	}

	solve(pos+1,k,x,f);
}


int main()
{
	freopen("B-small-attempt1.in","r",stdin); freopen("B-small-attempt1.out","w",stdout);
	int i,j,k,tests,cs=0,K;
	
	
	scanf("%d",&tests);

	fact[0]=1;
	for(i=1;i<=15;i++)
		fact[i]=(fact[i-1]*i)%M;

/*	for(i=1;i<(1<<20);i++)
	{
		int cnt=0;

		for(j=0;j<20;j++)
			if(i&(1<<j)) cnt++;

		if(cnt>5) continue;

		valid[cnt].push_back(i);

	}*/


	while(tests--)
	{
		scanf("%s%d%d",line,&K,&n);

		int len=strlen(line);

		all.clear();

		for(i=0;i<len;i=j+1)
		{
			string now;
			for(j=i;;j++)
				if(line[j]=='+' || line[j]=='\0') 
					break;
				else
					now+=line[j];

			all.push_back(now);
		}

//		for(i=0;i<all.size();i++)
//			printf("%s\n",all[i].c_str());

		MEM(freq,0);

		for(i=0;i<n;i++)
		{
			scanf("%s",line);

			for(j=0;line[j];j++)
				freq[i][line[j]-'a']++;
		}

		printf("Case #%d:",++cs);
		for(i=1;i<=K;i++)
		{
			MEM(val,0);
			ans=0;
			solve(0,i,0,1);
			printf(" %d",ans);
		}

		printf("\n");
	

	}

	return 0;
}