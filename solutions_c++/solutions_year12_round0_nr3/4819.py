// next_permutation
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

long int countr=0;
vector<long int> myvector;
vector<long int>::iterator it;
long int start=1111;
long int stop =2222;

void permute(long int num)
{

	long int length = 0;
	long int temp = num;
	long int intArray[10];
	long int intResult[10];
	long int i=0;
	long int j=0;

	
	while(temp!=0)
	{

		intArray[length]=(int)temp%10;
		intResult[length]=(int)temp%10;
		temp=temp/10;
		++length;
	}
	//cout<<length<<endl;

	temp=0;
	j=0;
	while(j<length-1)	
	{

		temp=intResult[0];

		i=0;
		while(i<length)
		{
			intResult[i]=intResult[i+1];
			i++;
		}		
		intResult[length-1]=temp;

		//Converting to integer
		temp = 0;
		i=0;
		while(i<length)
		{
			temp = temp + intResult[i] * pow(10,i);
			i++;
		}
		if(temp<=stop&&start<=temp&&temp>num)
		{
				
				countr++;
				//cout<<"FROM NUMBER : "<<num <<endl;
				//cout<<temp<<endl;
		}
		j++;
	}


	
	
}


int main () {
 	long int i=0;
	int T;
	long int j;
	long int data[60][2];
	cin>>T;
 	
 	for(i=0;i<T;i++)
 	{
 		cin>>data[i][0];
 		cin>>data[i][1];
 	}

	for(i=0;i<T;i++)
	{
	
		start=data[i][0];
		stop=data[i][1];
		for (j=start; j<=stop; j++) 
		{	
			
			permute(j);	


		}
		cout<<"Case #"<<i+1<<": "<<countr<<endl;
		countr=0;
	}
	
	
			

  return 0;
}
