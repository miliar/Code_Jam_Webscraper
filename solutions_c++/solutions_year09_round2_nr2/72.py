#include <iostream>
#include <algorithm>
using namespace std;

int test,l,i,j,k,mn;
char a[25],tmp;
bool flag;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d\n",&test);
	for (int tt=1;tt<=test;++tt){
		scanf("%s\n",&a);
		l=strlen(a);
		flag=false;
		for (i=l-1;i;--i){
			if (a[i-1]<a[i]){
				mn=l-1;
				for (j=l-1;j>=i;--j)
					if ((a[j]<a[mn] && a[mn]>a[i-1])||(a[mn]<=a[i-1]))mn=j;
				tmp=a[i-1];a[i-1]=a[mn];a[mn]=tmp;
				flag=true;
				sort(a+i,a+l);
				break;
			};
		};
		mn=l-1;
		for (i=l-1;i>=0;--i)
			if ((a[mn]=='0') || (a[i]<a[mn] && a[i]>0))mn=i;
		if (!flag){
			tmp=a[0];a[0]=a[mn];a[mn]=tmp;
			for (i=l-1;i;--i)a[i+1]=a[i];
			++l;
			a[1]=48;
			sort(a+1,a+l);
		};
		printf("Case #%d: ",tt);
		for (i=0;i<l;++i)printf("%c",a[i]);
		printf("\n");
	};
};