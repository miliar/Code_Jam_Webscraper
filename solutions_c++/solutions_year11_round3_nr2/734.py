/*
ID: tonyliu5
LANG: C++
TASK: gcj
*/

#include<stack>
#include<list>
#include<iostream>
#include<iomanip>
#include<fstream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<deque>
#include<queue>
#include<string>
#include<sstream>
#include<ctime>
#include<set>
#include<map>
#include<numeric>
#include<queue>
#include<cstring>
#include<stdio.h>
using namespace std;
template<class Ty,class Tx>Ty to (Tx x){Ty y;stringstream ss("");ss<<x;ss.seekg(0);ss>>y;return y;};
long long gcd(long long a,long long b){if(a<b)swap(a,b);if(a%b==0)return b;return gcd(a%b,b);};//最大公约数,0的要考虑情况，负数情况等特殊情况
long long gbs(long long a,long long b){return a*b/gcd(a,b);}//最小公倍数
template<class Ty,class Tx>vector<Ty> to(vector<Tx> x){vector<Ty>r;for(int i=0;i<x.size();i++)r.push_back(to<Ty>(x[i]));return r;}
/*
struct Node
{
	int from,to,v;
};
struct cmp
{
	bool operator ()(Node& a,Node& b)
	{
		return a.v>b.v;
	}
};
		闰年条件if(((1900+i)%4==0&&(1900+i)%100!=0)||((1900+i)%400==0&&(1900+i)%100==0))days[2]=29;
		不是闰年else days[2]=28;
*/


int main()
{
    freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	//return 0;
	/* google part! */
	int t=0;
	cin>>t;
	int T=1;
	while(t--)
	{
		long long L,t,N,C;
		cin>>L>>t>>N>>C;
		vector<long long> ll(L+1,0);
		vector<vector<long long> > dp(N+1,ll);
		vector<int> dis;
		while(C--)
		{
			int tmp;
			cin>>tmp;
			dis.push_back(tmp);
		}
		for(int i=1;i<=N;i++)
		{
			//如果决定修这个路i-1---i
			for(int j=0;j<L+1;j++)
			{
				long long ttt=dis[(i-1)%dis.size()];
				long long L1=dp[i-1][L]+dis[(i-1)%dis.size()]*2;
				if(j+1<=L)
				{
					L1=dp[i-1][j+1];
					if(t-dp[i-1][j+1]>0)
					{L1+=((t-dp[i-1][j+1])/2+dis[(i-1)%dis.size()]);}
					else
						L1+=dis[(i-1)%dis.size()];
				}
				dp[i][j]=min(L1,//修了
					         dp[i-1][j]+dis[(i-1)%dis.size()]*2);//没修
			}
		}
		long long ret=100000000;
		for(int i=0;i<dp[N].size();i++)
		{
			ret=min(ret,dp[N][i]);
		}
		cout<<"Case #"<<T<<": "<< ret<<endl;

		T++;
	}
   
	return 0;
}