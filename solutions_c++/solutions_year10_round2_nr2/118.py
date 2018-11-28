#include<iostream>
#include<vector>
using namespace std;
int N,K,B,T;
int L[100];
int V[100];
vector <int> Fast,Slow;
void Work()
{
     Fast.clear();
     Slow.clear();
     scanf("%d %d %d %d",&N,&K,&B,&T);
     double LIMIT=double(T)-1e-9;
     for (int i=0;i<N;++i) scanf("%d",&L[i]);
     for (int i=0;i<N;++i) scanf("%d",&V[i]);     
     for (int i=N-1;i>=0;--i)
     if (V[i] * T >= B - L[i])
              Fast.push_back(i); else
              Slow.push_back(i);
     if (Fast.size()<K) 
     {printf("IMPOSSIBLE"); return ;}
     int Ans=0;
     for (int i=0;i<K;++i)
     {
         int p=N-1,q;
         while (p>=0 && V[p]*T>=B-L[p]) --p;
         if (p<N-K) 
         {
             printf("%d",Ans);
             return ;
         }
         q=p-1;
         while (V[q]*T<B-L[q]) q--;
         for (int j=q+1;j<=p;++j)
         {
             Ans++;
             swap(L[j-1],L[j]);
             swap(V[j-1],V[j]);
         }
     }
             printf("%d",Ans);
     
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large-Ans.txt","w",stdout);
    int Cases;
    scanf("%d",&Cases);
    for (int i=1;i<=Cases;i++)
    {
        printf("Case #%d: ",i);
        Work();
        printf("\n");
    }
    return 0;
}
