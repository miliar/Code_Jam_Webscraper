#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
char G[100]="welcome to code jam";
int main()
{   int N,x,y,z,w,A[500],D[500],s,len;
    char inp[500],c;
    scanf("%d",&N);scanf("%c",&c);
    for(x=0;x<N;x++)
    {  len=0;
       scanf("%c",&c);
       while(c!='\n')
       {   inp[len++]=c;  scanf("%c",&c); }
       inp[len]='\0';
       for(y=0;y<500;y++){ A[y]=0; D[y]=0;}
       for(y=0;y<len;y++)
        if(inp[y]=='w')  A[y]=1;
       for(y=1;y<strlen(G);y++)
       {  for(z=0;z<len;z++) D[z]=0;
          for(z=0;z<len;z++)
          {  if(G[y]==inp[z])
             {  s=0; 
                for(w=0;w<z;w++)
                  if(inp[w]==G[y-1])s=(s+A[w])%10000; 
                D[z]=s;
                 
             }
          }
          for(z=0;z<len;z++) A[z]=D[z];
       }
       s=0;
       for(z=0;z<len;z++) s=(s+A[z])%10000;     
       printf("Case #%d: ",x+1);
       if(s<10) printf("000");
       else if(s<100) printf("00");
       else if(s<1000) printf("0");
       printf("%d\n",s);
    }
    return 0;
}
       
    
