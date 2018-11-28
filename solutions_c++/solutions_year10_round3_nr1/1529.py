#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
using namespace std;
typedef struct
{
      int A,B;  
}Point;
Point P[10000];
int compare (const void * a, const void * b)
{
    Point *t = (Point *)a,*t1 = (Point*)b;
  return ( t1->B - t->B);
}

int main()
{
    int T, TC = 0,N,i;
    freopen("A.in","r",stdin);  freopen("Aout.txt","w",stdout);
    scanf("%d",&T);
    for(TC = 1;TC <= T;TC++)
    {
           scanf("%d",&N);
           memset(P,0,sizeof(P));
           for(i = 0;i < N;i++) scanf("%d%d",&P[i].A,&P[i].B);
           qsort(P,N,sizeof(Point),compare);
//           for(int i = 0;i < N;i++) printf("%d %d\n",P[i].A,P[i].B);
             int cnt;
           for(cnt = 0,i = 1;i < N;i++)  
                 if( (P[0].A > P[i].A && P[0].B < P[i].B) || (P[0].A < P[i].A && P[0].B > P[i].B))
                     cnt++;
           printf("Case #%d: %d\n",TC,cnt);           
    }
    return 0;
}
