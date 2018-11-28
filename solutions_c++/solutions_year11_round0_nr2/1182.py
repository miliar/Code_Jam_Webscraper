#include<cstring>
#include<string>
#include<cstdio>
#include<algorithm>
using namespace std;

int l,n,m,test,testcase;
char A[50][5],B[50][5],list[105],str[105];

bool canCombine(char c1,char c2,char &c){
	for (int i=1;i<=n;i++) if (A[i][1]==c1 && A[i][2]==c2 || A[i][1]==c2 && A[i][2]==c1){
		c=A[i][3];
		return true;
	}
	return false;
}
bool oppose(char c1,char c2){
	for (int i=1;i<=m;i++) if (B[i][1]==c1 && B[i][2]==c2 || B[i][1]==c2 && B[i][2]==c1) return true;
	return false;
}
int main(){
	freopen("i.txt","r",stdin);
	testcase=1;
	for (scanf("%d",&test);test--;testcase++){
		scanf("%d",&n);
		printf("Case #%d: ",testcase);
		for (int i=1;i<=n;i++) scanf("%s",A[i]+1);
		l=0;
		scanf("%d",&m);
		for (int i=1;i<=m;i++) scanf("%s",B[i]+1);
		scanf("%d",&n);
		scanf("%s",str+1);
		for (int i=1;i<=n;i++){
			char c;
			if (l && canCombine(list[l],str[i],c)) list[l]=c;
			else{
				bool ok=true;
				for (int j=1;j<=l;j++) if (oppose(list[j],str[i])){
					l=0;
					ok=false;
					break;
				}
				if (ok) list[++l]=str[i];
			}
		}
		printf("[");
		for (int i=1;i<=l;i++){
			printf("%c",list[i]);
			if (i<l) printf(", ");
		}
		puts("]");
	}
	return 0;
}
