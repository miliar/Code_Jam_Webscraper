#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int main(){
  int k,s,n,p,t[120],count;
  
  scanf("%d", &k);
  for(int i=0;i<k;i++){
    count = 0;
    scanf("%d %d %d", &n,&s,&p);
    for(int j=0;j<n;j++) scanf("%d", &t[j]);
    
    for(int j=0;j<n;j++){
      if(t[j]%3 == 1){
	if((t[j]/3+1)>=p)
	  count++;
      }else if(t[j]%3 == 0){
	if(t[j]/3>=p) count++;
	else if(t[j] == 0)
	  continue;
	else if(s && t[j]/3+1>=p){
	  s--;
	  count++;
	}
	
      }else{
	if(t[j]/3+1>=p) count++;
	else if(s && t[j]/3+t[j]%3>=p){
	  s--;
	  count++;
	}
	  
      }
      
    }
    printf("Case #%d: %d\n",i+1, count);
  }
}