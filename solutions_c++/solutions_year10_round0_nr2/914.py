#include<stdio.h>
#include<iostream>
#include<stdlib.h>
using namespace std;
long long int gcd(long long int a,long long int b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}
main()
{
	int T,N,i,j;
	cin >> T;
	for(i=0;i<T;i++)
	{
		long long int *t,D1,D,k;
		cin >> N;
		t=(long long int *)malloc(sizeof(long long int)*N);
		cin >> t[0];
		cin >> t[1];D=t[1]-t[0];
	//	cout <<"DIFF "<< D <<"  "<< D1<< endl;
		if(D<0)
		D=t[0]-t[1];
		for(j=2;j<N;j++)
		{
			cin >> t[j];
			D1=t[j]-t[j-1];
			if(D1<0)
			D1=t[j-1]-t[j];
//			cout << D << " "<< D1 << endl;
			D=gcd(D,D1);
		}
		//cout << D << endl;
		k=t[0]%D;
		if(k)
		k=D-k;
		cout << "Case #" << i+1<<": "<< k << endl;
	}
}
