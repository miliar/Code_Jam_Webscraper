#include<iostream>
#include<fstream>
using namespace std;

int getdig(int A)
{
	int i=0;
	while(A>0)
	{
		A=A/10;
		i++;
	}
	return i;
}

int pow(int n,int k)
{
	int i;
	int result=1;
	for(i=0;i<k;i++)
	{
		result=result*n;
	}
	return result;
}

int main()
{
	int T,N,A,B,i,j,k,flag=0,lendata,numdig,temp,count,temp1;
	ifstream ip("C-large.in");
	ofstream op("write.txt");
	ip>>T;
	for(i=0;i<T;i++)
	{
		ip>>A;
		ip>>B;
		count=0;
		numdig=getdig(A);
		for(j=A;j<=B;j++)//j=n
		{
			k=0;
			temp=j;
			while(k<numdig-1)
			{
				temp1=temp%10;
				temp=pow(10,numdig-1)*temp1 + temp/10;
				//cout<<temp<<"\t";
				if(temp==j)
				{
					break;
				}
				
				else if(temp>j && temp<=B)
					count++;
				
				k++;
			}
			//cout<<"\n";
		}
		op<<"Case #"<<i+1<<": "<<count<<endl;
	}
	ip.close();
	op.close();
	return 0;
}
