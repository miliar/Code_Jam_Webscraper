#include<iostream>
#include<string>
#include<list>
#include<math.h>
using namespace std;

//list<long long> digits;

bool ugly(long long num)
{
	if(!num)
		return true;
	if(num%2==0)
		return true;
	if(num%3==0)
		return true;
	if(num%5==0)
		return true;
	if(num%7==0)
		return true;
	return false;
}

int main()
{
	long long N,N2,i,j,k,sum,temp,counter;
	char op;	
	string num;
	cin>>N;
	N2 = N;
	while(N--)
	{
		counter=0;
		cin>>num;
		//for(long long i=0; i<num.length(); i++)
		//	digits.push_back(num[i]-'0');
		long long lim = 1;
		for(j=0; j<num.length() - 1; j++)
			lim*=3;
		for(long long j=0; j<lim; j++)
		{
			i=j;
			temp=0;
			sum=0;
			op='+';
			for(k=0; k< num.length(); k++)
			{
				temp*=10;
				temp+=num[k]-'0';

				if(k==num.length()-1)
				{
					sum+= (op=='+')?temp:-temp;
					break;
				}

				switch(i%3)
				{
				case 0:
					break;
				case 1:
					sum += (op=='+')?temp:-temp;
					op='+';
					temp=0;
					break;
				case 2:
					sum += (op=='+')?temp:-temp;
					op='-';
					temp=0;
					break;
				}
				i/=3;
			}
				//i/=3;
				//cout<<j<<' '<<sum<<endl;
				if(ugly(sum))
					counter++;
			
		}
		cout<<"Case #"<<-(N-N2)<<": "<<counter;
		if(N) cout<<endl;
	}
}
