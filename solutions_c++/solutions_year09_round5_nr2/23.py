#include<cstdio>

const int MD = 10009;

int words[105][26];

//int w[11];

char p[5];
int sp;

int cw[105][5];

int csum[5];

int wyn[51];

int n;

int K;

void calc1(){
	for(int i=1;i<=n;i++) csum[0] = (csum[0] + cw[i][0]) % MD;
}

void calc2(){
	for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) if(i!=j) csum[0] = (csum[0] + cw[i][0] * cw[j][1])%MD;
	for(int i=1;i<=n;i++) csum[1] = (csum[1] + cw[i][0] * cw[i][1]) % MD;
}

void calc3(){
	for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) for(int k=1;k<=n;k++) if(i!=j && j!=k && k!=i) csum[0] = (csum[0] + cw[i][0] * cw[j][1] * cw[k][2]) % MD;
	for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) if(i!=j){
		csum[1] = (csum[1] + cw[i][0] * cw[j][1] * cw[j][2]) % MD;
		csum[1] = (csum[1] + cw[j][0] * cw[i][1] * cw[j][2]) % MD;
		csum[1] = (csum[1] + cw[j][0] * cw[j][1] * cw[i][2]) % MD;
	}
	for(int i=1;i<=n;i++) csum[2] = (csum[2] + cw[i][0] * cw[i][1] * cw[i][2]) % MD;
}

void calc4(){
	for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) for(int k=1;k<=n;k++) for(int l=1;l<=n;l++) if(i!=j && j!=k && k!=l && l!=i && k!=i && l!=j) csum[0] = (csum[0] + cw[i][0] * cw[j][1] * cw[k][2] * cw[l][3]) % MD;
	for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) if(i!=j){
		csum[1] = (csum[1] + cw[i][0] * cw[j][1] * cw[j][2] * cw[j][3]) % MD;
		csum[1] = (csum[1] + cw[j][0] * cw[i][1] * cw[j][2] * cw[j][3]) % MD;
		csum[1] = (csum[1] + cw[j][0] * cw[j][1] * cw[i][2] * cw[j][3]) % MD;
		csum[1] = (csum[1] + cw[j][0] * cw[j][1] * cw[j][2] * cw[i][3]) % MD;
	}
	for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) for(int k=1;k<=n;k++) if(i!=j && j!=k && k!=i){
		csum[2] = (csum[2] + cw[i][0] * cw[j][1] * cw[k][2] * cw[k][3]) % MD;
		csum[2] = (csum[2] + cw[i][0] * cw[k][1] * cw[k][2] * cw[j][3]) % MD;
		csum[2] = (csum[2] + cw[k][0] * cw[i][1] * cw[k][2] * cw[j][3]) % MD;
		csum[2] = (csum[2] + cw[k][0] * cw[k][1] * cw[i][2] * cw[j][3]) % MD;
		csum[2] = (csum[2] + cw[k][0] * cw[i][1] * cw[j][2] * cw[k][3]) % MD;
		csum[2] = (csum[2] + cw[i][0] * cw[k][1] * cw[j][2] * cw[k][3]) % MD;
	}
	for(int i=1;i<=n;i++) for(int j=1;j<=n;j++) if(i!=j){
		csum[3] = (csum[3] + cw[i][0] * cw[i][1] * cw[j][2] * cw[j][3]) % MD;
		csum[3] = (csum[3] + cw[i][0] * cw[j][1] * cw[i][2] * cw[j][3]) % MD;
		csum[3] = (csum[3] + cw[i][0] * cw[j][1] * cw[j][2] * cw[i][3]) % MD;
	}
	for(int i=1;i<=n;i++){
		csum[4] = (csum[4] + cw[i][0] * cw[i][1] * cw[i][2] * cw[i][3]) % MD;
	}

}

int c[105];

int f[105];
int of[105];

int po(int a,int b){
	int w = 1;
	for(;b>0;b>>=1){
		if(b&1) w = (w*a) % MD;
		a = (a*a) % MD;
	}
	return w;
}

int cnt[11][5][5];

int cprz[] = {0,1,2,3,5};

void calc_p(){
	for(int i=0;i<sp;i++){
		for(int j=1;j<=n;j++){
			cw[j][i] = words[j][p[i]-'a'];
		}
	}
	for(int i=0;i<=4;i++) csum[i] = 0;
	if(sp == 1) calc1();
	else if(sp == 2) calc2();
	else if(sp == 3) calc3();
	else calc4();
	for(int k=1;k<=K;k++){
		for(int i=0;i<cprz[sp];i++){
			wyn[k] = (wyn[k] + cnt[k][sp][i] * csum[i]) % MD;
		}
	}
}

int cperm(int a,int b,int c,int d){
	return (((((f[a+b+c+d] * of[a]) % MD) * of[b])%MD * of[c])%MD * of[d])%MD;
}

int bin(int n,int k){
	if(k > n) return 0;
	return ((f[n] * of[n-k])%MD * of[k])%MD;
}

char inpoly[55];

char buf[55];

void alg(){
	scanf("%s%d%d",inpoly,&K,&n);
	for(int k=1;k<=K;k++){
		for(int i=1;i<=4;i++){
			if(i == 4){
				int w = 0;
				for(int a = 0; a <= k; a++){
					for(int b = 0; b <= k-a; b++){
						for(int c = 0; c <= k-a-b; c++){
							for(int d = 0; d <= k-a-b-c; d++){
								int cnt = po(n-4,k-a-b-c-d);
								cnt = ((bin(k,a+b+c+d) * cperm(a,b,c,d))%MD * cnt)%MD;
								cnt = ((((cnt * a)%MD*b)%MD*c)%MD*d)%MD;
								w = (w + cnt) % MD;
							}
						}
					}
				}
				cnt[k][i][0] = w;
				w = 0;
				for(int a = 0; a <= k; a++){
					for(int b = 0; b <= k-a; b++){
						int cnt = po(n-2,k-a-b);
						cnt = ((bin(k,a+b) * cperm(a,b,0,0))%MD * cnt)%MD;
						cnt = ((((cnt * a)%MD*b)%MD*a)%MD*a)%MD;
						w = (w + cnt) % MD;
					}
				}
				cnt[k][i][1] = w;
				w = 0;
				for(int a = 0; a <= k; a++){
					for(int b = 0; b <= k-a; b++){
						for(int c = 0; c <= k-a-b; c++){
							int cnt = po(n-3,k-a-b-c);
							cnt = ((bin(k,a+b+c) * cperm(a,b,c,0))%MD * cnt)%MD;
							cnt = ((((cnt * a)%MD*b)%MD*c)%MD*a)%MD;
							w = (w + cnt) % MD;
						}
					}
				}
				cnt[k][i][2] = w;
				w = 0;
				for(int a = 0; a <= k; a++){
					for(int b = 0; b <= k-a; b++){
						int cnt = po(n-2,k-a-b);
						cnt = ((bin(k,a+b) * cperm(a,b,0,0))%MD * cnt)%MD;
						cnt = ((((cnt * a)%MD*b)%MD*b)%MD*a)%MD;
						w = (w + cnt) % MD;
					}
				}
				cnt[k][i][3] = w;
				w = 0;
				for(int a = 0; a <= k; a++){
					int cnt = po(n-1,k-a);
					cnt = ((bin(k,a) * cperm(a,0,0,0))%MD * cnt)%MD;
					cnt = ((((cnt * a)%MD*a)%MD*a)%MD*a)%MD;
					w = (w + cnt) % MD;
				}
				cnt[k][i][4] = w;
			}else if(i==3){
				int w = 0;
				for(int a = 0; a <= k; a++){
					for(int b = 0; b <= k-a; b++){
						for(int c = 0; c <= k-a-b; c++){
							int cnt = po(n-3,k-a-b-c);
							cnt = ((bin(k,a+b+c) * cperm(a,b,c,0))%MD * cnt)%MD;
							cnt = (((cnt * a)%MD*b)%MD*c)%MD;
							w = (w + cnt) % MD;
						}
					}
				}
				cnt[k][i][0] = w;
				w = 0;
				for(int a = 0; a <= k; a++){
					for(int b = 0; b <= k-a; b++){
						int cnt = po(n-2,k-a-b);
						cnt = ((bin(k,a+b) * cperm(a,b,0,0))%MD * cnt)%MD;
						cnt = (((cnt * a)%MD*b)%MD*b)%MD;
						w = (w + cnt) % MD;
					}
				}
				cnt[k][i][1] = w;
				w = 0;
				for(int a = 0; a <= k; a++){
					int cnt = po(n-1,k-a);
					cnt = ((bin(k,a) * cperm(a,0,0,0))%MD * cnt)%MD;
					cnt = (((cnt * a)%MD*a)%MD*a)%MD;
					w = (w + cnt) % MD;
				}
				cnt[k][i][2] = w;
			}else if(i==2){
				int w = 0;
				for(int a = 0; a <= k; a++){
					for(int b = 0; b <= k-a; b++){
						int cnt = po(n-2,k-a-b);
						cnt = ((bin(k,a+b) * cperm(a,b,0,0))%MD * cnt)%MD;
						cnt = ((cnt * a)%MD*b)%MD;
						w = (w + cnt) % MD;
					}
				}
				cnt[k][i][0] = w;
				w = 0;
				for(int a = 0; a <= k; a++){
					int cnt = po(n-1,k-a);
					cnt = ((bin(k,a) * cperm(a,0,0,0))%MD * cnt)%MD;
					cnt = ((cnt * a)%MD*a)%MD;
					w = (w + cnt) % MD;
				}
				cnt[k][i][1] = w;
			}else if(i==1){
				int w = 0;
				for(int a = 0; a <= k; a++){
					int cnt = po(n-1,k-a);
					cnt = ((bin(k,a) * cperm(a,0,0,0))%MD * cnt)%MD;
					cnt = (cnt * a)%MD;
					w = (w + cnt) % MD;
				}
				cnt[k][i][0] = w;
			}
		}
	}
	for(int i=1;i<=n;i++){
		scanf("%s",buf);
		for(int j=0;j<26;j++) words[i][j] = 0;
		for(int j=0;buf[j];++j) ++words[i][buf[j]-'a'];
	}
	for(int i=1;i<=K;i++) wyn[i] = 0;
	for(int i=0;inpoly[i];){
		if(inpoly[i] == '+') ++i;
		sp = 0;
		while(inpoly[i+sp] >= 'a' && inpoly[i+sp] <= 'z'){
			p[sp] = inpoly[i+sp];
			++sp;
		}
		calc_p();
		i += sp;
	}
	for(int i=1;i<=K;i++) printf(" %d",wyn[i]);
	printf("\n");
}


int main(){
	f[0] = 1;
	for(int i=1;i<=100;i++) f[i] = (f[i-1] * i)%MD;
	for(int i=0;i<=100;i++) of[i] = po(f[i],MD-2);
	int d;
	scanf("%d",&d);
	for(int i=1;i<=d;i++){
		printf("Case #%d:",i);
		alg();
	}
}
