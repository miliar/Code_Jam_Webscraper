
/*
ID: ir2pid
LANG: C++
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

int euros(int r,int k,list<int>g)
{
	int total=0;
	list<int>::iterator it;
	for(it=g.begin();it!=g.end();it++)
	{
		total=total+*it;
	}

	int sum=0;
	if(k<total)
	{
		for(int i=0;i<r;i++)
		{


			//list<int>::iterator it;
			it=g.begin();
			int count=0;
			while(count + *it <=k)
			{
				count = count+*it;
				int tmp = *it;
				g.pop_front();
				g.push_back(tmp);
				it=g.begin();
			}
				
			sum=sum+count;
		}
		return sum;
	}
	else
	{
		return total*r;
	}
	

}


//int *a,*b;

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	vector<int> r,k;
	list<int>tmp;
	vector<list<int>> g;
	int t,n,tx,ty,tz;

	fin>>t;

	//a=new int[no];
	//b=new int[no];

	for(int i=0;i<t;i++)
	{
		fin>>tx>>ty>>n;
		r.push_back(tx);
		k.push_back(ty);
		tmp.clear();
		for(int j=0;j<n;j++)
		{
			
			fin>>tz;
			tmp.push_back(tz);
		}
		g.push_back(tmp);

	}



	//qsort(a,b,0,no-1);



	for(int i=0;i<t;i++)
	{
		int tmp = euros(r[i],k[i],g[i]);

			fout<<"Case #"<<i+1<<": "<<tmp<<"\n";
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
