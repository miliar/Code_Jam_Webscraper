#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<cstdlib>
#include<cctype>
#include<cstring>
using namespace std;

int power(int n);
int ar[19];
int br[40];
int g[1009][1009];

int main()
{
 
 freopen("C-small-attempt3.in.txt","r",stdin);
 freopen("C-small-attempt0.out.txt","w",stdout);
 int j,ks,n,tmp,l,i,num;
 int low,high,k,p,cnt;
scanf("%d",&ks);
for(l=1;l<=ks;l++)
 {
  memset(g,0,sizeof(g));
  cnt=0;
  scanf("%d%d",&low,&high);
 
 for(n=low;n<=high;n++)   
     {
         p=0;k=0;	  
	  int digit=log10(n)+1;
        tmp=n;
		while(tmp)	   
	      {
              ar[k++]=tmp%10;	 	   
		       tmp=tmp/10;
			   
		  }
	  for(i=k-2;i>=0;i--) 
	    br[p++]=ar[i];
	  for(i=k-1;i>=0;i--)
	    br[p++]=ar[i];
//ok............................
int tmp2=digit;
int loop=0;
num=0; 
 for(i=0;i<p-digit;i++)
  	 {
	  num=0;
	  loop=i;
	  tmp2=digit;
	 for(j=0;j<digit;j++) 
	   {
	      num=num+br[loop]*power(tmp2-1);
			loop++;
			tmp2--;
		}
   //cout<<num<<endl;	
       	    if( (num!=n) && ((log10(num)+1)!=num) && (g[n][num]!=1) && (num>=low) && (num<=high))
	                  {  cnt++;
	                        g[n][num]=g[num][n]=1;
	                   }
  	   }

    }
 
printf("Case #%d: ",l);
 cout<<cnt<<endl;
 }
return 0;
}
int power(int n)
 {
 int res=1;
  for(int i=0;i<n;i++) 
     res*=10;
 return res;
 }

