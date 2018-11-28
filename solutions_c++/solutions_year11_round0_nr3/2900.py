#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	int N;
	unsigned int min,total,num,xorsum;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>N;
		cin>>num;
		min=total=xorsum=num;
		for(int j=1;j<N;j++){
			cin>>num;
			if(min>num) min=num;
			total+=num;
			xorsum^=num;
		}
		if(xorsum)
			cout<<"Case #"<<i<<": NO"<<endl;
		else
			cout<<"Case #"<<i<<": "<<total-min<<endl;
	}
	return 0;
}