#include <stdio.h>
#include <iostream>
#include <iomanip>
using namespace std;

double p[100010];
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int N;
	cin>>N;
	for(int k=0;k<N;k++){
		int a,b;
		double pr=1;
		cin>>a>>b;
		for(int i=0;i<a;i++){
			cin>>p[i];
			p[i]*=pr;
			pr*=p[i];
		}
		double min = b+2<b-a+5?b+2:b-a+5;
		double temp=p[a-1]*(b-a+1)+(1-p[a-1])*(2*b-a+2);
		if (temp<min) min=temp;
		for(int i=1;i<a;i++){
			double r=(b-a+2*i+1)*p[a-i-1]+(2*b-a+2*i+2)*(1-p[a-i-1]);
			if (r<min) min=r;
		}
		cout<<"Case #"<<k+1<<": "<<setprecision(6)<<fixed<<min<<endl;
	}
	return 0;
}


