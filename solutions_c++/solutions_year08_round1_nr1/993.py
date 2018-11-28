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
	int casenum,i,j,k;
	cin >> casenum;
	int t;
	int x[1000],y[1000];
	
	for(i=0; i<casenum; i++)
	{
		cin >> t;
		for(j=0 ; j<t; j++)
			cin >> x[j];
		for(j=0; j<t; j++)
			cin >> y[j];

		quick_sort(x,t);
		quick_sort(y,t);

		j=t-1;
		int ans=0;

		for(k=0 ; k<t; k++)
		{	
			ans += x[k] * y[j];
			j--;
		}

		cout << "Case #" << i+1 << ": " << ans << "\n";

	}
}


