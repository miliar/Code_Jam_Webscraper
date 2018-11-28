#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

int pow(int a, int b){
  int k  = 1;
  for(int i=0;i<b;i++)
    k *= a;
    
  return k;
}

using namespace std;

int main(){
  int t,a,b,count,dig,h,done[8],ctrl;
  scanf("%d", &t);
  for(int i=0;i<t;i++){
    scanf("%d %d", &a, &b);
    h=a;
    dig =0;
    count = 0;
    while(h/10){
      h /= 10;
      dig++;
    }
    for(int j=a;j<=b;j++){
      h = j;
      int m = 0;
      for(int l=0;l<dig;l++){
	h = h/10 + pow(10,dig)*(h%10);
	ctrl = 1;
	for(int k = 0;k<m;k++){
	  if(done[k] == h)
	    ctrl = 0;
	}
	if(h<=b && h>j && ctrl){
	  count++;
	  done[m++] = h;
	}
      }

      
    }
    printf("Case #%d: %d\n",i+1,count);
    
  }

}