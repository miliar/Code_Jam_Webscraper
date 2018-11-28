#include<cstdio>
#include<algorithm>
using namespace std;

struct word{
	int len , f[26], id;
	void init(){
		len = 0;
		for (int i=0;i<26;++i) f[i] = 0;
	}
}a[10005];

int Z,N,M;
char w[30],hi[10005][13];

bool cmp(word a,word b){
	if (a.len!=b.len){
		return a.len < b.len;
	}
	
	for (int i=0;i<26;++i){
		if (a.f[w[i]-'a']!=b.f[w[i]-'a']) return a.f[w[i]-'a']<b.f[w[i]-'a'];
	}
	
	return true;
}

int ans;
int ansid;
int tmpid;

void guess(int l, int r,int p,int wrong){
	//printf("check %d %d %d %d\n",l,r,p,wrong);
	if (l==r){
		if (wrong>ans || (wrong==ans && ansid>a[l].id)){
			ans = wrong;
			ansid = a[l].id;
		}
		return;
	}

	int pre = l;
	for (int i = l+1;i<=r+1;++i){
		if (i<=r && a[i].f[w[p]-'a'] == a[i-1].f[w[p]-'a']){
			
		}else{
			if (i==r+1 && pre==l){
				guess(pre,i-1,p+1,wrong);
			}else{
				if (a[pre].f[w[p]-'a']==0){
					guess(pre,i-1,p+1,wrong+1);
				}else{
					guess(pre,i-1,p+1,wrong);
				}
			}
			pre = i;
		}
	}
}

int main(){
	scanf("%d",&Z);
	for (int z=1;z<=Z;++z){
		scanf("%d%d",&N,&M);
		for (int i=0;i<N;++i){
			scanf("%s",hi[i]);
			a[i].init();
			a[i].id = i;
			
			for (int j=0;hi[i][j];++j){
				++a[i].len;
				for (int k=0;k<26;++k){
					a[i].f[k] *= 2;
				}
				a[i].f[hi[i][j]-'a']++;
			}
		}
		
		printf("Case #%d:",z);
		
		a[N].init();
		
		for (int i=0;i<M;++i){
			ans = -1;
			ansid = 0;
			tmpid;
			scanf("%s",w);
			sort(a,a+N,cmp);
			
			int pre = 0;
			for (int i=1;i<=N;++i){
				if (a[i].len != a[i-1].len){
					guess(pre,i-1,0,0);
					pre = i;
				}
			}
			printf(" %s",hi[ansid]);
		}
		puts("");
	}

	return 0;
}
