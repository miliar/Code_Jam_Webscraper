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
	f.open("A-large.in");
	f1.open("out.txt");
	int T;
	f>>T;int t=1;
	vector<long long> a30(32,0);
    int N,K;
	/*f.close();
	f.open("in.txt");getline(f,tmp);*/	
    N=30;
	long long k=0;
	vector<bool> ON(N,0);
	vector<bool> power(N+1,0);
    for(double ii=0;ii<31;ii++)
	{
		a30[ii]=pow(2.0,ii)-1;
	}
	
	
    
	while(t<=T)
	{
    
	 
	f>>N>>K;
	string ret;
	if(K<a30[N])ret="OFF";
	else if(K==a30[N])ret="ON";
	else
	{
		if(K%(a30[N]+1)==a30[N])ret="ON";
		else ret="OFF";
	}
	if(N==1&&K==1)ret="ON";
    if(N==1&&K==0)ret="OFF";
	f1<<"Case #"<<t<<": "<<ret<<endl;
	t++;
	}
	f.close();
	f1.close();
}