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
long long gcd(long long a,long long b){if(a<b)swap(a,b);if(a%b==0)return b;return gcd(a%b,b);};//���Լ��
long long gbs(long long a,long long b){return a*b/gcd(a,b);}//��С������
template<class Ty,class Tx>vector<Ty> to(vector<Tx> x){vector<Ty>r;for(int i=0;i<x.size();i++)r.push_back(to<Ty>(x[i]));return r;}

long long digui(long long l,long long p,long long c)
{
	long long ll=l,pp=p;
	if(ll*c>=pp)return 0;
	while(ll<pp)
	{
		long long ppp=pp;
		ll*=c;pp/=c;
		if(pp*c<ppp)pp++;
	}
	return 1+digui(pp,p,c);
}
void main()
{
	fstream f;//����
	fstream f1;//���
	f.open("in.txt");
	f1.open("out.txt");
	int T;
	f>>T;
	int t=1;
	/*f.close();
	string tmp;
	f.open("B-small-attempt3.in");getline(f,tmp);*/
	int N;		  
	while(t<=T)
	{
		long long p,l,c;
	    f>>l>>p>>c;	
	    f1<<"Case #"<<t<<": "<<digui(l,p,c)<<endl;
	    t++;
	}
	f.close();
	f1.close();
}