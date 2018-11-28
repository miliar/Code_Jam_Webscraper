// A.cpp : Defines the entry point for the console application.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;
#define ll long long


ll gcd(ll m, ll n)
{
    ll r;
    if (m < n) {swap(m, n);}
    if (n == 0) {return m;}
    if ((r = m % n)) {return gcd(n, r);}
    return n;
}

ll lcm(ll m, ll n)
{
    return (m * n) / gcd(m, n);
}



int main()
{
	ifstream ifs("data.txt");ofstream ofs("output.txt");
	ll cases; ifs>>cases;
	for(ll cas=0;cas<cases;++cas){
		ofs<<"Case #"<<cas+1<<":";
		cout<<"Case #"<<cas+1<<": ";
		double result=0;

		ll N;
		ifs>>N;vector <double> s;double X=0;
		for(ll i=0;i<N;++i){
			double tmp; ifs>>tmp; s.push_back(tmp);
			X+=tmp;
		}

		for(ll i=0;i<N;++i){

			double l=0,r=1;
			while(l+0.000000001<r){
				double cur=(l+r)/(double)2.0;//ofs<<cur<<endl;
				double point=(double)s[i]+(double)X*cur;
				bool ok=false;
				double remain=0;
				
				for(int j=0;j<N;++j){
					if(j!=i){
						double a=(point>s[j])?point-s[j]:0;
						remain+=a;
						if(remain>=X*(1.0-cur)){
							ok=true;
							break;
						}
					}
				}

				if(ok){
					r=cur;
				}else{
					l=cur;
				}
			}//while
			//cout.setf(ios::fixed);
			//cout.precision(6);
		//	cout<<(double)100*(l+r)/(double)2<<" "<<endl;
			printf("%lf ",100.0*(l+r)/2.0);
			ofs.setf(ios::fixed);
			ofs.precision(6);
			//ofs<<(double)100*(l+r)/(double)2.0<<" ";
			double tmp=(double)100.0*l;
			ofs<<" "<<tmp;
		}
		cout<<endl;
		//ofs<<result<<endl;		
		ofs<<endl;
	}
	
	return 0;
}



