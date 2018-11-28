#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main(void){
	int t;
	cin>>t;
	for(int set=1;set<=t;set++){
		int n,k;
		cin>>n>>k;
		int p=(int)pow(2,n)-1, a=p&k;
		printf("Case #%d: %s\n",set,a==p?"ON":"OFF");
	}

	return 0;
}
