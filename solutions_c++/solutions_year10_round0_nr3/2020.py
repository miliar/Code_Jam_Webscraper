#include<iostream>
#include<fstream>
using namespace std;
long long euro,N,k,R,T,sum,g[1005],muia;
ofstream fout("date.out");

void solve()
{int i,q=1,pas,p;
long long eps=0,no;
  muia=0;
  for(i=1;i<=N;i++)
    muia+=g[i];
   if(muia<=k)
   sum=R*muia;
   else

   { for(i=1;i<=R;i++)
    {
        eps=0;

        pas=q;
        p=1;
        for(q;(eps+g[q]<=k);)
        {
            eps=eps+g[q];

            if(q<N)
            q++;
            else q=1;

        }

        sum+=eps;
    }
}
}

void cit()
{int i,j;
    ifstream fin("date.in");
    fin>>T;
    for(i=1;i<=T;i++)
     {fin>>R>>k>>N;
     for(j=1;j<=N;j++)
     {fin>>g[j];

     }

     sum=0;
     solve();
     fout<<"Case #"<<i<<": "<<sum<<'\n';
     sum=0;


     }
     fin.close();
}
int main()
{
    cit();
    fout.close();
    return 0;
}
