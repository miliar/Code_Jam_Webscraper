#include <iostream>
#include <cmath>
using namespace std;
int main(){
	int t,i,j,x[10],y[10],r[10],n;
	double tot,d1,d2,d3;
	cin >> t;
	for(int q=1;q<=t;q++){
		cin >> n;
		for(i=0;i<n;i++){
			cin >>x[i]>>y[i]>>r[i];
		}
		if(n==1){
			tot=r[0]*1.0;
		}else if(n==2){
			tot=r[0]*1.0;
			if(r[1]>r[0]) tot=r[1]*1.0;
		}else{
			d1 = r[0]+r[1]+sqrt((y[1]-y[0])*(y[1]-y[0])*1.0+1.0*(x[1]-x[0])*(x[1]-x[0]));
			d2 = r[1]+r[2]+sqrt((y[1]-y[2])*(y[1]-y[2])*1.0+1.0*(x[1]-x[2])*(x[1]-x[2]));
			d3 = r[2]+r[0]+sqrt((y[2]-y[0])*(y[2]-y[0])*1.0+1.0*(x[2]-x[0])*(x[2]-x[0]));
			if(d1<=d2 && d1<=d3){
				tot = d1/2;
				if(tot<r[2])tot=r[2]*1.0;
			}else if(d2<=d1 && d2<=d3){
				tot = d2/2;
				if(tot<r[1])tot=r[1]*1.0;
			}else{
				tot = d3/2;
				if(tot<r[0])tot=r[0]*1.0;
			}
		}
		cout.precision(10);
		cout<<"Case #"<<q<<": "<<tot<<endl;
	}
}
