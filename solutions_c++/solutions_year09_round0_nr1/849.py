#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int subst(char code[],int &pos,char c)
{   int x=0;
    if(code[pos]=='(')
    {    pos++;
         while(code[pos]!=')')
         { if(c==code[pos]) x=1; 
           pos++;} 
          
    }  
    else  if(c==code[pos]) x=1; 
    pos++;
    return x;
}     
int main()
{   int L,D,N,x,y,z,s,f,c,len,pos;
    char Word[5000][15],code[10000];
    scanf("%d %d %d",&L,&D,&N);
     for(x=0;x<D;x++)
      scanf("%s",Word[x]);
    for(x=0;x<N;x++)
    {
       scanf("%s",code); 
       s=0; 
       for(y=0;y<D;y++)
       {  pos=0;len=0;c=0;
          while(len<L)
          {    f=0;
               f=subst(code,pos,Word[y][len]);
               if(f==0){c=1; break;}
               len++;
          }
          if(c==0) s++;  
       }
       printf("Case #%d: %d\n",x+1,s);
    }
    return 0;
}
