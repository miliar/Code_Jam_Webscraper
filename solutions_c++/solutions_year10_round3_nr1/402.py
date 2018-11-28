#include <iostream>
using namespace std;


template <typename T>
void Merge(int l,int m,int r,T A[])
{
	T * B=new T[r-l+1];
	for(int i=0;i<r-l+1;i++)
	{
		B[i]=0;
	}
	int ind1=l,ind2=m+1,ind3=0;
	while(ind1<=m && ind2<=r)
	{
		if(A[ind1]<A[ind2])
		{
			B[ind3++]=A[ind1++];
		}
		else
		{
			B[ind3++]=A[ind2++];
		}
	}
	if(ind1<m) 
	{
		for(int i=ind1;i<=m;i++)
		{
			B[ind3++]=A[i];
		}
	}
	else
	{
		for(int i=ind2;i<=r;i++)
		{
			B[ind3++]=A[i];
		}
	}
	delete [] B;
}


template <typename T>
void MergeSort(int l,int r,T A [])
{
	if(l<r)
	{
		int m=(l+r)/2;
		MergeSort(l,m,A);
		MergeSort(m+1,r,A);
		Merge(l,m,r,A);
	}
}




int main()
{
	int arr[6]={1,7,3,0,100,87};
	MergeSort<int>(0,5,arr);
	for(int i=0;i<5;i++)
	{
		cout<<arr[i]<<endl;
	}
	cout<<"hello,world"<<endl;
	return 1;
}
