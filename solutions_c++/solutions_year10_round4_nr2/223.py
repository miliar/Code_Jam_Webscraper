#include<cstdio>
int ZZZ,tmp,cnt,m[10000],P;

void whh(int f,int t){
	bool b = false;
	for (int i=f;i<=t && !b;++i) if (m[i]>0) b=true;
	if (b==true){
		++cnt;
		for (int i=f;i<=t;++i) if (m[i]>0) --m[i];
	}
	int m = (f+t)/2;
	if (f!=t){
		whh(f,m);
		whh(m+1,t);
	}
}

int main(){
	scanf("%d",&ZZZ);
	for (int z=1;z<=ZZZ;++z){
		scanf("%d",&P);
		tmp = (1<<P);
		for (int i=0;i<tmp;++i){
			scanf("%d",&m[i]);
			m[i] = P-m[i];
		}
		int k;
		for (int i=1;i<tmp;++i) scanf("%d",&k);
		cnt = 0;
		whh(0,tmp-1);
		printf("Case #%d: %d\n",z,cnt);
	}
	
	return 0;
}
