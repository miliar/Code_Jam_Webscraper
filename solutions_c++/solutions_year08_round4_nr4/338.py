#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;
ifstream fin("D-small-attempt0.in");
ofstream fout("p4.out");
#define INF 1000000
//#define fout cout

char s[51000], temp[51000];
int len;
int k;
int f[51000][26];
bool have[26];
int ans;
int p[10];

void init()
{
	fin>>k>>s;
	len=strlen(s);
}
int getAns()
{
	for (int i=0;i<len/k;i++)
	{
		int base=i*k;
		for (int j=0;j<k;j++)
			temp[base+j]=s[base+p[j]];
	}
	int ans=0;
	for (int i=0;i<len;i++)
		if (i==0 || temp[i]!=temp[i-1]) ans++;
	return ans;
}
void permute(int no)
{
	if (no==k)
	{
		ans=min(ans,getAns());
		return;
	}
	for (int i=0;i<k;i++)
		if (!have[i])
		{
			p[no]=i;
			have[i]=true;
			permute(no+1);
			have[i]=false;
		}
}
void calc()
{
	ans = INF;
	memset(have,false,sizeof(have));
	permute(0);
	fout<<ans<<endl;
}
int main()
{
	int t;
	fin>>t;
	for (int i=1;i<=t;i++)
	{
		init();
		fout<<"Case #"<<i<<": ";
		calc();
	}

}