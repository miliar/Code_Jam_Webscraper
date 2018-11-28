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
	long long k=0;		  
	while(t<=T)
	{
	int K,N;//k*k
	f>>K>>N;
	deque<deque<char>> in(K,deque<char>(0));
	vector<string> rotate(K,string(K,' '));

	for(int i=0;i<K;i++)
	{
	string tmp;
	f>>tmp;
    for(int j=0;j<K;j++)
	{
		if(tmp[j]!='.')in[i].push_back(tmp[j]);
	}
	while(in[i].size()<K){in[i].push_front('.');}
	}
	for(int i=0;i<K;i++)
		for(int j=0;j<K;j++)
		{
			rotate[j][K-i-1]=in[i][j];
		}
    bool ret_red=false,ret_blue=false;
	bool red=false,blue=false;
	for(int i=0;i<K;i++)//hang
	{
		int r=0,b=0;
		for(int j=0;j<K;j++)
		{
			if(r==N)red=true;
			if(b==N)blue=true;
			if(rotate[i][j]=='R'){r++;b=0;}
			else if(rotate[i][j]=='B'){b++;r=0;}
			else {b=0;r=0;}
		}
		if(r==N)red=true;
		if(b==N)blue=true;
	}
	if(red)ret_red=red;if(blue)ret_blue=blue;
	red=false,blue=false;
	for(int i=0;i<K;i++)//lie
	{
		int r=0,b=0;
		for(int j=0;j<K;j++)
		{
			if(r==N)red=true;
			if(b==N)blue=true;
			if(rotate[j][i]=='R'){r++;b=0;}
			else if(rotate[j][i]=='B'){b++;r=0;}
			else {b=0;r=0;}
		}
		if(r==N)red=true;
		if(b==N)blue=true;
	}
	if(red)ret_red=red;if(blue)ret_blue=blue;
	red=false,blue=false;
	bool red1=false,blue1=false;
	for(int i=0;i<K;i++)//  
	{
		int r=0,b=0,dxie=0;// '\'下半部分
		int r1=0,b1=0,d1=0;//shangbangbufen
        while(i+dxie<K)
		{
			if(r==N)red=true;if(r1==N)red1=true;
			if(b==N)blue=true;if(b1==N)blue1=true;
			if(rotate[i+dxie][dxie]=='R'){r++;b=0;}
			else if(rotate[i+dxie][dxie]=='B'){b++;r=0;}
			else {b=0;r=0;}
			if(rotate[dxie][i+dxie]=='R'){r1++;b1=0;}
			else if(rotate[dxie][i+dxie]=='B'){b1++;r1=0;}
			else {b1=0;r1=0;}
			dxie++;
		}
			if(r==N)red=true;if(r1==N)red1=true;
			if(b==N)blue=true;if(b1==N)blue1=true;
	}
	if(red||red1)ret_red=1;if(blue||blue1)ret_blue=1;
	red=0;blue=0;red1=0;blue1=0;
	for(int i=0;i<K;i++)//  
	{
		int r=0,b=0,dxie=0;// '/'下半部分
		int r1=0,b1=0,d1=0;//shangbangbufen
        while(i-dxie>0)
		{
			if(r==N)red=true;
			if(b==N)blue=true;
			if(rotate[i-dxie][dxie]=='R'){r++;b=0;}
			else if(rotate[i-dxie][dxie]=='B'){b++;r=0;}
			else {b=0;r=0;}

			dxie++;
		}
			if(r==N)red=true;
			if(b==N)blue=true;
		while(d1+i<K)
		{if(r1==N)red1=true;if(b1==N)blue1=true;if(r1>N)red1=false;if(b1>N)blue1=false;
			if(rotate[K-1-d1][d1+i]=='R'){r1++;b1=0;}
			else if(rotate[K-1-d1][i+d1]=='B'){b1++;r1=0;}
			else {b1=0;r1=0;}
			d1++;
		}
		if(r1==N)red1=true;if(b1==N)blue1=true;if(r1>N)red1=false;if(b1>N)blue1=false;
	}
	if(red||red1)ret_red=1;if(blue||blue1)ret_blue=1;
	if(ret_red&&ret_blue)
	{
	f1<<"Case #"<<t<<": "<<"Both"<<endl;
	}
	else if(ret_red&&!ret_blue)
	{
    f1<<"Case #"<<t<<": "<<"Red"<<endl;
	}
	else if(!ret_red&&ret_blue)
	{
    f1<<"Case #"<<t<<": "<<"Blue"<<endl;
	}
	else
    f1<<"Case #"<<t<<": "<<"Neither"<<endl;
	t++;
	}
	f.close();
	f1.close();
}