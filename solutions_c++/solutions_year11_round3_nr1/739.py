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
    freopen("A-large(1).in","r",stdin);
	freopen("A-large.out","w",stdout);
	//return 0;
	/* google part! */
	int t=0;
	cin>>t;
	int T=1;
	while(t--)
	{
		bool ret=true;
		int R,C;
		cin>>R>>C;
		vector<string> m;
		while(R--)
		{
			string tmp;
			cin>>tmp;
			m.push_back(tmp);
		}
		for(int i=0;i<m.size();i++)
		{
			if(!ret)break;
			for(int j=0;j<m[0].size();j++)
			{
				if(m[i][j]=='#')
				{
					if(i+1<m.size()&&j+1<m[0].size())
					{
						if(m[i+1][j]=='#'&&m[i][j+1]=='#'&&m[i+1][j+1]=='#')
						{
							m[i][j]='/';
							m[i+1][j]='\\';
							m[i][j+1]='\\';
							m[i+1][j+1]='/';
						}
						else {ret=false;break;}
					}
					else {ret=false;break;}
				}
			}
		}
		cout<<"Case #"<<T<<":"<<endl;
		if(!ret)
		{
			cout<<"Impossible"<<endl;
		}
		else
		{
			for(int i=0;i<m.size();i++)
			{
				for(int j=0;j<m[0].size();j++)
				{
					cout<<m[i][j];
				}
				cout<<endl;
			}
		}
		T++;
	}
   
	return 0;
}