#include<iostream>
#include<cstring>
using namespace std;
string C[50];
string D[50];
void Solve(int id)
{
     int A,B,L;
     cin>>A;
     for (int i=0;i<A;++i) cin>>C[i];
     cin>>B;
     for (int i=0;i<B;++i) cin>>D[i];
     cin>>L;
     string tmp;
     cin>>tmp;
     char stack[200];
     int sn=0;
     for (int i=0;i<L;++i)
     {
         stack[sn++]=tmp[i];
         bool flag=true;
         if (sn>=2)
         {
               for (int i=0;i<A;++i)
               {
                if ((stack[sn-1]==C[i][0] && stack[sn-2]==C[i][1])  || 
                (stack[sn-1]==C[i][1] && stack[sn-2]==C[i][0]))
                {
                   stack[sn-2]=C[i][2];
                   sn--;
                   flag=false;
                }
                if (!flag) break;
               }
         }
         if (flag)
         {
             for (int i=0;i<B;++i)
             {
                 for (int j=0;j<sn-1;++j)
                 {
                     if ((stack[j]==D[i][0] && stack[sn-1]==D[i][1]) ||
                    (stack[j]==D[i][1] && stack[sn-1]==D[i][0]))
                    {
                                       sn=0;
                                       flag=false;
                    }
                    if (!flag) break;
                 }
                 if (!flag) break;
             }
         }
     }
     printf("Case #%d: [",id);
     if (sn>0)
     {
           printf("%c",stack[0]);
           for (int i=1;i<sn;++i)
           printf(", %c",stack[i]);
     }
     printf("]\n");
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int T;
    cin>>T;
    for (int i=0;i<T;++i) Solve(i+1);
    return 0;
}
