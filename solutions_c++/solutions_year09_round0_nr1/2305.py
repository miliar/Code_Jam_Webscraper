#include <iostream.h>
#include <cstdio>
using namespace std;
string s[6000];
int main()
{
 freopen("fj.in","r",stdin);
 freopen("fj.out","w",stdout);
 int l,d,n;
 scanf("%d%d%d",&l,&d,&n);
 char a[5000];
 int dq[30][256]; 
 for (int i=0; i<d; i++) { scanf("%s",a); s[i]=a;};
 for (int t=0; t<n; t++)
 {
   scanf("%s",&a);
   memset(dq,0,sizeof(dq));
   int i=0,z=0;
   int res=0,c=0;
   c=1;
   do
   {
   if (a[i]=='(') { i++;  while (a[i]!=')') { dq[z][a[i]]=1; i++; }       }
   else dq[z][a[i]]=1; 
   i++; z++;
   }
   while (i<strlen(a));
   for (int dt=0; dt<d; dt++)
   { c=1;
    for (int j=0; j<l; j++)
    {
     c*=dq[j][s[dt][j]];
    }
   // if (c && (t==7)) cout<<s[dt]<<endl;
    res+=c;
       
   }
   printf("Case #%d:  %d\n",t+1,res);
 }
}
