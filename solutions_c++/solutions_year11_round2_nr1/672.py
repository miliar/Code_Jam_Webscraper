#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iostream>
using namespace std;
char mat[1000][1000];
int win[100], play[100];
double ow[100],oow[100];

void calcWin(int n)
{
   for(int r=0;r<n;r++) 
   {
     win[r]=play[r]=0;
     for(int c=0;c<n;c++) 
        if( mat[r][c]!='.'  )
	{
	   play[r]++;
	   if( mat[r][c]=='1'  )win[r]++;
	} 
   }
}
void calcOW(int n)
{  
   for(int r=0;r<n;r++) 
   {
     double sum=0.0;
     int C=0;
     for(int c=0;c<n;c++)
       if(r!=c)
     {
        if( mat[r][c]!='.'  )
	{
	   if( mat[r][c]=='0'  )  sum+=((win[c]-1)/(double)(play[c]-1));
	   else sum+=((win[c])/(double)(play[c]-1));
	   C++;
	}
     }
	ow[r]=sum/(double)(C);
   }
}
void calcOOW(int n)
{
   for(int r=0;r<n;r++) 
   {
     double sum=0.0;
     int C=0;
     for(int c=0;c<n;c++)
       if(  mat[r][c]!='.' )
        if( r!=c  )
	{
	   sum+=ow[c];
	   C++;
	}	   
	oow[r]=sum/(double)(C);
   }
}
int main()
{
 freopen("in.txt","r",stdin);
   int N;
   scanf("%d",&N);
  for(int _r=0;_r<N;_r++)
  {
    int n;
     scanf("%d",&n);
     for(int r=0;r<n;r++)
        scanf("%s",mat[r]);
     calcWin(n);
     calcOW(n);
     calcOOW(n);
     printf("Case #%d:\n",_r+1);     
     for(int r=0;r<n;r++)
     {       
       printf("%lf\n",.25*(win[r]/(double)play[r])+.5*ow[r]+.25*oow[r]);
     }
  }
 return 0;
}