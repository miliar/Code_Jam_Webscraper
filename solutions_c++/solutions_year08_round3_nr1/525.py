#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <istream>
#include <string.h>
#include <vector>
#include <sstream>

using namespace std;


#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define sz(a) int((a).size())

typedef vector<int> vi;
typedef vector<string> vs;


void quick_sort(int *array,int n)
{

 int i,j,x,temp;
 if(n > 1)
 {

  i = -1;
  j = n-1;
  x = array[n-1];
  while(1)
  {
     while(array[++i] < x);
     while(array[--j] > x);
     if(i>=j)
      break;
     temp = array[i];
     array[i] = array[j];
     array[j] = temp;
  }
    temp = array[i];
    array[i] = array[n-1];
    array[n-1] = temp;
    quick_sort(array,i);
    quick_sort(array+i+1,n-i-1);
 }
}


void main()
{
	int casenum,i,j;
	cin >> casenum;
	int p, k, l;
	int x[1001];
	
	for(i=0; i<casenum; i++)
	{
		cin >> p >> k >> l;
		for(j=0 ; j<l; j++)
			cin >> x[j];

		quick_sort(x,l);

		long long ans=0;

		int j=1, jj=1, kk;
		for(kk=l-1; kk>=0; kk--)
		{
			ans += x[kk] * jj;

			if(j==k)
			{
				jj++;
				j=1;
			}
			else j++;
		}

		cout << "Case #" << i+1 << ": " << ans << "\n";

	}
}
