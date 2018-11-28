#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char s[30];
int a[30];
int n;
int tn,cp;
int main(){
    int i,j,k;
    freopen("B.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&tn);
    for (cp=1;cp<=tn;cp++){
        scanf("%s",&s);
        n=strlen(s);  
        for (i=0;i<n;i++) a[i]=s[i]-'0';
        int m=-1,f=0;
        for (i=n-1;i>=0 && f==0;i--){
            if (m>a[i]){
               f=1;
               int mm=100;
               for (j=i+1;j<n;j++)
                   if (a[j]>a[i] && a[j]<mm) mm=a[j],k=j;
               int tmp;
               tmp=a[k];a[k]=a[i];a[i]=tmp;
               sort(a+i+1,a+n);
            }
            if (a[i]>m) m=a[i];
        }
        if (f==0){
           a[n++]=0;
           int mm=100;
           for (i=0;i<n;i++)
               if (a[i]>0 && a[i]<mm) mm=a[i],k=i;
           int tmp;
           tmp=a[0];a[0]=a[k];a[k]=tmp;
           sort(a+1,a+n);
        }
        printf("Case #%d: ",cp);
        for (i=0;i<n;i++) printf("%d",a[i]);printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
