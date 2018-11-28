#include<iostream>
#include<string>
#include<vector>
#include<string.h>
#include<cmath>
#include<stdlib.h>
using namespace std;
int pushback(int b,int size)
{
	int power = (int)pow(10,size-1);
	int first = b/power;
	return( (b - first*power)*10+first);
}
		
bool isPair(int a, int b, int size)
{
	int temp = b;
	for(int i=0; i<size ;i++)
	{	
		if(temp==a)
		{
			return true;
		}
		
		temp = pushback(temp,size);
	}
}
int main(void)
{
	int numofcase;
	cin>>numofcase;
	string temp;
	for(int i=0; i<numofcase ; i++)
	{
		int A,B,result=0,size;
		string tempA,tempB;
		cin>>tempA>>tempB;
		size = tempA.length();
		A=atoi(tempA.c_str());
		B=atoi(tempB.c_str());
		for(int j=A; j<=B; j++)
		{
			for(int k=j+1; k<=B; k++)
			{
				if(isPair(j,k,size))
				{
					result++;
				}
			}
		}
		
		cout<<"Case #"<<(i+1)<<": "<<result<<endl;
	}
return 0;
}	















