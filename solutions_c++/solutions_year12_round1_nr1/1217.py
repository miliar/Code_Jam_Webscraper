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
	for(ll c=0;c<cases;++c){
		ofs<<"Case #"<<c+1<<": ";
		//cout<<"Case #"<<c+1<<": "<<endl;
		double result=0;
		ll A,B;
		ifs>>A>>B;
		vector <double> p;
		//{string tmp;getline(ifs,tmp);};
		for(ll i=0; i< A; ++i){
			double tmp;string str;
			ifs>>str;
			sscanf(str.c_str(),"%lf",&tmp);
			p.push_back(tmp);//cout<<p[i]<<endl;
		}

		double p_all_1=1;
		for(ll i=0;i<A;++i){
			//‘S³‰ð
			p_all_1*=p[i];
		}
		double c1;
		c1=p_all_1*(B-A+1)+(1-p_all_1)*(2*B-A+2);

		double c3;
		c3=B+2;

		double c2=10000000000;
		for(ll i=0;i<A;++i){
			double del_remain_correct=1;
			for(ll j=0; j<A-i;++j){
				del_remain_correct*=p[j];
			}
			c2=min(c2,del_remain_correct*(B-A+1+2*i)+(1-del_remain_correct)*(2*i+B-A+1+B+1));
			
		}
		result =min(c1,min(c2,c3));
	//	cout.setf(ios::fixed);cout.precision(6);
	//	cout<<result<<endl;
		ofs.setf(ios::fixed);ofs.precision(6);
		ofs<<result<<endl;		
	}
	
	return 0;
}



