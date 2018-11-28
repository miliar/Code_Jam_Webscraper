#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
#define M 1000
struct line{
	int x,y;
} sou[M+5];

int main(){
	freopen("A-large.in","rb",stdin);
	freopen("A-large.out","wb",stdout);
	int ca,c=0,n,i,j;
	scanf("%d",&ca);
	while(ca--){
		c++;

		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d",&sou[i].x,&sou[i].y);

		int res=0;
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				if(((sou[i].x>sou[j].x)&&(sou[i].y<sou[j].y))||((sou[i].x<sou[j].x)&&(sou[i].y>sou[j].y)))
					res++;
			}
		}
		printf("Case #%d: %d\n",c,res);
		
	}
	//system("pause");
	return 0;
}