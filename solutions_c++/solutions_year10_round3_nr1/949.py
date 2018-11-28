#include<iostream>
#include<string.h>
using namespace std;

const int maxn=1001;

struct point
{
 int A,B;
};
point p[maxn];

int T,N;
//int ans;

int sol()
{
 int br=0;
 
 for(int i=1;i<=N;i++)
  for(int j=i+1;j<=N;j++)
   if((p[i].A>p[j].A && p[i].B<p[j].B) || (p[i].A<p[j].A && p[i].B>p[j].B))
    br++;

return br;
}

int main()
{
 scanf("%d", &T);
  
  for(int i=1;i<=T;i++)
   { 
   // ans=0;
   scanf("%d", &N);
    
    for(int j=1;j<=N;j++)
     scanf("%d %d", &p[j].A, &p[j].B);
    
   cout<<"Case #"<<i<<": "<<sol()<<endl;
    }

return 0;
}
