#include<iostream>

using namespace std;

int main(){   
   freopen("Download A-small.in","r",stdin);  freopen("outut.txt","w",stdout);
    
    int t,Case=1;scanf("%d",&t);
    while(t--){
      int n,k;scanf("%d %d",&n,&k);
      int c=1;
      while( n--) c*=2;
      k=k%c;        
      printf("Case #%d: ",Case);  
      if( k!=c-1 ) printf("OFF\n");
      else printf("ON\n");    
      Case++;
    }
       
}
