using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

# define PI 3.14159265

int main() {
    int t,a,b,i,j,cnt,tmp1,tmp2,cs=0,c,ten,num;
    scanf("%d",&t);
    while(t--) {
         cs++;      
         scanf("%d %d",&a,&b);
         cnt=0;
         
         c=0;
         num=a;
         while(num!=0) {
                       num/=10;
                       c++;
         }
         ten=1;
         for(j=0;j<c-1;j++) ten*=10;
         //cout<<ten<<endl;
         
         for(i=a;i<=b;i++) {
                  num=i;
                  while(1) {
                           tmp1=num%10;
                           tmp2=num/10;
                           num=tmp1*ten+tmp2;
                           if(num<=b && num>=a && num>i) cnt++;
                           //cout<<num<<endl;
                           if(num==i) break;
                  }
         }
         
         printf("Case #%d: %d\n",cs,cnt);
    }
    return 0;
}
         
                  
                               
                        
                                         
