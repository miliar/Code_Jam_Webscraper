#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef long long int64;

#define MAX_CANDY 1000

int main() {
	int T,N,cases,sean,pat,real,real_max,curr;
	int candy[MAX_CANDY];
	cin>>T;
	for(int t=1;t<=T;t++){
		cin>>N;
		for(int n=0;n<N;n++){
			cin>>candy[n];
		}
		cases=pow(2,N)-2;
		real_max=0;
		for(int i=1; i<=cases; i++){
			real=0;
			sean=0;
			pat=0;
			for(int j=1; j<=N; j++){
				curr=1<<(j-1);
				if((i&curr)==curr){
					sean^=candy[j-1];
					real+=candy[j-1];
				}
				else{
					pat^=candy[j-1];
				}				
			}
			if((pat==sean)&&(real>real_max))
				real_max=real;
		}
		if(real_max>0)
			cout<<"Case #"<<t<<": "<<real_max<<endl;
		else
			cout<<"Case #"<<t<<": "<<"NO"<<endl;
	}
	return 0;
}
