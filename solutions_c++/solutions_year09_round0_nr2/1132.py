#include <stdio.h>
#include <vector>

using namespace std;

struct smap{
	int alti;
	char* basin;
} map[102][102];

char bch[102][102];

struct scoord{
	short i;
	short j;
} coord;

vector<scoord> st;
int T, H, W;
char suit='a';

scoord next(scoord coord){
	scoord ret;
	int min=map[coord.i][coord.j].alti;	//NWES
	if(map[coord.i-1][coord.j].alti<min){
		min=map[coord.i-1][coord.j].alti;
		ret.i=coord.i-1, ret.j=coord.j;
	}
	if(map[coord.i][coord.j-1].alti<min){
		min=map[coord.i][coord.j-1].alti;
		ret.i=coord.i, ret.j=coord.j-1;
	}
	if(map[coord.i][coord.j+1].alti<min){
		min=map[coord.i][coord.j+1].alti;
		ret.i=coord.i, ret.j=coord.j+1;
	}
	if(map[coord.i+1][coord.j].alti<min){
		min=map[coord.i+1][coord.j].alti;
		ret.i=coord.i+1, ret.j=coord.j;
	}
	if(min==map[coord.i][coord.j].alti) {
		ret.i=0, ret.j=0;
	}
	return ret;
}

int main(void){
	FILE *fin=fopen("B-large.in","r"), *fout=fopen("output.txt","w");

	int i,j;
	fscanf(fin, "%d", &T);
	for(int n=0; n<T; ++n){
		suit='a';
		fscanf(fin, "%d%d", &H, &W);
		for(i=0; i<=H+1; ++i) { map[i][0].alti=map[i][W+1].alti=16384; }
		for(j=0; j<=W+1; ++j) { map[0][j].alti=map[H+1][j].alti=16384; }
		for(i=1; i<=H; ++i) for(j=1; j<=W; ++j){ map[i][j].basin=NULL, fscanf(fin, "%d", &map[i][j].alti); }
		for(i=1; i<=H; ++i){
			for(j=1; j<=W; ++j){
				if(map[i][j].basin==NULL){
					st.clear();
					coord.i=i, coord.j=j;
					while(1){
						st.push_back(coord);
						bch[coord.i][coord.j]=suit;
						char* tmp=&bch[coord.i][coord.j];
						coord=next(coord);
						if(coord.i==0 && coord.j==0){
							suit++;
							int k=st.size();
							while(k--){
								map[st[k].i][st[k].j].basin=tmp;
							}
							break;
						}else if(map[coord.i][coord.j].basin!=NULL){
							int k=st.size();
							while(k--){
								map[st[k].i][st[k].j].basin=map[coord.i][coord.j].basin;
							}
							break;
						}
					}
				}
			}
		}
		fprintf(fout, "Case #%d:\n", n+1);
		for(i=1; i<=H; ++i){
			for(j=1; j<=W; ++j){
				fprintf(fout, "%c ", *map[i][j].basin);
			}
			fprintf(fout, "\n");
		}
	}

	fclose(fin), fclose(fout);
	return 0;
}