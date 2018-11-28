#include <cstdio>

using namespace std;

const int maxlen=110;
int tr,n,t1,t2;
char chx[maxlen],chy[maxlen],chz[maxlen],chs[maxlen],cht[maxlen],q[maxlen];

int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	scanf("%d",&tr);
	for (int test=0;test<tr;test++){
		char ch;
		scanf("%d",&t1);
		for (int i=0;i<t1;i++)
			scanf("%c%c%c%c",&ch,&chx[i],&chy[i],&chz[i]);
		scanf("%d",&t2);
		for (int i=0;i<t2;i++)
			scanf("%c%c%c",&ch,&chs[i],&cht[i]);
		scanf("%d%c",&n,&ch);
		int top=0;
		for (int i=-0;i<n;i++){
			scanf("%c",&ch);
			bool flag=false;
			if (top>0)
				for (int i=0;i<t1;i++)
					if ((chx[i]==ch&&chy[i]==q[top-1])||(chx[i]==q[top-1]&&chy[i]==ch)){
						q[top-1]=chz[i];
						flag=true;
						break;
				}
			if (flag) continue;
			if (top>0)
				for (int i=0;i<t2;i++){
					for (int j=0;j<top;j++)
						if ((chs[i]==ch&&cht[i]==q[j])||(chs[i]==q[j]&&cht[i]==ch)){
							top=0;
							flag=true;
							break;
						}
					if (flag) break;
				}
			if (!flag) q[top++]=ch;
		}
		printf("Case #%d: [",test+1);
		for (int i=0;i<top;i++){
			printf("%c",q[i]);
			if (i!=top-1) printf(", ");
		}
		printf("]\n");
	}
	
	return 0;
}
