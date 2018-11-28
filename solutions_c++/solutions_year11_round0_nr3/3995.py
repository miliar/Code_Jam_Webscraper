#include<fstream>
#include<iostream>

using namespace std;

//ifstream f("date.in");
//ofstream g("date.out");

int T,i,N,val0,val1,S1,S0,a[20],v[20],maxx;

void solve();
void back(int k,int X0, int X1);

int main()
{
   cin>>T;
   for (i=1;i<=T;++i)
   {
      cout<<"Case #"<<i<<": ";
      val1=val0=maxx=0;
      solve();
   }
   //f.close();
   //g.close();
   return 0;
}

void solve()
{
   int i;
   cin>>N;
   for (i=1;i<=N;++i)
      cin>>a[i];
   back(1,0,0);
   if (maxx==0)
      cout<<"NO\n";
   else cout<<maxx<<'\n';
}

void back(int k,int X0, int X1)
{
   int i,X02=X0,X12=X1;
   if (k==N+1)
   {
      if (X0==X1&&S1&&S0)
      {
         if (maxx<S1) maxx=S1;
         if (maxx<S0) maxx=S0;
      }
   }
   else 
      for (i=0;i<2;++i)
      {
         X02=X0;
         X12=X1;
         v[k]=i;
         if (v[k])
         {
            X12=X1 xor a[k];
            S1+=a[k];
         }
         else
         {
            X02=X0 xor a[k];
            S0+=a[k];
         }
         
         back(k+1,X02,X12);
         
         if (v[k])
            S1-=a[k];
         else 
            S0-=a[k];
      }
}


