#include <iostream>
#include <string>
#include <vector>
using namespace std;


int numer(vector<string> se, string que)
{
int i;
for(int i=0;i<100;i++)
  if (se[i]==que) return i;
return -1;
}


int maks(int tab[1001][100], int j,int s)
{
int pom=1999;
for(int i=0;i<s;i++)
  if (tab[j][i]<pom) pom=tab[j][i];
return pom;
}

int main()
{
string que;
vector<string> se(100);
int tab[1001][100];
int n,q,s,p,j;
cin>>n;
for(j=0;j<100;j++)
     tab[0][j]=0;
for(int i=0;i<n;i++)
  {
//   cout<<"ala ma kota";
   cin>>s;
   getline(cin,que);
   for(j=0;j<s;j++)
     getline(cin,se[j]);
//     cout<<" a kot ma ale"<<se[j]<<endl;
   cin>>q; 
   getline(cin,que);
   for(j=1;j<=q;j++)
     {
 //    cout<<"bbbbbbbb";
     getline(cin,que);
     
     p=numer(se,que);
     for(int k=0;k<s;k++)
       if (k==p) tab[j][k]=2000; else if (tab[j-1][k]!=2000) tab[j][k]=tab[j-1][k]; else tab[j][k]=maks(tab,j-1,s)+1;
     }
  cout<<"Case #"<<i+1<<": "<<maks(tab,j-1,s)<<endl;
  }
}
