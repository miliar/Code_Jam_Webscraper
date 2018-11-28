#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
using namespace std;

inline void swap(unsigned long long *ptra,unsigned long long *ptrB);
void insertionSort(unsigned long long a[],int n);
void display(int a[],int n);
int P,K,L;
unsigned long long freq[1001];

int main()
{
	int N,i,caseNo;
	cin>>N;
	for(caseNo=1;caseNo <= N;caseNo++)
	{
		cin>>P>>K>>L;
		for(i=0;i < L;i++)
			cin>>freq[i];
		insertionSort(freq,L);
		int count=1;
		unsigned long long keyStrokes=0;
		
		for(i=0;i < L;i++)
		{
			keyStrokes+=count*freq[i];
			if((i+1) % K == 0)
				count++;
		}
		cout<<"Case #"<<caseNo<<": "<<keyStrokes<<endl;
	}
	return 0;
}




inline void swap(unsigned long long *ptra,unsigned long long *ptrB)
{
	unsigned long long temp=*ptra;
	*ptra=*ptrB;
	*ptrB=temp;
}
void insertionSort(unsigned long long a[],int n)
{
	int i,j;
	unsigned long long temp;
	for(i=1;i < n;i++)
	{
		temp=a[i];
		j=i-1;
		while(j >= 0 && temp > a[j]) /* j cannot be unsigned int with this condition */
		{
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=temp;		
	}
}


void display(int a[],int n)
{
	int i;
	printf("\n");
	for(i=0;i < n;i++)
		printf("%d ",a[i]);
}
