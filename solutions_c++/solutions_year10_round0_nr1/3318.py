
/*
ID: ir2pid1
LANG: C++
TASK: milk
*/

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <cctype>

using namespace std;

void qsort(int *a,int *b,int,int);
void swap(int *a,int *b,int,int);
bool toggle(bool temp)
{
	if(temp==false)
		return true;
	else
		return false;
}
double binary(int n)
{
	double temp=0;
	for(int i=0;i<n;i++)
	{
		temp=temp+pow(double(2),double(i));
	}
	return temp;
}


bool snapper(int n,int k)
{
	double val;
	val=binary(n);
	if(k<n)
		return false;
	else if(val==k)
		return true;
	else
	{
		while(k-val>1)
		{
			k=k-val;
			k--;
		}
	}

	if(k==0||k==val)
		return true;
	else
		return false;

}


//int *a,*b;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	vector<int> n,k;
	int t,x,y;

	fin>>t;

	//a=new int[no];
	//b=new int[no];

	for(int i=0;i<t;i++)
	{
		fin>>x>>y;
		n.push_back(x);
		k.push_back(y);
	}



	//qsort(a,b,0,no-1);

	for(int i=0;i<t;i++)
	{
		if(snapper(n[i],k[i]))
		{
			fout<<"Case #"<<i+1<<": ON"<<"\n";
		}
		else
		{
			fout<<"Case #"<<i+1<<": OFF"<<"\n";
		}
	}

		

	fin.close();
	fout.close();
}



void swap(int *a,int *b,int x,int y)
{
	int temp,left,right;
	left=x;
	right=y;

			temp=a[left];
			a[left]=a[right];
			a[right]=temp;

			temp=b[left];
			b[left]=b[right];
			b[right]=temp;
}


void qsort(int *a,int *b,int start,int end)
{
        int i = start;                          // index of left-to-right scan
        int k = end;                            // index of right-to-left scan

        if (end - start >= 1)                   // check that there are at least two elements to sort
        {
                int pivot = a[start];       // set the pivot as the first element in the partition

                while (k > i)                   // while the scan indices from left and right have not met,
                {
                        while (a[i] <= pivot && i <= end && k > i)  // from the left, look for the first
                                i++;                                    // element greater than the pivot
                        while (a[k] > pivot && k >= start && k >= i) // from the right, look for the first
                            k--;                                        // element not greater than the pivot
                        if (k > i)                                       // if the left seekindex is still smaller than
                                swap(a,b, i, k);                      // the right index, swap the corresponding elements
                }
                swap(a,b, start, k);          // after the indices have crossed, swap the last element in
                                                // the left partition with the pivot 
                qsort(a,b, start, k - 1); // quicksort the left partition
                qsort(a,b, k + 1, end);   // quicksort the right partition
        }
        else    // if there is only one element in the partition, do not do any sorting
        {
                return;                     // the array is sorted, so exit
        }
}
