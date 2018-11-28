// a.cpp : Defines the entry point for the console application.
//


#include <algorithm>
#include <stdio.h>
#include <string>
using namespace std;
string data[105];
int f[105][1005];
int bsearch(string s,int n)
{
	int low,high,mid;
	int flag;
	low=1;
	high=n;
	flag=0;
	while(low<=high)
	{
		mid=(low+high)/2;
		if(s<data[mid])
			high=mid-1;
		else if(s>data[mid])
				low=mid+1;
		
		else
		{
			flag=mid;
			break;
		}
	}
	return flag;
}
int main()
{
     int test;
	 scanf("%d",&test);
	 int testc;
	 for(testc=1;testc<=test;testc++)
	 {
		 int q,g;
		 scanf("%d",&q);
		 int i,j,k,l;
		 char temp[105];
		 getchar();
		 for(i=1;i<=q;i++)
		 {
             gets(temp);
			 data[i]=temp;
		 }
		 scanf("%d",&g);
		 sort(data+1,data+q+1);
         memset(f,0,sizeof(f));
		 getchar();
		 int Min=10000;
		 for(i=1;i<=g;i++)
		 {
             gets(temp);
			 j=bsearch(temp,q);
			 
			 for(k=1;k<=q;k++)
			 {
				 Min=10000;
				 for(l=1;l<=q;l++)
				 {
					 if(f[l][i-1]<Min)
						 Min=f[l][i-1];
				 }
                 if(f[k][i-1]>Min+1)
					 f[k][i]=Min+1;
				 else
					 f[k][i]=f[k][i-1];			 
				
			 }
			 f[j][i]=100000;
			 
		 }
		 int min=10000;
		 for(i=1;i<=q;i++)
		 {
			 if(f[i][g]<min)
				 min=f[i][g];
		 }
		 printf("Case #%d: %d\n",testc,min);


	 }
	return 0;
}
