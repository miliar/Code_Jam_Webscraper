#include <stdio.h>
#include <memory.h>
class _LIST{
public:
	int A, B, C;
	_LIST *next;
} *list[10000];
int llll;
void insert(int a,int A, int B, int C){
	_LIST *mk;
	mk = new _LIST; mk->next = list[a]; list[a] = mk;
	list[a]->A = A;
	list[a]->B = B;
	list[a]->C = C;
	if(a > llll) llll = a;
}
int can[100][5][10], hc;
int back[5][10];

int cool[100][5][2];
int Dy[12][12][100];

int cnt;
void backs(int x,int y,int z){
	if(z == cnt){
		int i, j;
		for(i=0;i<5;i++) for(j=0;j<10;j++) can[hc][i][j] = back[i][j];
		hc ++;
		return;
	}
	if(y == cnt*2){
		backs(x+1, 0, z);
		return;
	}
	if(x == cnt) return;
	bool al;
	al = false;
	if(back[x][y] == 1){
		if(x < cnt){
			if(back[x+1][y] == 0){
				back[x+1][y] = 1;
				backs(x, y, z+1);
				back[x+1][y] = -1;
				backs(x, y, z);
				back[x+1][y] = 0;
				al = true;
			}
		}
		if(y < cnt*2 && !al){
			if(back[x][y+1] == 0){
				back[x][y+1] = 1;
				backs(x, y, z+1);
				back[x][y+1] = -1;
				backs(x, y, z);
				back[x][y+1] = 0;
				al = true;
			}
		}
		if(y > 0 && !al){
			if(back[x][y-1] == 0){
				back[x][y-1] = 1;
				backs(x, y, z+1);
				back[x][y-1] = -1;
				backs(x, y, z);
				back[x][y-1] = 0;
				al = true;
			}
		}
		if(x > 0 && !al){
			if(back[x-1][y] == 0){
				back[x-1][y] = 1;
				backs(x, y, z+1);
				back[x-1][y] = -1;
				backs(x, y, z);
				back[x-1][y] = 0;
				al = true;
			}
		}
	}
	if(!al){
		backs(x, y+1, z);
	}
}
char A[12][14], B[12][14], dat[12][14];
int N, M;
int ddr[4][2] = { {0,1}, {0,-1}, {1,0}, {-1,0} };
bool CanCheck(int x, int y, int dx, int dy){
	return (0<=x+dx && x+dx<N && 0 <=y+dy && y+dy<M) && (0<=x-dx && x-dx<N && 0 <=y-dy && y-dy<M);
}
bool GOOD(int x,int y){
	return (0<=x && 0<=y && x < N && y < M) ;
}
int temp[12][12];
int Now[5][2];
void Process(int x,int y,int z, int val){
	int i, j, k;
	for(i=0;i<N;i++) for(j=0;j<M;j++) temp[i][j] = 0;
	for(i=0;i<cnt;i++){
		Now[i][0] = x+cool[z][i][0]; Now[i][1] = y+cool[z][i][1];
		temp[ x+cool[z][i][0] ][ y+cool[z][i][1] ] = 1;
	}

	int d1, d2;
	for(i=0;i<cnt;i++){
		for(j=0;j<cnt;j++){
			for(d1=0;d1<4;d1++){
				int dx, dy;
				dx = ddr[d1][0]; dy = ddr[d1][1];
				if(CanCheck(Now[i][0], Now[i][1], dx, dy)){
					if(dat[Now[i][0]-dx][Now[i][1]-dy] != '#' && dat[Now[i][0]+dx][Now[i][1]+dy] != '#' && temp[Now[i][0]-dx][Now[i][1]-dy] != 1 && temp[Now[i][0]+dx][Now[i][1]+dy] != 1){
						temp[ Now[i][0] ][ Now[i][1] ] = 0;
						Now[i][0] += dx; Now[i][1] += dy;
						temp[ Now[i][0] ][ Now[i][1] ] = 1;

									int iq, jq, x1, x2;
									for(iq=0;iq<N;iq++){
										for(jq=0;jq<M;jq++){
											if(temp[iq][jq] == 1) break;
										}
										if(jq < M) break;
									}
									for(x1=0;x1<hc;x1++){
										for(x2=0;x2<cnt;x2++){
											if(temp[ iq+cool[x1][x2][0] ][ jq+cool[x1][x2][1] ] == 0) break;
										}
										if(x2 == cnt) break;
									}
									if(x1 < hc){
										if(Dy[iq][jq][x1] == -1 || Dy[iq][jq][x1] > val+1){
											Dy[iq][jq][x1] = val+1;
											insert(val+1, iq, jq, x1);
//											int i, j;	for(i=0;i<N;i++){ for(j=0;j<M;j++){ printf("%d",temp[i][j]);}printf("\n");}
										}
									}

						for(d2=0;d2<4;d2++){
							int dx, dy;
							dx = ddr[d2][0]; dy = ddr[d2][1];
							if(CanCheck(Now[j][0], Now[j][1], dx, dy)){
								if(dat[Now[j][0]-dx][Now[j][1]-dy] != '#' && dat[Now[j][0]+dx][Now[j][1]+dy] != '#' && temp[Now[j][0]-dx][Now[j][1]-dy] != 1 && temp[Now[j][0]+dx][Now[j][1]+dy] != 1){
									temp[ Now[j][0] ][ Now[j][1] ] = 0;
									Now[j][0] += dx; Now[j][1] += dy;
									temp[ Now[j][0] ][ Now[j][1] ] = 1;
									
									int qi, qj, x1, x2;
									for(qi=0;qi<N;qi++){
										for(qj=0;qj<M;qj++){
											if(temp[qi][qj] == 1) break;
										}
										if(qj < M) break;
									}
									for(x1=0;x1<hc;x1++){
										for(x2=0;x2<cnt;x2++){
											if(temp[ qi+cool[x1][x2][0] ][ qj+cool[x1][x2][1] ] == 0) break;
										}
										if(x2 == cnt) break;
									}
									if(x1 < hc){
										if(Dy[qi][qj][x1] == -1 || Dy[qi][qj][x1] > val+2){
											Dy[qi][qj][x1] = val+2;
											insert(val+2, qi, qj, x1);
//											int i, j;	for(i=0;i<N;i++){ for(j=0;j<M;j++){ printf("%d",temp[i][j]);}printf("\n");}
										}
									}

									temp[ Now[j][0] ][ Now[j][1] ] = 0;
									Now[j][0] -= dx; Now[j][1] -= dy;
									temp[ Now[j][0] ][ Now[j][1] ] = 1;
								}
							}
						}
						
						temp[ Now[i][0] ][ Now[i][1] ] = 0;
						Now[i][0] -= dx; Now[i][1] -= dy;
						temp[ Now[i][0] ][ Now[i][1] ] = 1;
					}
				}
			}
		}
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	while(1){
		if(T == 0) break;
		T--;
		scanf("%d %d",&N,&M);
		int i, j, k, l;
		cnt = 0;
		for(i=0;i<N;i++){
			scanf("%s",dat[i]);
			for(j=0;j<M;j++){
				if(dat[i][j] == 'o' || dat[i][j] == 'w'){ A[i][j] = 'a';cnt ++;}
				else A[i][j] = ' ';
				if(dat[i][j] == 'x' || dat[i][j] == 'w') B[i][j] = 'a';
				else B[i][j] = ' ';
			}
		}
		memset(back, 0, sizeof(back));
		for(i=0;i<cnt;i++) back[0][i] = -1;
		back[0][cnt-1] = 1;
		hc = 0;
		backs(0, cnt-1, 1);

		int ccc;
		int ttj, ttk;
		for(i=0;i<hc;i++){
			ccc = 0;
			for(j=0;j<5;j++){
				for(k=0;k<10;k++){
					if(can[i][j][k] == 1){
						if(ccc == 0){ ttj = j; ttk = k;}
						cool[i][ ccc ][0] = j - ttj;
						cool[i][ ccc ][1] = k - ttk;
						ccc ++;
					}
				}
			}
		}
		for(i=0;i<N;i++) for(j=0;j<M;j++) for(k=0;k<hc;k++) Dy[i][j][k] = -1;
		llll = 0;
		for(i=0;i<N;i++){
			for(j=0;j<M;j++){
				if(A[i][j] == 'a'){
					for(k=0;k<hc;k++){
						for(l=0;l<cnt;l++){
							if(A[ i+cool[k][l][0] ][ j+cool[k][l][1] ] != 'a')  break;
						}
						if( l == cnt ) break;
					}
					Dy[i][j][k] = 0;
					insert(0, i, j, k);
					break;
				}
			}
			if( j < M ) break;
		}

		int si, sj, sk;
		for(i=0;i<N;i++){
			for(j=0;j<M;j++){
				if(B[i][j] == 'a'){
					for(k=0;k<hc;k++){
						for(l=0;l<cnt;l++){
							if(B[ i+cool[k][l][0] ][ j+cool[k][l][1] ] != 'a')  break;
						}
						if( l == cnt ) break;
					}
					break;
				}
			}
			if( j < M ) break;
		}
		si = i; sj = j; sk = k;
		int x, y, z;
		for(i=0;i<=llll;i++){
			_LIST *D;
			for(; list[i] != NULL ; ){
				x = list[i]->A; y = list[i]->B; z = list[i]->C;
				if(Dy[x][y][z] == i){
					Process(x, y, z, i);
				}
				D = list[i];
				list[i] = list[i]->next;
				delete D;
			}
		}
		static int ss=1;
		printf("Case #%d: %d\n",ss++, Dy[si][sj][sk]);
	}
	return 0;
}