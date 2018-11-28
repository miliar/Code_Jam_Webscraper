#include <cstdio>
using namespace std;

int len(int a,int b) {if(a>b) return a-b; else return b-a;}
int antimin(int x) {if(x>0) return x; else return 0;}

int main(){
	int T; scanf("%d",&T);
	for (int tc = 1; tc <= T; tc += 1) {
		int n,tempatO=1,tempatB=1,waktuO=0,waktuB=0,hasil=0;
		scanf("%d",&n);
		for (int i = 0; i < n; i += 1) {
			int d; char bot; scanf("%s %d",&bot,&d);
			if(bot=='O'){
				waktuB += antimin(len(d,tempatO)-waktuO)+1;
				hasil += antimin(len(d,tempatO)-waktuO)+1;
				tempatO=d; waktuO=0;
			} else if(bot=='B'){
				waktuO += antimin(len(d,tempatB)-waktuB)+1;
				hasil += antimin(len(d,tempatB)-waktuB)+1;
				tempatB=d; waktuB=0;
			}
			//printf("%d O:%d %d B:%d %d\n",hasil,tempatO,waktuO,tempatB,waktuB);
		}
		printf("Case #%d: %d\n",tc,hasil);
	}
}
