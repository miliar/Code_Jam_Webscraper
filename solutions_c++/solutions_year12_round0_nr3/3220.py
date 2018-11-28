#include<iostream>
#include<stdio.h>
#include<vector>
#include<cmath>
using namespace std;
int getNumDigit(long int number)
{
	return floor( log10( abs( number ) ) ) + 1;
}
long int shiftRight(long int number,int digit)
{
	int rmb = number%10;
	number = number/10;
	number = number+rmb*pow(10,digit-1);
	return number;
}
bool isRecycle(long int num1,long int num2)
{
	int digit = getNumDigit(num1);
	if(digit!=getNumDigit(num2))
		return false;
	//if(digit==1)
	//	return false;

	for(int i=0;i<digit;i++)
	{
		num1=shiftRight(num1,digit);
		if(num1==num2)
			return true;
	}
	return false;
}

int main(){
	int T;
	cin>>T;
	vector<int> results;
	results.resize(T);
	long int A,B;
	int cnt = 0;
	for(int i=0;i<T;i++)
	{
		cin>>A;
		cin>>B;
		cnt = 0;
		for(long int k=A;k<B;k++)	
			for(long int l=k+1;l<=B;l++)
				if(isRecycle(k,l))
					cnt++;	
		results[i]=cnt;
	}
	for(int i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": "<<results[i]<<endl;
	}	

	return 0;
}
