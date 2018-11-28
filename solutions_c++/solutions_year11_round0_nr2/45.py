#include<cstdio>
#include<cstring>

const char table[]="QWERASDF";
int elbat[128];

int merge[8][8];
bool hate[8][8];

int lst[128],siz,cnt[8];

void clear() {
	siz=0;
	memset(cnt,0,sizeof(cnt));
}

void solve() {
	int n,i,j; char c;
	clear();
	scanf("%d",&n);
	while(n--) {
		scanf(" %c",&c);
		i=elbat[c];
		if(siz>=1&&lst[siz-1]<8&&merge[lst[siz-1]][i]>=0) {
			cnt[lst[siz-1]]--;
			lst[siz-1]=merge[lst[siz-1]][i];
			continue;
		}
		for(j=0;j<8;j++)if(hate[i][j]&&cnt[j]!=0)break;
		if(j<8){clear();continue;}
		lst[siz++]=i;
		cnt[i]++;
	}
	// output
	for(i=0;i<siz;i++) {
		if(i) {
			putchar(',');
			putchar(' ');
		}
		putchar(lst[i]<8?table[lst[i]]:lst[i]);
	}
}

void input() {
	int n; char a,b,c;
	memset(merge,0xff,sizeof(merge));
	memset(hate,0,sizeof(hate));
	scanf("%d",&n);
	while(n--) {
		scanf(" %c %c %c",&a,&b,&c);
		merge[elbat[a]][elbat[b]]=c;
		merge[elbat[b]][elbat[a]]=c;
	}
	scanf("%d",&n);
	while(n--) {
		scanf(" %c %c",&a,&b);
		hate[elbat[a]][elbat[b]]=true;
		hate[elbat[b]][elbat[a]]=true;
	}
}

int main() {
	int T,i;
	memset(elbat,0xff,sizeof(elbat));
	for(i=0;i<8;i++)elbat[table[i]]=i;
	scanf("%d",&T);
	for(i=1;i<=T;i++) {
		input();
		printf("Case #%d: [",i);
		solve();
		puts("]");
	}
	return 0;
}
