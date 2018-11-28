#include<list>
#include<iostream>
#include<fstream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<deque>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<stack>
#include<numeric>
using namespace std;
template<class Ty,class Tx>Ty to (Tx x){Ty y;stringstream ss("");ss<<x;ss.seekg(0);ss>>y;return y;};
long long gcd(long long a,long long b){if(a<b)swap(a,b);if(a%b==0)return b;return gcd(a%b,b);};//最大公约数
long long gbs(long long a,long long b){return a*b/gcd(a,b);}//最小公倍数
template<class Ty,class Tx>vector<Ty> to(vector<Tx> x){vector<Ty>r;for(int i=0;i<x.size();i++)r.push_back(to<Ty>(x[i]));return r;}


void main()
{
	fstream f;
	fstream f1;
	f.open("B-small-attempt3.in");
	f1.open("out.txt");
	int T;
	f>>T;int t=1;
	f.close();
	string tmp;
	f.open("B-small-attempt3.in");getline(f,tmp);
	long long k=0;		  
	while(t<=T)
	{
	tmp="";
	int siz=0;long long tmpnum;
	getline(f,tmp);
	stringstream ss("");
	ss<<tmp;ss>>siz;
	vector<long long> num(siz,0);
	for(int i=0;i<siz;i++)
	{
		ss>>tmpnum;
		num[i]=tmpnum;
	}
    long long gc=0;
	for(int i=0;i<siz;i++)
	{
		for(int j=i+1;j<siz;j++)
		{
			long long cha;
			if(num[i]>num[j])
			cha=num[i]-num[j];
			else if(num[i]<num[j])
            cha=num[j]-num[i];
			else continue;
			if(gc==0)gc=cha;
			else
				gc=gcd(cha,gc);
		}
	}
	long long gb=0;
    for(int i=0;i<siz;i++)
	{
		num[i]=gc-num[i]%gc;
		if(gb==0)gb=num[i];
		else
			gb=gbs(gb,num[i]);
	}
	if(gc==gb)gb=0;
	f1<<"Case #"<<t<<": "<<gb<<endl;
	t++;
	}
	f.close();
	f1.close();
}