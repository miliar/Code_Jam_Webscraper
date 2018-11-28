#include <iostream>
#include <conio.h>
#include <cstdio>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
int mark[10000][100],dem;

bool check(int i,int k)
{
  if (mark[i][0]==0) mark[i][0]++;
  
  for (int j=1; j<=mark[i][0];j++)
     if (mark[i][j]==k) return false;
     
mark[i][0]++;
mark[i][mark[i][0]]=k;
return true;
}

void process(int x,int y)
{
bool ok;
char xau[200];
int L=x; int R=y;
    if (R>10)
    {
     if (L<=10)L=11;
     for (int i=L;i<=R;i++)
        {
           itoa (i,xau,10);
           string chuoi=xau;
           for (int j=1;j<=strlen(xau);j++)
           {
               string tmp=chuoi.substr(j,strlen(xau)-j+1)+chuoi.substr(0,j);
               int k=atoi(tmp.c_str());
               
               if ((tmp[0]!='0') &&(k<=R) && (k>=i) && (k!=i) && check(i,k))  dem++;
           }
        }
    }
}

int main(){
   	string fname = "C-small-attempt0"; 
	freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	int n=0,a,b; 
	cin>>n;
      for (int i=1; i<=n;i++)
      {
          cin>>a>>b;
          dem=0;         
          memset(mark, 0, sizeof(mark));
          process(a,b);
          cout<<"Case #"<<i<<": "<<dem<<"\n";
      }
}
