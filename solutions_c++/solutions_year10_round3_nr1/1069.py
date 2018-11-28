using namespace std;
#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<map>
struct connect
{ int A,B; };
bool chk(connect P,connect Q)
{ if((P.A<Q.A) && (P.B>Q.B)) return 1;
  if((P.A>Q.A) && (P.B<Q.B)) return 1;
  return 0;
}
int main()
{   long long x,y,z,ans,T,N;
    scanf("%lld",&T); 
    for(x=0;x<T;x++)
    {  ans=0;
       scanf("%lld",&N); 
       vector<connect> line(N);
       for(y=0;y<N;y++)
         scanf("%d %d",&line[y].A,&line[y].B);
       for(y=0;y<N;y++)
        for(z=y+1;z<N;z++)
         if(chk(line[y],line[z])) ans++;
       printf("Case #%lld: %lld\n",x+1,ans);    
     }
     return 0;
}     
