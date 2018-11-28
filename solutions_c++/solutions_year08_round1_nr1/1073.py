#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;  
 
int main()
{

   vector<int>array1,array2; 
      
   int i,j,n,n1,num;
   long int res=0;
   cin>>n;   
   for (i=0;i< n;i++)
    {
     cin>>n1;
     for (j=0;j<n1;j++)
       {cin>> num;
        array1.push_back(num);}
     sort(array1.begin(), array1.end());
     for (j=0;j<n1;j++)
       {cin>> num;
        array2.push_back(num);}
     sort(array2.begin(), array2.end());
     for (j=0;j<n1;j++)
         res += array1[j]*array2[n1-1-j];
     printf("Case #%d: %ld\n",i+1,res);
     res=0;
     array1.clear();
     array2.clear();
    }
   
    
 }   
