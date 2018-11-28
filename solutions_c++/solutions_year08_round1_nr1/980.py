#include <iostream>
#include <cstdio>
#define MAX 900

using namespace std;

char buf[10000];

void product(int A[MAX], int B[MAX], int n, int x)
{
	long int prod = 0;
	int i;
	
	for(i = 0; i < n; i++)
	 prod += (A[i]*B[i]);
	 
	cout << "Case #"<< x+1 <<": "<< prod << endl;
} 

void bsort_B(int a[MAX], int n)
{
	int temp, c, i;
	do
	{
		c = 0;
		for(i = 0; i < n - 1; i++)
		if(a[i] < a[i+1])
		{
			temp = a[i];
			a[i] = a[i+1];
			a[i+1] = temp;
			c = 1;
		}
	}while(c);
}

void bsort_A(int a[MAX], int n)
{
	int temp, c, i;
	do
	{
		c = 0;
		for(i = 0; i < n - 1; i++)
		if(a[i] > a[i+1])
		{
			temp = a[i];
			a[i] = a[i+1];
			a[i+1] = temp;
			c = 1;
		}
	}while(c);
}


void input(int x)
{
	int n, i;
	int A[MAX], B[MAX];
	cin>>n;

	for(i = 0; i < n; i++)
	 cin>>A[i];
	
			
	bsort_A(A,n);
	
	
	for(i = 0; i < n; i++)
	 cin>>B[i];
		
		
		
	bsort_B(B,n);
	
	product(A,B,n,x);
}
	

	
int main ()
{
		freopen("/Users/shobhu/gcjor1_1-small.out","w",stdout);
		int T, i;
		cin>>T;
		
		for( i = 0; i < T; i++)
		 input(i);
		 
		return 0;
} 