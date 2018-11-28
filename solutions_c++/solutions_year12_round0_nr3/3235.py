#include<cstdio>
#include<cstring>
#include<math.h>
using namespace std;
int main(){
	int i,j,T,t,a,b,n,p;
	char ch;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output1.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%d %d",&a,&b);
		if(a<10)
			printf("0\n");
		else{
			int n=(int)log10((double)b)+1;
			int con=(int )pow((double)10,(double)n);
			int sum=0;
			for(i=a;i<=b;i++){
				int tem1,tem2=a;
				p=10;
				while(1){
					tem1=i%p;
					tem2=i/p;
					if(tem2<=0)
						break;
					if(tem1*(con/p)+tem2>i && tem1*(con/p)+tem2<=b)
						sum++;
					p*=10;
				}
			}
			printf("%d\n",sum);
		}
	}
}