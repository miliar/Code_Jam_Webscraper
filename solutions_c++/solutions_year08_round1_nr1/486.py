#include<string>
#include<algorithm>
using namespace std;

int a[10],b[10];
int main(){
 //   freopen("1.txt","w",stdout);
   int i,t,n,min;
   scanf("%d",&t);
   int c=1;
   while(t--)
   {
        scanf("%d",&n);
        for(i=0;i<n;i++)scanf("%d",&a[i]);
        for(i=0;i<n;i++)scanf("%d",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        min = 0;
        for(i=0;i<n;i++)
        {
            min+=a[i]*b[n-i-1];
        }
        printf("Case #%d: %d\n",c++,min);
   }
}
