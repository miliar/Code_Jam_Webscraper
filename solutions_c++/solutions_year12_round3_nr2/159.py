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
	ifstream ifs("data.txt");ofstream ofs("output2.txt");
	ll cases; ifs>>cases;
	for(ll cas=0;cas<cases;++cas){
		ofs<<"Case #"<<cas+1<<":"<<endl;
		cout<<"Case #"<<cas+1<<":"<<endl;
		double D; int N,A;
		string tmp=""; 
		getline(ifs,tmp);
		getline(ifs,tmp);//cout<<tmp<<endl;
		sscanf(tmp.c_str(),"%lf %d %d",&D,&N,&A);//cout<<D<<" ;"<<N<<" "<<A<<endl;
		double t[2],x[2];
		for(int i=0;i<N;++i){
				tmp="";
				getline(ifs,tmp);//cout<<tmp<<endl;
				//if(N==1)cout<<D<<" ; "<<tmp<<endl;
				sscanf(tmp.c_str(),"%lf %lf",&t[i],&x[i]);
				//cout<<t[i]<<" "<<x[i]<<endl;
		}
		double a[10];
		for(int i=0;i<A;++i){
			tmp="";ifs>>tmp;sscanf(tmp.c_str(),"%lf",&a[i]);
			//cout<<a[i]<<endl;
		}
		//cout<<endl;
		double result;
		for(int i=0;i<A;++i){
			double tm=sqrt(((double)2.0*(double)D/(a[i])));
			if(N==1||x[0]+((x[1]-x[0])/(t[1]-t[0]))*tm>D){
				result=tm;
			}else{
				result=(D-x[0])*( (t[1]-t[0])/(x[1]-x[0]));
			}
			ofs.precision(7);ofs.fixed;
				ofs<<result<<endl;
		}


		//ofs<<result<<endl;	
		
	}
	
	return 0;
}



