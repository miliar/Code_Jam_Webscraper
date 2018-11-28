#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <math.h>
using namespace std;
char mat[1000][1000];
int D[1000][1000];
    int  n,m,d;
bool posible(int k,int _r, int _c,double cr,double cc)
{
     if( _r+k>=n || _c+k>=m ) return false;
	int ccc=0;
	double sumr=0,sumc=0;
	for(int r=_r;r<=_r+k;r++)
	for(int c=_c;c<=_c+k;c++)	
	{
		sumr+=(cr-r)*D[r][c];
		sumc+=(cc-c)*D[r][c];
		ccc++;
	}
	ccc-=4;
	sumr-=((cr-_r)*D[_r][_c]+(cr-_r)*D[_r][_c+k]+(cr-(_r+k))*D[_r+k][_c]+(cr-(_r+k))*D[_r+k][_c+k]);
	sumc-=((cc-_c)*D[_r][_c]+(cc-(_c+k))*D[_r][_c+k]+(cc-_c)*D[_r+k][_c]+(cc-(_c+k))*D[_r+k][_c+k]);
   
   if( fabs(sumr/(double)(ccc))<=1e-9 &&  fabs(sumc/(double)(ccc))<=1e-9) return true;
   
   return false;
	
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout); 
    
    int N;
    scanf("%d",&N);

    for(int _h=0;_h<N;_h++)
    {
       scanf("%d%d%d",&n,&m,&d);
       for(int r=0;r<n;r++)
        scanf("%s",mat[r]);
        
           for(int r=0;r<n;r++)       
            for(int c=0;c<m;c++)
             D[r][c]=d+(mat[r][c]-'0');        
        
       int res=-1;
       for(int k=1;k<=min(n,m);k++)
        {
           int sum=0;
           for(int r=0;r<n;r++)       
            for(int c=0;c<m;c++)
             {
               if(  posible(k,r,c,r+k/2.0,c+k/2.0) )  
                 res=k;
             }
        }
       if(res!=-1)
         printf("Case #%d: %d\n",_h+1,res+1);
       else
        printf("Case #%d: impossible\n",_h+1);
    }
    
    return 0;   
}
