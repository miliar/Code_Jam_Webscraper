#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
#define M 100
int num[M+5];

int main(){
	freopen("A-large.in","rb",stdin);
	freopen("A-large.out","wb",stdout);
	int ca,c=0,a,b,i,j;
	scanf("%d",&ca);
	while(ca--){
		c++;
		scanf("%d%d",&a,&b);
		memset(num,0,sizeof(num));

		int temp=b%(1<<a);
		int len=0;
		while(temp!=0){
			num[len]=temp%2;
			temp/=2;
			len++;
		}
		for(i=0;i<a;i++){
			if(num[i]==0)
				break;
		}
		if(i==a)
			printf("Case #%d: ON\n",c);
		else 
			printf("Case #%d: OFF\n",c);
	}
	return 0;
}