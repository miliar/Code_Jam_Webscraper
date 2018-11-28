#include <string>
#include <fstream>
#include <sstream>
#include <iostream>
using namespace std;

int main()
{
  int n,m,q,mn;
  int mat[1001][100];
  string line;
  string se[100], qu[1001];
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");
  getline(fin,line);
  {
    istringstream ifstr(line);
    ifstr>>n;
  }
  for(int i=1;i<=n;i++)
  {
    cout << i << endl;
    fin>>m;
    getline(fin,line);
    {
      istringstream ifstr(line);
      ifstr>>m; 
    }
    for(int j=0;j<m;j++)
      getline(fin, se[j]);
    getline(fin,line);
    {
      istringstream ifstr(line);
      ifstr>>q; 
    }
    qu[0]="";
    for(int j=1;j<=q;j++)
      getline(fin,qu[j]);
    if(q==0)
    {
      fout << "Case #" << i << ": " << 0 << endl;
      continue; 
    }
    for(int j=q;j>=0;j--)
      if(j==q)
      {
        for(int k=0;k<m;k++)
          if(qu[j]!=se[k]) mat[j][k]=0;
          else             mat[j][k]=-1;
      }
      else if(j>=0)
      {
        mn=1000000;
        for(int k=0;k<m;k++)
          if(mat[j+1][k]!=-1)
          { 
            mat[j][k]=mat[j+1][k];
            if(mat[j+1][k]<mn) mn=mat[j+1][k];
          }
        for(int k=0;k<m;k++)
          if(mat[j+1][k]==-1)
            mat[j][k]=mn+1;
        for(int k=0;k<m;k++)
          if(qu[j]==se[k]) mat[j][k]=-1;
        if(j==0)
        {
          mn=1000000;
          for(int k=0;k<m;k++)
            if(mat[j][k]<mn) mn=mat[j][k];
          fout << "Case #" << i << ": " << mn << endl;
        }
      }
    /*for(int j=0;j<=q;j++)
    {
      for(int k=0;k<m;k++)
        cout << mat[j][k] << " ";
      cout << endl;
    }
    cout << endl;*/
  }
  fin.close();
  fout.close();
  return(0);
}