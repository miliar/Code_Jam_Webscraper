#include <stdio.h>
#define MAXINS 105

class Instruction {
	public:
		int id,x;
		Instruction() {}
		Instruction(int ii,int xi):id(ii),x(xi) {}
};

int ins,rc1,rc2;
Instruction r1[MAXINS],r2[MAXINS];

inline int abs(int x) { return x>=0?x:0-x; }
inline int max(int a,int b) { return a>b?a:b; }

inline int solve() {
	int i1,i2,last1,last2,t;
	last1=last2=0;
	i1=i2=1;
	while(i1<rc1||i2<rc2) {
		if(i2==rc2||i1<rc1&&r1[i1].id<r2[i2].id) {
			t=max(abs(r1[i1].x-r1[i1-1].x)+last1+1,last2+1);
			last1=t;
			i1++;
		} else {
			t=max(abs(r2[i2].x-r2[i2-1].x)+last2+1,last1+1);
			last2=t;
			i2++;
		}
	}
	return max(last1,last2);
}

int main(void)
{
	int i,t,x,casenum=1;
	char ch[5];
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&ins);
		rc1=rc2=1;
		r1[0]=r2[0]=Instruction(-1,1);
		for(i=0;i<ins;i++) {
			scanf("%s %d",ch,&x);
			if(ch[0]=='O') r1[rc1++]=Instruction(i,x);
			else r2[rc2++]=Instruction(i,x);
		}
		printf("Case #%d: %d\n",casenum++,solve());
	}
}
