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
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//return 0;
	/* google part! */
	int t=0;
	cin>>t;
	int T=1;
	while(t--)
	{
		int N;
		cin>>N;
		vector<string> m;
		vector<double>wp(N);
		vector<double>owp1(N);
		vector<double>owp2(N);
		vector<double>oowp1(N);
		vector<double>owp(N);
		vector<int> bisaishu(N,0);
		vector<double>ret(N);
		while(N--)
		{
			string tmp;
			cin>>tmp;
			m.push_back(tmp);
		}
		for(int i=0;i<m.size();i++)
		{
			int win=0,lose=0;
			for(int j=0;j<m.size();j++)
			{
				if(m[i][j]=='1'){win++;bisaishu[i]++;}
				if(m[i][j]=='0'){lose++;bisaishu[i]++;}
			}
			wp[i]=(double)win/(double)(win+lose);
			owp1[i]=win;
			owp2[i]=lose;
		}
		
		for(int i=0;i<m.size();i++)
		{	
			double o=0;
			for(int j=0;j<m.size();j++)
			{
				
				if(i==j)continue;
				if(m[i][j]=='1'){o+=(owp1[j]/(owp1[j]+owp2[j]-1));}
				if(m[i][j]=='0'){o+=((owp1[j]-1)/(owp1[j]+owp2[j]-1));}
			}
			o=o/(double)bisaishu[i];
			owp[i]=o;
		}
		for(int i=0;i<ret.size();i++)
		{
			double oowp=0;
			for(int j=0;j<owp.size();j++)
			{
				if(m[i][j]!='.')
				oowp+=owp[j];
			}
			oowp=oowp/(double)bisaishu[i];
			ret[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp;
		}
		cout<<"Case #"<<T<<":"<<endl;
		for(int i=0;i<ret.size();i++)
		{
			cout<<ret[i]<<endl;
		}
		T++;
	}
   

}