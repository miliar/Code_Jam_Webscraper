#include <iostream>
using namespace std;

int mat[50][50];
int N,M;
int len[50],cnt[50];
int mk[50][50];

int change(char c) {
	if(c >= '0' && c <= '9') return c - '0';
	else return c - 'A' + 10;
}

void tuse(int x,int y,int ll) {
	for(int i = 0;i < ll;++i) {
		for(int j = 0;j < ll;++j) {
			mk[x+i][y+j] = 1;
		}
	}
}

int check(int x,int y,int ll) {
	int now = !mat[x][y];
	for(int i = 0;i < ll;++i) {
		now = !now;
		int cnt = now;
		for(int j = 0;j < ll;++j) {
			cnt = !cnt;
			if(x + i >= M)return 0;
			if(y + j >= N)return 0;
			if(mk[x+i][y+j]) return 0;
			if(mat[x+i][y+j] == !cnt) {
				continue;
			} else return 0;
		}
	}
	return true;	
}

int get_dp(int &vv) {
	vv=0;
	int maxlen = 0;
	for(int i = min(N,M);i >= 1;--i) {
		if(maxlen)break;
		for(int j = 0;j < M;++j) {
			if(maxlen)break;
			for(int k = 0;k < N;++k) {
				if(mk[j][k])continue;
				if(check(j,k,i)) {
					maxlen = i;
					break;
				}
			}
		}
	}
	for(int i = 0;i < M;++i) {
		for(int j = 0;j < N;++j) {
			if(mk[i][j])continue;
			if(check(i,j,maxlen)) {
				tuse(i,j,maxlen);
				vv++;
			}
		}
	}		
	return maxlen;		
}

int solve() {
	memset(mk,0,sizeof(mk));
	memset(cnt,0,sizeof(cnt));
	int ret = 0;
	while(true) {
		int maxlen = get_dp(cnt[ret]);
		if(maxlen == 0)break;
	//	cout << maxlen << " " << cnt[ret] << endl;
		len[ret++] = maxlen;
		if(maxlen == 1)break;
	}
	return ret;
}

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T, cas = 1;
	scanf("%d",&T);
	while(T--) {
		memset(mat, 0, sizeof(mat));
		scanf("%d%d",&M,&N);
		for(int i = 0;i < M;++i) {
			char str[50];
			scanf("%s",str);
			for(int j = 0;j < N / 4;++j) {
				for(int k = 3;k >= 0; --k) {
					if(j * 4 + (3-k) >= N) continue;
					mat[i][j*4+(3-k)] = ((change(str[j]))&(1<<k))>>k;
				}		
			}
		}
		int ret = solve();
		printf("Case #%d: %d\n",cas++, ret);
		for(int i = 0;i < ret;++i) {
			printf("%d %d\n", len[i], cnt[i]);
		}
	}	
	return 0;
}
