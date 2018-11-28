#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

//solution:
//


int T, N;

ifstream o("B-small-attempt2.in");
//ifstream o("B-large-practice.in");
ofstream oo("b-small.out");
//ofstream oo("b-large.out");

int cmp ( const void *a , const void *b ) 
{ 
return *(int *)a - *(int *)b; 
} 

//read data from file
void read()
{
	
	int i, j;
	o>>T;
	cout<<T<<endl;
}

int exchangesub(int sub, int k)
{
	cout<<"exchangesub:"<<sub;
	int result=0;
	int* a=new int[20];
	int i;
	for(i=0; i<k; i++)
	{
		a[i]=sub%10;
		sub/=10;
	}
	qsort(a,k,sizeof(int), cmp);
	for(i=0; i<k; i++)
	{
		result*=10;
		result+=a[i];
	}
	cout<<":"<<result<<endl;
	return result;
}

int exchange(int N, int j, int cc, int kk)
{
	int cN=N, ccc, k=1, i=1, last;
	bool b=false;
	for(;i<j;i*=10, k++)
	{
		ccc=cN%10;
		if(ccc>cc)
		{
	//		cN=cN/=10;
//			int next=cN%10;
	//		while(next==ccc)
	//		{
//				i*=10;
//				k++;
//				cN=cN/=10;
//				next=cN%10;
//			}
				N+=ccc*j-ccc*i+cc*i-cc*j;
			//	i*=10;
				N+=exchangesub(N%j, kk)-N%j;
				return N;
			
		}
		cN/=10;
	}
	return N;
}
int changeall(int N)
{
	int n=0, m=0, cN=N, cc;
	int result = 0, chengshu=1;
	bool b=false;
	while(cN!=0)
	{
		cc=cN%10;
		cout<<cc<<endl;
		if(cc==0)
		{
			m++;
			chengshu*=10;
		}
		else
		{
			if(b==false)
			{
				b=true;
				result+=cc*chengshu*10;
				cout<<result<<endl;
			}
			else
			{
				result=result*10;
				cout<<result<<endl;
				result=result+cc;
				cout<<result<<endl;
			}
		}
		n++;
		cN/=10;
		
	}
	return result;
}

void onecase(int n)
{
	int i, j;

	o>>N;
	cout<<N<<endl;

	int result = N;
	int last = -1, cc, cN;

	for(j=1, i=1, cN=N; cN>0; j*=10, i++)
	{
		cc=cN%10;
		if(cc>=last)
		{
			last = cc;
			cN=cN/10;
			
			continue;
		}
		else
		{
			cout<<"exchange"<<endl;
			result=exchange(N, j, cc, i);
			break;
		}
	}
	if(cN==0)
	{
		cout<<"changeall"<<endl;
		result=changeall(N);
	}

	oo<<"Case #"<<n<<": "<<result<<"\n";
	cout<<"Case #"<<n<<": "<<result<<"\n";
	
}

int main()
{
	read();
	for(int i=1; i<=T; i++)
	{
		
		onecase(i);
	}
	oo.close();
	return 0;
}
