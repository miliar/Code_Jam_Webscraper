#include <stdio.h>
#include <algorithm>

using namespace std;

int a,x,y,i,j,p,mx,b,lim1,lim2,arr[105];

int main() {

   scanf("%d",&y);

  for(x=0; x<y; x++){


   scanf("%d %d %d",&j,&a,&p);

   for(i=0; i<j; i++) {

     scanf("%d",&arr[i]);

   }


   sort(arr,arr+j);

   lim1 =( p *3 ) -2;
   lim2 =( p + ((p-2)*2));

   if(lim1 < 0) { lim1 = p; }
   if(lim2 < 0) { lim2 = p; }



   mx = 0;

   for(i=j-1; i>=0; i--) {

     if(arr[i] >= lim1) {

        mx ++;

     }
     else{


      if(arr[i]>=lim2 && a > 0) {

        mx++;
        a--;

      }

     }
   }


     printf("Case #%d: %d\n",x+1,mx);

    }

return 0;
}
