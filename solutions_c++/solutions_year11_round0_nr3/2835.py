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
};*/


int main()
{
    freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int t=0;
	cin>>t;
	int T=1;
	while(t--)
	{
		vector<int> wei(20,0);
		int n;
		cin>>n; long long tmp=0;long long m=10000000;
		long long sum=0;
		while(n--)
		{
			cin>>tmp;
			m=min(m,tmp);sum+=tmp;
			int w=0;
            do
			{
				if(tmp%2==1)wei[w]++;
				w++;
			}while(tmp/=2);
		}
		bool shit=false;
		for(int i=0;i<wei.size();i++)
		{
			if(wei[i]%2==1)
			{cout<<"Case #"<<T<<": NO"<<endl;shit=true;break;}
		}
		if(shit==false)
		cout<<"Case #"<<T<<": "<<sum-m<<endl;
		T++;
	}

}