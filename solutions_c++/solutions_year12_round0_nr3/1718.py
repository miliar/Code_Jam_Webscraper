#include<cstdio>
#include<algorithm>
#include<math.h>
using namespace std;

int main(){
	int t,a,b,i,j,k,n,temp,count,len,la,lb,li,s,c,flag;
	scanf("%d",&t);
	j=0;
	while(j++<t){
		scanf("%d %d",&a,&b);
		count=0;s=0;
		for (i=a;i<=b;i++){
			li=log10(i);
			len=pow(10,li+1);
			int a[10]={0};
			c=0;
			while(li){
				temp=pow(10,li--);
				n=i%temp;
				n*=(len/temp);
				n+=i/temp;
				if(n<=b&&n>i) {
					flag=0;
					for(k=0;k<c;k++)
						if(n==a[k]) flag++;
					if(flag==0){
						a[c]=n;
						c++;
					//	printf("%d %d\n",i,n);
						count++;}
					}
			}
		}
		printf("Case #%d: %d\n",j,count);
	}
	return 0;
}
