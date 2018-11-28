#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int main()
{
	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\C-small-attempt0.in","r",stdin);
	freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\gcj\\C-small-attempt0.out","w",stdout);
	int r,k,n,g[1000];
	int gain[1000];
	int next[1000];
	int sum[2000];
	int flag[1000];
	int tgain[1000];
	int cas;
	cin>>cas;
	for(int cs=1;cs<=cas;cs++)
	{
		cin>>r>>k>>n;
		for(int i=0;i<n;i++)
			cin>>g[i];
		for(int i=0;i<2*n;i++)
		{
			if(i==0) sum[i]=g[0];
			else sum[i]=sum[i-1]+g[i%n];
		}
		for(int i=0;i<n;i++)
		{
			int maxx=(i==0?0:sum[i-1])+k;
			int j=upper_bound(sum+i,sum+2*n,maxx)-sum;
			if(j-i>=n)
				j=i+n;
			next[i]=j%n;
			gain[i]=sum[j-1]-(i==0?0:sum[i-1]);
			flag[i]=-1;
		}
		int s=0;
		int step=0;
		int cgain=0;
		while(flag[s]==-1)
		{
			flag[s]=step++;
			tgain[s]=cgain;
			cgain+=gain[s];
			s=next[s];
		}
		int circlelen=step-flag[s];
		int circlegain=cgain-tgain[s];
		int prelen=flag[s];
		cout<<"Case #"<<cs<<": "; 
		if(r<prelen)
		{
			int p=0;
			for(int i=0;i<r;i++)
				p=next[p];
			cout<<tgain[p]<<"\n";
			
		}
		else
		{
			r-=prelen;
			int times=r/circlelen;
			int p=s;
			for(int i=0;i<r%circlelen;i++)
				p=next[p];
			cout<<tgain[p]+times*circlegain<<"\n";
		}
	}
}