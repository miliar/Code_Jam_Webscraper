
//Problem B. Space Emergency

#include <iostream>
#include <cmath>

#pragma warning(disable: 4800)
#include "mpirxx.h" //http://www.mpir.org/
#pragma warning(default: 4800)

using namespace std;

#define mytype mpz_class

int l,n,c;
mytype ti;
int d[1000];

int lpos[2];

mytype simulate(){
	int i,j;
	mytype total=0;
	mytype tmp;
	for (i=0;i<n;i++){
		if (lpos[0]==i || lpos[1]==i){
			if (total>=ti){
				total+=d[i%c];
			}else if (total+d[i%c]*2<=ti){
				total+=d[i%c]*2;
			}else { //acc in middle
				tmp=(ti-total);
				total+=tmp/2+d[i%c];
			}
		}else {
			total+=d[i%c]*2;
		}
		//cout<<"total: "<<i<<":"<<total<<endl;
	}
	return total;
}

mytype compute(){
	int i,j,k;
	lpos[0]=-1;
	lpos[1]=-1;
	mytype min=simulate();
	//cout<<"first min "<<min<<endl;
	mytype tmp;

	if (l>=1)
	for (i=0;i<n;i++){
		lpos[0]=i;
		if (l==1){
			tmp=simulate();
			if (tmp<min) min=tmp;
		} else {
			for (j=0;j<n;j++){
				if (i==j) continue;
				lpos[1]=j;
				tmp=simulate();
				//cout<<" i,j "<<i<<" "<<j<<" "<<tmp<<endl;
				if (tmp<min) min=tmp;
			}
		}
	}
	
	return min;
}

int main(){
	int t;
	int i,j,k;
	int result;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>l>>ti>>n>>c;
		for (j=0;j<c;j++){
			cin>>d[j];
		}
		cout<<"Case #"<<(i+1)<<": "<<compute()<<endl;
	}
}
