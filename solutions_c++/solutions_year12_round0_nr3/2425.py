
//Problem C. 

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <cmath>

using namespace std;

int n;
int a,b;
int res;

void compute(){
	int i,j,k;
	int digit=1;
	int mul=1;
	res=0;
	k=a;
	while (k/10>0) {
		k/=10;
		digit++;
		mul*=10;
	}
	for (i=a;i<b;i++){
		k=i;
		for (j=1;j<digit;j++){
			k=k/10+(k%10)*mul;
			if (k==i) break; //e.g. 1212
			if (k>i && k<=b) {
				res++;
				//printf("%d\t%d\t%d\n",i,k,j);
			}
		}
	}
}

int main(){
	int t;
	int i,j,k;

	cin>>t;
	for (i=0;i<t;i++){
		cin>>a>>b;
	
		compute();
		cout<<"Case #"<<(i+1)<<": "<<res<<endl;
	}
}
