#include <iostream>
#include <cmath>
using namespace std;
double dis(double a, double b){
	return sqrt(a*a+b*b);
}
double get(double a, double b, double c, double d, double e, double f){
	return (c+f+dis(a-d,b-e))/2;
}
int main(){
	int t;
	cin >> t;
	for(int kase=1; kase<=t; kase++){
		int n;
		cin >> n;
		double ans=0;
		if(n==1){
			double a,b,c;
			cin >> a >> b >> c;
			ans=c;
		}
		if(n==2){
			double a,b,c,d,e,f;
			cin >> a >> b >> c>>d>>e>>f;
			ans=max(c,f);

		}
		if(n==3){
			double a,b,c,d,e,f,g,h,i;
			cin >> a >> b >> c>>d>>e>>f>>g>>h>>i;
			double t1,t2,t3;
			t1=max(i,get(a,b,c,d,e,f));
			t2=max(c,get(g,h,i,d,e,f));
			t3=max(f,get(a,b,c,g,h,i));
			ans=min(t1,min(t2,t3));

		}
		cout<<"Case #"<<kase<<": "<<ans<<endl;
	}
}

#

