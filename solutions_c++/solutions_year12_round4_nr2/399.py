#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

struct tp
{
       int x,y,r,id;
}a[10007] ;
int n,w,l,T;
int buff,Test;
int xx[10007],yy[10007];

bool cmp(const tp &a , const tp &b)
{
     return a.r>b.r ;
}

int det(int X1,int Y1,int X2,int Y2)
{
	return X1*Y2-X2*Y1;
}

int main()
{
	freopen("input.txt","r",stdin);
	
	scanf("%d",&Test);
	
	for (int T=1;T<=Test;++T){
	        printf("Case #%d: ",T);
			scanf("%d%d%d",&n,&w,&l);
          	memset(a,0,sizeof(a)) ;

	        buff=0;
	        if (w<l){
	        	swap(w,l);
				buff=1;
	        }   
	        for (int i=1;i<=n;++i){
	        	scanf("%d",&a[i].r) ;
	        	a[i].id=i;
	        }
            	sort(a+1,a+n+1,cmp);
          	int nextx=0,currx=0,curry=0;
          	for (int i=1;i<=n;++i){
	              	if (curry==0) nextx+=a[i].r;
		        a[i].y=curry;
	              	a[i].x=currx; 
	              	curry+=a[i].r+a[i+1].r;
	
	              	if (curry>l){
	                      nextx+=a[i+1].r;
	                      currx=nextx;
	                      curry=0;	                      
	              	}
           	}
           	for (int i=1;i<=n;i++){
			xx[a[i].id]=a[i].x;
			yy[a[i].id]=a[i].y;
			if (buff==1) swap(xx[a[i].id],yy[a[i].id]);
		}

            	for (int i=1;i<=n;i++) printf("%d.0 %d.0%c",xx[i],yy[i],i<n ? ' ':'\n') ;
	}
	return 0;
}
