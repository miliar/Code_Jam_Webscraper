#include<cstdio>

int round, limit, n;
int group[1000];
int chk[1000][1000];
__int64 que[1000010];

__int64 proc(){
	int i,j;
	int p = 0;
	int t;
	__int64 tot = 0;
	int cnt = 1;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			chk[i][j] = -1;
		}
	}
	while(true){
		__int64 sum = 0;
		t = p;
		while(true){
			sum += group[p];
			if(sum > limit){
				break;
			}
			p++;
			if(p >= n) p = 0;
			if(t == p) break;
		}
		if(sum > limit) sum -= group[p];
		p--;
		if(p < 0) p = n-1;

		if(chk[t][p] != -1){
			__int64 ccnt = cnt - chk[t][p];
			__int64 rest = round - cnt + 1;
			__int64 rep = rest / ccnt;
			__int64 remain = rest % ccnt;

			__int64 accum = 0;
			for(i=chk[t][p];i<cnt;i++){
				accum += que[i];
				if(i - chk[t][p] + 1 == remain){
					tot += accum;
				}
			}
			tot += rep * accum;
			break;
		}
		
		tot += sum;
		chk[t][p] = cnt;
		que[cnt++] = sum;
		if(cnt > round){
			break;
		}		
		p++;
		if(p >= n) p = 0;
	}
	return tot;
}

int main(void){
	int i,j,T;
	int ans;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(i=1;i<=T;i++){
		fscanf(fin,"%d %d %d",&round, &limit, &n);
		for(j=0;j<n;j++){
			fscanf(fin,"%d",&group[j]);
		}
		ans = proc();
		fprintf(fout,"Case #%d: %d\n",i,ans);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}