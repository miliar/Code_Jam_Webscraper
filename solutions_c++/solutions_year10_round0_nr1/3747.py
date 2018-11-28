#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
 using namespace std;
 
 #define FOR(i,a,b) for(int i=a;i<b;++i)
 #define INF int(1e9);
 
 typedef long long LL;
 int N,K;
 bool wire,state;
 int power(int a,int b)
 {
		if(b==0)
			return 1;
		if(b==1)
			return a;
		if(b%2==0)
			return power(a,b/2)*power(a,b/2);
		else
			return a*power(a,(b-1)/2)*power(a,(b-1)/2);	 
}			
int main()
{
		ifstream fin("A.in");
		ofstream fout("OUT.in");
		int t,total;
		fin>>t;
		total=t;
		while(t--)
		{
			wire=false,state=false;
			fin>>N>>K;
			LL low=power(2,N-1);
			LL high=power(2,N);
			if(K>=high)
				K=K%high;		
			if(K>=low)
					state=true;		
			else
					state=false;
			if(K % low==low-1)
				wire=true;
			else
				wire=false;
			if(wire==true and state==true)
				fout<<"Case #"<<total-t<<": "<<"ON"<<endl;
			else
				fout<<"Case #"<<total-t<<": "<<"OFF"<<endl;
		}
		return 0;
}									
