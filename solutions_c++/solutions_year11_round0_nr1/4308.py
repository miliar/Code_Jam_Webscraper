#include<fstream>
#include<iostream>

using namespace std;

//ifstream f("date.in");
//ofstream g("date.out");

struct numere
{
   int lg;
   int d[120];
} a[2];

int N,lg,pt[120];
char c[600];

void read();
void solve2(int N);
void solve();
int aflanr (int &pos);

int main()
{
   read();
   
   //cin.close();
   //g.close();
   return 0;
}

void read()
{
   int i;
   cin>>N;
   cin.get();
   for (i=1;i<=N;++i)
   {
      cout<<"Case #"<<i<<": ";
      solve();
   }
}

int aflanr (int &pos)
{
   int nr=0;
   while(c[pos]>='0'&&c[pos]<='9'&&pos<=lg)
   {
      nr=nr*10+(c[pos]-'0');
      ++pos;
   }
   ++pos;
   return nr;
}

void solve()
{
   int nr,i,j,ok1,n2;
   cin.getline(c,600);
   lg=strlen(c);
   i=0;
   nr=aflanr(i);
   for (j=1;j<=nr;++j)
   {
      if (c[i]=='O') ok1=0;
      else ok1=1;
      
      pt[j]=ok1;
      
      i+=2;
      n2=aflanr(i);
      
      a[ok1].lg++;
      a[ok1].d[a[ok1].lg]=n2;
   }
   solve2(nr);
   a[0].lg=a[1].lg=0;
}

void solve2(int N)
{
   int nrs=0,R1,R2,i,I1,I2,pasi;
   i=1; I1=I2=1;
   R1=R2=1;
   while (i<=N)
   {
      if (R1!=a[0].d[I1]&&R2!=a[1].d[I2])
      {
         if (I2==-1||(abs(R1-a[0].d[I1])<abs(R2-a[1].d[I2])))
         {
            pasi=abs(R1-a[0].d[I1]);
            nrs+=pasi;
            R1=a[0].d[I1];
            if (I2!=-1)
               if (R2>a[1].d[I2]) R2-=pasi;
               else R2+=pasi;
            continue;
         }
         if (I1==-1||(abs(R1-a[0].d[I1])>=abs(R2-a[1].d[I2])))
         {
            pasi=abs(R2-a[1].d[I2]);
            nrs+=pasi;
            R2=a[1].d[I2];
            if (I1!=-1)
               if (R1>a[0].d[I1]) R1-=pasi;
               else R1+=pasi;
         }
         continue;
      }
      ++nrs;
      if (R1==a[0].d[I1]&&R2!=a[1].d[I2])
      {
         if (pt[i]==0)
            { 
               ++I1; ++i; 
               if (I1>a[0].lg) I1=-1;
            }
         if (R2>a[1].d[I2]) --R2;
         else ++R2;
         continue;
      }
      if (R1!=a[0].d[I1]&&R2==a[1].d[I2])
      {
         if (pt[i]==1)
            { 
               ++I2; ++i;
               if (I2>a[1].lg) I2=-1;
            }
         if (R1>a[0].d[I1]) --R1;
         else ++R1;
         continue;
      }
      if (R1==a[0].d[I1]&&R2==a[1].d[I2])
      {
         if (pt[i]==0)
            { ++I1; ++i; 
               if (I1>a[0].lg) I1=-1;
         continue; }
         if (pt[i]==1)
            { ++I2; ++i; 
         if (I2>a[1].lg) I2=-1;
         continue; }
         continue;
      }
   }
   cout<<nrs<<'\n';
}
