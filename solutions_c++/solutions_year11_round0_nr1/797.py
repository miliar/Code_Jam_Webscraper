#include <cstdio>
#include <cstdlib>

int main() {

freopen("A.in","r",stdin);
freopen("A.out","w",stdout);


int t;
scanf("%d",&t);


for (int j=0;j<t;j++)
	{
	int n;
	scanf("%d",&n);
	int pos1=1,pos2=1;
	int t1=0,t2=0;
	int tim=0;
	for (int i=0;i<n;i++) {
		int a;
		char c[2];
		scanf("%s %d",c,&a);
		int add;
//		printf("%s\n",c);
		if (c[0]=='O') {
			add=abs(pos1-a);
			pos1=a;
			t1+=add;
			if (t1<tim) t1=tim;
			t1++;
			tim=t1;
//			printf("pos1=%d\tpos2=%d\tt1=%d\tt2=%d\ttim=%d\n",pos1,pos2,t1,t2,tim);
			}
		else {
			add=abs(pos2-a);
			pos2=a;	
			t2+=add;
			if (t2<tim) t2=tim;
			t2++;
			tim=t2;

//			printf("pos1=%d\tpos2=%d\tt1=%d\tt2=%d\ttim=%d\n",pos1,pos2,t1,t2,tim);		
			}
		}
	printf("Case #%d: %d\n",j+1,tim);	
	}

return 0;

}
