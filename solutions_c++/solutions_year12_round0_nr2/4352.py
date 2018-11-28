/*
Vikas.kumar_vkx
*/
#include <iostream>
using namespace std;

int main() {

int n=3;
int s=1;
int m=5;
int a[101],temp=0;
int count=0;n=6;s=2;m=8;
int tt=0;

    int T; scanf("%d",&T); 
	while (T--) {tt++;count=0;
                    scanf("%d %d %d",&n,&s,&m);
                    for(int i=0;i<n;i++){
                    scanf("%d",&a[i]);
                    temp=(m<2)?1:(m-1)*3+1;
                    if(a[i]>=temp)count++;
                    else if(s&&(temp-1) && (((temp-1)==a[i])|| ((temp-2)==a[i]))){count++;s--;}
                    }
                    if(m==0)count=n;
                    printf("Case #%d: %d\n",tt,count);

        }                    scanf("%d",&n);
}
