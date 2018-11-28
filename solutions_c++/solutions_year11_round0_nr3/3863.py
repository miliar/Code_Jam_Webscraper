#include <stdio.h>
#include <iostream>
#include <algorithm>

int many,Max;
int R[1005];

void input()
{
	scanf("%d",&many);
	for(int i=0;i<many;i++)
		scanf("%d",&R[i]);
}
void pro(int A,int B,int a,int b,int num)
{
	if(num == many){
		if(a == b && A != 0 && B != 0) {
			if(Max < A) Max = A;
			if(Max < B) Max = B;
		}
		return ;
	}
	pro(A+R[num],B,a^R[num],b,num+1);
	pro(A,B+R[num],a,b^R[num],num+1);
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int T,asdf = 1;
	scanf("%d",&T);
	while(T -- ){
		input();
		Max = -1;
		printf("Case #%d: ",asdf);
		pro(0,0,0,0,0);
		if(Max == -1) printf("NO\n");
		else printf("%d\n",Max);
		asdf ++ ;
	}
}