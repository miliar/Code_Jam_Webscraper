#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int t1,t2,A,B,b,test,n,testcase;
char s[5];

int abs(int x){
	if (x<0) return -x;
	return x;
}
void work(int &pos,int &t,int time){
	int tmp=abs(pos-b);
	t+=tmp;
	if (t<time) t=time;
	t++;
	pos=b;
}
int main(){
//	freopen("i.txt","r",stdin);
	testcase=1;
	for (scanf("%d",&test);test--;testcase++){
		scanf("%d",&n);
		A=B=1;
		t1=t2=0;
		printf("Case #%d: ",testcase);
		for (int i=1;i<=n;i++){
			scanf("%s%d",s,&b);
			if (s[0]=='O') work(A,t1,max(t1,t2));
				else work(B,t2,max(t1,t2));
		}
		printf("%d\n",max(t1,t2));
	}
	return 0;
}
