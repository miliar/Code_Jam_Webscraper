#include <cstdio>
#include <cstring>
using namespace std;

int C,n;
char bl[10],ch;
int a[100];

int main() {
  scanf("%d",&C);
  for (int c=1;c<=C;c++) {
    scanf("%d",&n);
    gets(bl);
    memset(a,0,sizeof(a));
    for (int i=1;i<=n;i++) {
      for (int j=1;j<=n;j++) {
	scanf("%c",&ch);
	if (ch=='1') a[i]=j;
      }
      gets(bl);
    }
    int ans=0;
    for (int i=1;i<=n;i++) {
      for (int j=i;j<=n;j++) {
	if (a[j]<=i) {
	  for (int k=j;k>=i+1;k--) {
	    int tmp=a[k];a[k]=a[k-1];a[k-1]=tmp;
	    ans++;
	  }
	  break;
	}
      }
    }
    printf("Case #%d: %d\n",c,ans);
  }
}
