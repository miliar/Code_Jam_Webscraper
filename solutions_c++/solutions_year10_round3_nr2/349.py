#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include<math.h>
using namespace std;


int main()
{
	unsigned long T,L,P,C,N;
	int i,j,k,l,count,zz;
	cin>>T;
	double temp;
	double result,dif;
	
	for(i=0;i<T;i++)
	{
		cin>>L>>P>>C;
		temp=L;count=0;
		while(temp<P)
		{
			temp*=C;
			count++;
		}
		if(count>1)
			result=log2 (count);
		else 
			result=0;
		zz=(int)result;
		dif=result-zz;
		if(dif>0)
			zz++;
			
		cout<<"Case #"<<i+1<<": "<<zz<<endl;
	}
}
