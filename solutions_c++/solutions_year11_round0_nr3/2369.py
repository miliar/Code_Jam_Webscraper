#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;

long moddiff(long, long);
int cwbs(int,int);
int main() 
{
    //--------------------------------
    int  t;
    cin >> t;
    int  _case = 1;
    int arr[1000];
    int list1[1000];
    int list2[1000];
	for(;_case<=t;_case++)
	{     
        int n;
        cin >> n;
        memset(list1, 0 ,sizeof(list1));
        memset(list2, 0 ,sizeof(list2));
        memset(arr,   0 ,sizeof(arr));
        for(int i=0; i<n; i++)
          cin >> arr[i];
        for(int i=0; i<n; i++)   
           for(int j=0; j<n; j++)
           {
             if(arr[i]>arr[j])
             {
              arr[i] = arr[i] + arr[j];
              arr[j] = arr[i] - arr[j];
              arr[i] = arr[i] - arr[j];                 
             }       
           } 
        int S[1000];  
        long sum = 0;
        //---------------------------------- 
        sum = 0;
        for(int i=0; i<n-1; i++)
        {
           int sum1 = 0, sum2=0; 
           long tempsum1 = 0, tempsum2 = 0;     
           for(int j=0; j<=i; j++)
           {
              sum1 = cwbs(sum1,arr[j]); 
              tempsum1 = tempsum1 + arr[j];
           }   
           for(int j=i+1; j<n; j++)
           {
              sum2 = cwbs(sum2,arr[j]);
              tempsum2 = tempsum2 + arr[j];  
           } 
           if(sum1==sum2)
              if( max(tempsum2,tempsum1) >sum )
                sum = max(tempsum2,tempsum1);
        }   
    	//------------- o/p ----------------
		cout << "Case #" << _case << ": " ;
		if (sum == 0)
         cout << "NO";
        else 
         cout << sum;
		cout << endl;
}
	return 0;
}

long moddiff(long a, long b)
{
       if (a > b)
          return a - b;
        else
          return b - a;     
}

int cwbs(int a, int b)
{
    int x = 1; int sum = 0;
    while(a>=1 || b>=1)
    {
        sum = sum + ((a%2 + b%2) %2) * x;
        x = x*2; 
        a = a/2;
        b = b/2;
    }
    return sum;
}
