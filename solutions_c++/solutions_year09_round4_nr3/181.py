#include<stdio.h>
#include<string.h>

#define MAX_BPM 105

int n;
int k;
int y[105][27];	//y[n][k]

int N;

int mat[105][105];

/*
	thanks to Igor
*/
int graph[MAX_BPM][MAX_BPM];
bool seen[MAX_BPM];
int matchL[MAX_BPM], matchR[MAX_BPM];
int nleftbpm, nrightbpm;

bool bpmDfs( int u ){
    for( int v = 0; v < nrightbpm; v++ ) if( graph[u][v]==N ){
        if( seen[v] )
			continue;
        seen[v] = true;
        if( matchR[v] < 0 || bpmDfs( matchR[v] ) ){
            matchL[u] = v;
            matchR[v] = u;
            return true;
        }
    }
    return false;
}
int bpm(){
	memset( matchL, -1, sizeof( matchL ) );
	memset( matchR, -1, sizeof( matchR ) );
	static int cnt,i;
	for(cnt = i = 0; i < nleftbpm; i++ ){
		memset( seen, 0, sizeof( seen ) );
		if( bpmDfs( i ) )
			cnt++;
	}
	return cnt;
}
/******/


int get(int i,int j){
	bool eq,ls,gr;
	eq = ls = gr = false;
	int p;

	for(p=0;p<k;p++){
		
		if(y[i][p]==y[j][p])
			eq = true;
		else if(y[i][p] > y[j][p])
			gr = true;
		else
			ls = true;
	}

	if(eq || (ls && gr))	return 0;
	if(ls)	return 1;
	return -1;

}

int main(){

	int T;
	int i,j,p;

	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%d%d",&n,&k);

		for(i=0;i<n;i++)for(j=0;j<k;j++)
			scanf("%d",&y[i][j]);
		
		nleftbpm = nrightbpm = n;

		for(i=0;i<n;i++)for(j=i+1;j<n;j++){
			p = get(i,j);
			if(p==1)
				graph[i][j] = N;
			else if(p==-1)
				graph[j][i] = N;
		}

		printf("Case #%d: %d\n",N,n-bpm());
	}

	return 0;
}