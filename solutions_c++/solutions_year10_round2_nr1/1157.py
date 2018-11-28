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
	fstream f;//输入
	fstream f1;//输出
	f.open("in.txt");
	f1.open("out.txt");
	int T;
	f>>T;
	int t=1;
	/*f.close();
	string tmp;
	f.open("B-small-attempt3.in");getline(f,tmp);*/
	int N,M;		  
	while(t<=T)
	{
	f>>N>>M;
	set<string> dic;
	for(int i=0;i<N;i++)
	{
		string tmp;
		f>>tmp;
		int j;
		for(j=0;j<tmp.size()-1;j++)
		{
			tmp[j]=tmp[j+1];
			if(tmp[j]=='/')tmp[j]=' ';
		}	
		tmp.resize(tmp.size()-1);
		stringstream ss;ss<<tmp;
		string tmp_out;
        string quan;
		while(ss>>tmp_out)
		{
			quan+="/";
			quan+=tmp_out;
			tmp_out="";tmp_out.clear();		dic.insert(quan);
		}

	}
	int ret=dic.size();
	for(int i=0;i<M;i++)
	{
        string tmp;
		f>>tmp;
		int j;
		for(j=0;j<tmp.size()-1;j++)
		{
			tmp[j]=tmp[j+1];
			if(tmp[j]=='/')tmp[j]=' ';
		}	
		tmp.resize(tmp.size()-1);
		stringstream ss;ss<<tmp;
		string tmp_out;
        string quan;
		while(ss>>tmp_out)
		{
			quan+="/";
			quan+=tmp_out;
			tmp_out="";tmp_out.clear();
dic.insert(quan);
		}
		
	}
	
	f1<<"Case #"<<t<<": "<<dic.size()-ret<<endl;
	t++;
	}
	f.close();
	f1.close();
}