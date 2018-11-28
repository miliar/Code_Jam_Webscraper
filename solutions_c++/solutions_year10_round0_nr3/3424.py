#include <iostream>
#include<fstream>

using namespace std;
int a[1002],r,k,n,i,j,m,s,y,nekoj,z,t,tt,pocetok,kraj,mom;
bool b[1002][1002];
long long int odgovor,pari,x,c[1002][1002],d[1002][1002];

int main()
{
     ifstream fin("test.in");
    ofstream fout("test.out");
    fin>>t;
    for (tt=1;tt<=t;tt++)
    {
        fin>>r>>k>>n;
        for (i=1;i<=1001;i++)
        for (j=1;j<=1001;j++)
        {
            b[i][j]=false,c[i][j]=0,d[i][j]=0;
        }
        for (i=1;i<=n;i++)
        fin>>a[i];
        mom=0;
        pari=0;
        pocetok=1;
        i=0;
        odgovor=0;
        while (true)
        {
              x=0;
              pocetok=i+1;
              if (pocetok>n) pocetok=1;
              while (x<=k)
              {
                    i++;
                    if (i>n) i=1;
                    if (i==pocetok && x!=0) break;
                    x=a[i]+x;
              }
              if (x>k)
              {
                 x=x-a[i];
                 i--;
              }
              pari=x+pari;
              mom++;
              nekoj=i;
              if (nekoj==0) nekoj=n;
              if (b[pocetok][nekoj]==true)
              {
                 odgovor=odgovor+d[pocetok][nekoj];
                 r=r-c[pocetok][nekoj];
    odgovor=odgovor+(r / (mom-c[pocetok][nekoj]))*(pari-d[pocetok][nekoj]);
            // cout<<odgovor;
                 mom=r-(r % (mom-c[pocetok][nekoj]));
                 pari=0;
                 break;
              }
              
              
              
              b[pocetok][nekoj]=true;
              c[pocetok][nekoj]=mom;
              d[pocetok][nekoj]=pari;
              if (mom==r) { odgovor=pari; pari=0; break; }
         }
         while (mom<r)
         {
               x=0;
               pocetok=i+1;
               if (pocetok>n) pocetok=1;
               while (x<=k)
               {
                     i++;
                     if (i>n) i=1;
                     if (i==pocetok && x!=0) break;
                     x=a[i]+x;
               }
               if (x>k)
               {
                       x=x-a[i];
                       i--;
               }
               pari=x+pari;
               mom++;
               
         }
            fout<<"Case #"<<tt<<": "<<odgovor+pari<<endl;
 }
    return 0;
}

