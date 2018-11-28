#include <iostream>
#include <fstream>
#include <string>
 
#include <windows.h>
using namespace std;
void Split(int line ,ifstream &input ,ofstream &output) ;
void QuickSort(long *arr,int low , int high) ;
long Partition(long *arr,int low ,int high) ;

const int DIGITS =31;
int main()
{
	long start = GetTickCount();
	ifstream input("C-large.in",ios::in);
	if(!input)
	{
		cerr<<"Cannot read target file"<<endl;
		exit(1);
	}

	ofstream output("C-large.out",ios::out);
	if(!output)
	{
		cerr<<"Cannot open output file"<<endl;
		exit(1);
	}
	int lines ;
	input>>lines;
	
	int i =0;
	for (i=0;i<lines;i++)
	{
		Split(i, input,output);
	}

	input.close();
	output.close();
	long end = GetTickCount();
	cout<<"Time : "<<end - start<<" ms"<<endl;
	system("pause");
	return 0;
}
void Split(int line ,ifstream &input ,ofstream &output)
{
	int candy_count , i ,j ;
	input>> candy_count ; 
	long  *candies = new long[candy_count] ;

	long sum = 0;
	for(i =0 ;i<candy_count;i++)
	{
		input>>candies[i] ;	
	}

	// if Patrick doesn't cry, it means ,in this array, the total appearing times of 1 in each binary digit must be an even number
	// we check parity of each digit , parity[j] is 0 means the jth digit of total appearing times of 1 is even , parity[j] is1 means odd
	//start from low digit ,that is : parity[0] stands for the lowest digit 
	int parity[DIGITS]={0};
	for(i=0;i<candy_count ;i++)
	{
		long tmp =candies[i] ;
		//if the jth digit is 1 ,change the parity[j]
		for(j=0;j<DIGITS; j++)
		{
			if(  (tmp &0x01)==1)
				parity[j] =  ( (parity[j]==0) ? 1 :0)  ;
			tmp>>=1 ;
		}
	}
	bool dividable = true; 
	for(i=0;i<DIGITS ;i++)
	{
		if(0!=parity[i])
		{
			dividable = false ;
			break ;
		}
	}
	if( !dividable)
	{
		//cout<<"Case #"<<line+1<<":  NO\n";
		output<<"Case #"<<line+1<<":  NO\n";
		delete[] candies;
		return ;
	}

	QuickSort(candies ,0,candy_count-1) ;
	for(i=1 ;i<candy_count ;i++)
	{
		sum +=candies[i] ;
	}
	output<<"Case #"<<line+1<<":  "<<sum<<"\n";
	//cout<<"Case #"<<line+1<<":  "<<sum<<"\n";
	delete[] candies;
}



void QuickSort(long *arr,int low , int high)
{


	if(!arr)
		return ;
	if (low<high)
	{
		long pivotloc = Partition(arr,low,high);
		QuickSort(arr,low,pivotloc-1);
		QuickSort(arr,pivotloc+1,high);
	}
}

long Partition(long *arr,int low ,int high) 
{
	long pivot = arr[low];
	while (low<high)
	{
		
		while(low<high && arr[high]>=pivot)
			high --; 
		arr[low]= arr[high] ;
		while(low<high && arr[low]<=pivot)
			low ++;
		arr[high]= arr[low];
	}
	arr[low] = pivot;
	return low ;
}