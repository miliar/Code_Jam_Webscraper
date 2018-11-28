#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;

long long x[101];
long long y[101];

int main(){
	int t;
	int n,A,B,C,D,x0,y0,M;
	int ret;
	long long tx,ty;
	cin>>t;
	for(int tc=1;tc<=t;tc++){
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		ret=0;
		x[0]=x0;y[0]=y0;
		for(int i=1;i<n;i++){
			x[i]= (A*x[i-1]+B)%M;
			y[i]= (C*y[i-1]+D)%M;
		}
		//cout<<"here "<<endl;
		for(int i=0;i<n;i++)
		for(int j=i+1;j<n;j++)
		for(int k=j+1;k<n;k++){
			tx=x[i]+x[j]+x[k];
			ty=y[i]+y[j]+y[k];
			if(tx%3==0 && ty%3==0) 
				ret++;
		}
		//cout<<"here1 "<<endl;
		//printf("Case #%d: %d\n",tc,res);
		cout<<"Case #"<<tc<<": "<<ret<<endl;
	}
	return 0;
}
