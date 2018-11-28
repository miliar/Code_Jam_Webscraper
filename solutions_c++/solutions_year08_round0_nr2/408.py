#include<cstdio>
#include<cstring>
#include<cstdlib>
//#include<conio.h>

int N, T, NA, NB, a[100][3], b[100][3], cnt, fa, fb;

int cmp(const void* a, const void*b){
	int *x=(int*)a, *y=(int*)b;
	if(x[0]==y[0]) return x[1]-y[1];
	return x[0]-y[0];
}

void doit(){ 
	int i=0, j=0, cur;
	while(a[i][2]==1&&i<NA) i++;
	while(b[j][2]==1&&j<NB) j++;
	if(i<NA&&j<NB){
		if(a[i][0]<b[j][0]||(a[i][0]==b[j][0]&&a[i][1]<b[j][1])){
			cur=a[i][1]; a[i][2]=1; cnt++; fa++;
			while(1){
				while(b[j][0]<cur&&j<NB) j++;
				if(j>=NB) break;
				while(b[j][2]==1&&j<NB) j++;
				if(j>=NB) break;
				cur=b[j][1]; b[j][2]=1; cnt++;
				while(a[i][0]<cur&&i<NA) i++;
				if(i>=NA) break;
				while(a[i][2]==1&&i<NA) i++;
				if(i>=NA) break;
				cur=a[i][1]; a[i][2]=1; cnt++;
			}
		}
		else{
			cur=b[j][1]; b[j][2]=1; cnt++; fb++;
			while(1){
				while(a[i][0]<cur&&i<NA) i++;
				if(i>=NA) break;
				while(a[i][2]==1&&i<NA) i++;
				if(i>=NA) break;
				cur=a[i][1]; a[i][2]=1; cnt++;
				while(b[j][0]<cur&&j<NB) j++;
				if(j>=NB) break;
				while(b[j][2]==1&&j<NB) j++;
				if(j>=NB) break;
				cur=b[j][1]; b[j][2]=1; cnt++;
			}
		}
	}
	else{
		for(int k=j; k<NB; k++) if(b[k][2]==0){ cnt++; fb++;}
		for(int k=i; k<NA; k++) if(a[k][2]==0){ cnt++; fa++;}
	}
	return;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int h, m;
	scanf("%d", &N);
	for(int k=1; k<=N; k++){
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		for(int i=0; i<NA; i++){
			scanf("%d:%d", &h, &m);
			a[i][0]=h*60+m;
			scanf("%d:%d", &h, &m);
			a[i][1]=h*60+m+T;
			a[i][2]=0;
		}
		qsort(a, NA, sizeof(int[3]), cmp);
		//for(int i=0; i<NA; i++) printf("%d %d\n", a[i][0], a[i][1]);
		for(int i=0; i<NB; i++){
			scanf("%d:%d", &h, &m);
			b[i][0]=h*60+m;
			scanf("%d:%d", &h, &m);
			b[i][1]=h*60+m+T;
			b[i][2]=0;
		}
		qsort(b, NB, sizeof(int[3]), cmp);
		//for(int i=0; i<NB; i++) printf("%d %d\n", b[i][0], b[i][1]);
		cnt=0; fa=0; fb=0;
		while(cnt<NA+NB) doit();
		printf("Case #%d: %d %d\n", k, fa, fb);
    }
    //getch();
    return 0;
}

