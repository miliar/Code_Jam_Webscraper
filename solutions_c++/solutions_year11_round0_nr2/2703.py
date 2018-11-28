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
    freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt3.out","w",stdout);
	int t=0;
	cin>>t;
	int T=1;
	while(t--)
	{
		map<string,string> c;
		int C=0;
		cin>>C;string str,tmp,tmp_to;
		while(C--)
		{
			cin>>str;
			tmp.push_back(str[0]);tmp.push_back(str[1]);tmp_to.push_back(str[2]);
			c[tmp]=tmp_to;tmp.clear();
			tmp.push_back(str[1]);tmp.push_back(str[0]);
			c[tmp]=tmp_to;
		}
		int D=0;
		map<string,string> d;
		cin>>D;string str1,tmp1,tmp2;
		while(D--)
		{
			cin>>str1;
			tmp1.push_back(str1[0]);
			tmp2.push_back(str1[1]);
			d[tmp1]=tmp2;
			d[tmp2]=tmp1;
			//cout<<d[tmp1];
		}
		int N=0;cin>>N;
		//map<string,int> dic;//出现这个字符，对应从第几位到这位全部清空
		string ret;cin>>ret;
		for(int i=0;i<ret.size()-1;i++)
		{
			string temp;
			temp.push_back(ret[i]);temp.push_back(ret[i+1]);
			map<string,string>::iterator p;
			p=c.end();
			p=c.find(temp);
			if(p!=c.end()){ret[i]='.';ret[i+1]=c[temp][0];}
			else
			{
				string kao;kao.push_back(ret[i+1]);
				p=d.end();
				p=d.find(kao);
				if(p!=d.end())//是要替换的
				{
					for(int j=i;j>=0;j--)
					{
						if(ret[j]==d[kao][0])
						{
							for(int k=0;k<i+2;k++)//gai guo
							{
								ret[k]='.';
							}							
							break;
						}
					}
				}
			}
		}
		string result;
		for(int l=0;l<ret.size();l++)
	    {
			if(ret[l]!='.')result.push_back(ret[l]);
	    }
		if(result.size()==0)
		cout<<"Case #"<<T<<": []"<<endl;
		else if (result.size()==1)
		{cout<<"Case #"<<T<<": ["<<result[0]<<"]"<<endl;}
		else
		{
			cout<<"Case #"<<T<<": ["<<result[0];
			for(int i=1;i<result.size();i++)
			{
				cout<<", "<<result[i];
			}
			cout<<"]"<<endl;
		}

		T++;
	}

}