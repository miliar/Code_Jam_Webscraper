#include<string>
#include<algorithm>
using namespace std;
int main(){
  //  freopen("1.in","r",stdin);
  //  freopen("4.txt","w",stdout);
   char str[1010];
   char m1[6]={1,2,3,4,5,6},m2[1010];
   int a,n,i,k,l,j,min,tot;
   scanf("%d",&n);
   for(a=1;a<=n;a++)
   {
       scanf("%d%s",&k, str);
       l = strlen(str);
       min=2000000;
       do{
            for(j=0;j<l/k;j++){
            for(i=0;i<k;i++)
            {
                m2[i+j*k]=str[(m1[i]-1)+j*k];
            }
            }

           tot=1;
           for(i=1;i<l;i++)
           {
               if(m2[i]!=m2[i-1])tot++;
           }
           if(tot<min)min=tot;
       }while(next_permutation(m1,m1+k));
       printf("Case #%d: %d\n",a,min);
   }
}
