#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;

int a[1000],b[1000];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,col;
    scanf("%d",&t);
    for (int j = 0; j < t; j++) {
     col=0;
     scanf("%d",&n);
     for (int i = 0; i < n; i++) scanf("%d%d",&a[i],&b[i]);
     for (int i = 0; i < n; i++)
      for (int k = i+1; k < n; k++){
       if ((a[i]>a[k]&&b[i]<b[k])||(a[i]<a[k]&&b[i]>b[k])) col+=1;
      }
     printf("Case #%d: %d\n",j+1,col);
    }

    return 0;
}
