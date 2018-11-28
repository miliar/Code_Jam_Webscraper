#include<cstdio>

int n,p,sum;
int M[1100];
int chk[1100];
int ton[1100];
bool chk2[1100];

void decr(int x){
	if(x >= n && x < 2*n){
		M[x-n+1]--;
		return;
	}
	decr(x*2);
	decr(x*2+1);
}

int process(){
	int i,j,t;
	for(i=0;i<n;i++) chk2[i] = true;
	while(true){
		for(i=0;i<n;i++) chk[i] = 0;
		for(i=1;i<=n;i++){
			if(M[i] == 0){
				t = (n + i - 1) / 2;
				while(t >= 1){
					chk[t] = -1;
					t /= 2;
				}
			}
			else{
				t = (n + i - 1) / 2;
				while(t >= 1){
					if(chk[t] == -1) break;
					chk[t]++;
					t /= 2;
				}
			}
		}
		double max = -1.0;
		double temp;
		int maxi;
		for(i=0;i<n;i++){
			if(chk[i] == -1) continue;
			if(chk2[i] == false) continue;
			temp = (double)ton[i] / (double)chk[i];
			if(max < temp){
				max = temp;
				maxi = i;
			}
		}
		if(max == -1.0) break;
		chk2[maxi] = false;
		sum -= ton[maxi];
		decr(maxi);
	}
	return sum;
}

int main(void){
	int i,j,k,T;
	int ans;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++){
		fscanf(fin,"%d",&p);
		n = 1 << p;
		for(j=1;j<=n;j++){
			fscanf(fin,"%d",&M[j]);
		}
		sum = 0;
		for(j=n;j>1;j/=2){
			for(k=j/2;k<j;k++){
				fscanf(fin,"%d",&ton[k]);
				sum = sum + ton[k];
			}
		}
		ans = process();
		fprintf(fout,"Case #%d: %d\n",i,ans);
	}
	fcloseall();
	return 0;
}