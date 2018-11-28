#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;
typedef long long i64;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T, cas=0; scanf("%d", &T);
  int p[110];
  char c[110];
  while(T--){
	 cas++;
	 int n; 
	 memset(p, 0, sizeof(p));
	 memset(c, 0, sizeof(c));
	 scanf("%d", &n);
	 for(int i=0; i<n; i++)	 
	   scanf("%s %d", c+i, &p[i]);
     int i, tim=0, spend=0, po=1, pb=1, col=0, ans=0;
     int fo=0, fb=0;
     if(c[tim]=='O')
       col=0;
     else
       col=1;
	 for(tim=0; tim<n; tim++){
		  if(c[tim]=='O'){
		    if(col==0){
				ans+=abs(p[tim]-po);
				spend=spend+abs(p[tim]-po);
			}
			else{
			  int tmp=abs(p[tim]-po);	 
              if(tmp>spend){
 				spend=tmp-spend;
				if(fo==0){
					ans=ans>tmp?ans:tmp;
				}
				else
 					ans+=spend;
			  }
			  else
			    spend=0;
		    }
			po=p[tim];				  
			col=0;
			ans++;
			spend++;
			fo=1;
		  }
		  else if(c[tim]=='B'){
	        if(col==0){
			  int tmp = abs(p[tim]-pb);
			  if(tmp>spend){
				  spend=tmp-spend;
				  if(fb==0){
					  ans=ans>tmp?ans:tmp;
				  }
				  else
					ans+=spend;	
			    
			  }
			  else{
			    spend=0;
			  }
	        }
	        else{
				ans+=abs(p[tim]-pb);
				spend=spend+abs(p[tim]-pb);
		    }
		    pb=p[tim];
	        col=1;
			ans++;
			spend++;
			fb=1;
	      }	 
		//  printf("tim %d ans %d\n",tim, ans);		 
	 }	
	 printf("Case #%d: %d\n", cas, ans);
  }
  while(1);
  system("pause");
  return 0;
}
