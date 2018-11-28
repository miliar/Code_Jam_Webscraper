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
	f.open("C-small-attempt1.in");
	f1.open("out.txt");
	int T;
	f>>T;int t=1;
	long long R,k;int N;
	//f.close();	
	/*string tmp;
	f.open("B-small-attempt3.in");getline(f,tmp);*/
	while(t<=T)
	{
        f>>R>>k>>N;
		deque<long long> a(N,0);
		
		int n=0;
		while(n<N)
		{
			f>>a[n];
			n++;
		}
		long long r=0;
		long long ret=0;
		long long k1=0;
		while(r<R)
		{
            deque<bool> b(N,0);
			while(k1<k&&b[0]!=1)
			{
				k1+=a[0];
				if(k1<=k){a.push_back(a[0]);a.pop_front();b.pop_front();b.push_back(1);}
				else if(k1>k){k1-=a[0];break;}
				else break;
			}
			ret+=k1;
			r++;k1=0;
		}
		f1<<"Case #"<<t<<": "<<ret<<endl;
		t++;
	}


	f.close();
	f1.close();
}