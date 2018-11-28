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
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t=0;
	cin>>t;
	int T=1;
	while(t--)
	{
		int key=0;
		cin>>key;
		
		vector<int> b(1,1);
		vector<int> o(1,1);
		int tmp=0;
		int ret=0;
		int prev_time_B=0,prev_time_O=0;
		while(key--)
		{
			string str="";
			cin>>str>>tmp;
			if(str=="O")
			{
				if(abs(tmp-o[o.size()-1])-prev_time_O>=0)
				{
					prev_time_B+=abs(tmp-o[o.size()-1])+1-prev_time_O;
					ret+=abs(tmp-o[o.size()-1])+1-prev_time_O;
					prev_time_O=0;
				}
				else
				{
					ret++;
					prev_time_O=0;
					//prev_time_O=max(0,prev_time_O);
					prev_time_B=1;
				}
				o.push_back(tmp);
			}
			else 
			{
				if(abs(tmp-b[b.size()-1])-prev_time_B>=0)
				{
					prev_time_O+=abs(tmp-b[b.size()-1])+1-prev_time_B;
					ret+=abs(tmp-b[b.size()-1])+1-prev_time_B;
					prev_time_B=0;
				}
				else
				{
					ret++;
					prev_time_B=0;
					//prev_time_B=max(0,prev_time_B);
					prev_time_O=1;
				}
				b.push_back(tmp);
			}
		}
		cout<<"Case #"<<T<<": "<<ret<<endl;
		T++;
	}

}