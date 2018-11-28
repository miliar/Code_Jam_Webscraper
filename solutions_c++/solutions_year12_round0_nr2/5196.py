#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;


int main(){
    int T,n,s,p,a,t[100]={};
    scanf("%d",&T);
    FILE *f = fopen("BB.out","w+");
    int z=1;
    while(T--)
    {
    int total=0;
     scanf("%d %d%d",&n,&s,&p);
     for(int i=0;i<n;i++)
     {
     scanf("%d",&a);
     //int c1=a/3,c2=(a-a/3)/2;
    // int c3=a-c2-c1;
     int c1=a/3,c2=a/3,c3=a/3;
     int ss=0;
     while(c1+c2+c3 < a)
     {
      if(ss%3==0)c1++;
      else if(ss%3==1)c2++;
      else c3++;
      ss++;
      ss%=3;               
     }
     
     if(c1 >= p || c2 >= p || c3 >= p) total++;
     else if(((c1+1 >= p && (c2>0 || c3>0)) || (c2+1 >= p && (c1>0 || c3>0)) || (c3+1 >= p && (c2>0 || c1>0)) ) && s)total++,s--;  
     else if(abs(c1-c2)==1 && abs(c1-c3)==1 && abs(c3-c2)==1 && ((c1+2 >= p && (c2>0 && c3>0)) || (c2+2 >= p && (c1>0 && c3>0)) || (c3+2 >= p && (c2>0 && c1>0)) ) && s)total++,s--;             
     }
     fprintf(f,"Case #%d: %d\n",z++,total);
    }
    
    return 0;
    }
