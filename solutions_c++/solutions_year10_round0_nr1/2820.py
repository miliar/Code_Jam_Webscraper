#include<iostream>
#include<cmath>
#include<stdio.h>
using namespace std;

int main()
{
	freopen("A-large(2).in","r",stdin);
	freopen("output.txt","w",stdout);
 	char res[5][5]={"ON","OFF"};
	int in;
	int n=0;
        unsigned long int k=0;	
	cin>>in;
	
	for(int i=0;i<in;i++){
		cin>>n>>k;
		k=(k+1)%(unsigned long int)(pow(2,n));
		if(k)	k=1;
		cout<<"Case #"<<i+1<<": "<<res[k]<<endl;
	}
	return 0;
}
