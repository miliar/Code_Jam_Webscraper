#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;
int _N;
int mat[50][50];
pair <int,int> ar[32*32];
int h;
void encuentra(int a,int n, int m)
 {
    h=0;
   for(int r=0;r<=n-a;r++)
    for(int c=0;c<=m-a;c++)
     {
       bool valid=true;

       for(int j=0;j<a && valid;j++)
        for(  int k=0;k<a && valid;k++ )
         {
            if( mat[r+j][c+k]==-1 )
                valid=false;
            else{
              if(  r+j+1<r+a && mat[r+j+1][c+k]==mat[r+j][c+k] )   valid=false;
              if(  c+k+1<c+a && mat[r+j][c+k+1]==mat[r+j][c+k] )   valid=false;
              if(  r+j+1<r+a && c+k+1<c+a && mat[r+j+1][c+k+1]!=mat[r+j][c+k] )   valid=false;
            }
         }

       if( valid )
        ar[h++]=make_pair( r,c );

     }
 }
bool valido(int R, int C, int a)
 {
    for(int r=0;r<a;r++)
     for(int c=0;c<a;c++)
      if(  mat[R+r][C+c]==-1 )
       return false;
    return true;
 }
void llena(int R, int C, int a)
 {
    for(int r=0;r<a;r++)
     for(int c=0;c<a;c++)
      mat[R+r][C+c]=-1;

 }
int main()
{
 scanf("%d",&_N);
   for(int _r=0;_r<_N;_r++)
    {
       int n,m;
       vector < pair<int,int> > res;
       unsigned int a;
       scanf("%d%d",&n,&m);
       for(int r=0;r<n;r++)
        {
           scanf("%x",&a);
           for(int c=0;c<m;c++)
           {
            if( (a&(1<<(m-c-1))) )
             mat[r][c]=1;
            else
             mat[r][c]=0;
           }
        }

        for(int r=min(n,m);r>=1;r--)
         {
            encuentra(r,n,m);
            if( h )
             {
               int cont=0;
               sort(ar,ar+h);
               for(int c=0;c<h;c++)
                if(valido(ar[c].first,ar[c].second,r))
                 cont++,llena(ar[c].first,ar[c].second,r);
               if(cont)
                res.push_back( make_pair(r,cont) );
             }
         }
         printf("Case #%d: %d\n",_r+1,res.size());
         for(int r=0;r<res.size();r++)
          printf("%d %d\n",res[r].first,res[r].second);
    }
}
