#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

#include <fstream>
#include <cassert>
using namespace std;
#define all(x) (x).begin(),(x).end()

#define vs vector <string>
#define vi vector <int>
#define p(X) push_back((X))

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fire(i,j,n) for(int (i)=(j);(i)<=(n);(i)++)
#define firr(i,j,n) for(int (i)=(j);(i)>(n);(i)--)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)

#define _bc(i) __builtin_popcount(i)

#define FILEREAD
int mp[101][101];
int comp[101][101];
char label[101][101];
char ItoC[21001];
int dr[]={-1,0,0,1};
int dc[]={0,-1,1,0};
int ncmp;
int H,W;

bool valid(int r,int c) {return (r>=0 && r<H && c>=0 && c<W);}
bool isreachable(int cr,int cc,int nr,int nc)
{
	int mht=-1;
	int nnr,nnc;
	fir(k,0,4) {
		int tr=cr+dr[k];
		int tc=cc+dc[k];
		if (!valid(tr,tc)) continue;
		if (mp[tr][tc]>=mp[cr][cc]) continue;
		if (mht==-1 || mht>mp[tr][tc]) {mht=mp[tr][tc];nnr=tr;nnc=tc;}
	}
	if (mht==-1) {nnr=cr;nnc=cc;}
	if (nnr==nr && nnc==nc) return true;
	return false;
}
void dfs(int cr,int cc)
{
	comp[cr][cc]=ncmp;
	fir(k,0,4) {
		int nr=cr+dr[k];
		int nc=cc+dc[k];
		if (!valid(nr,nc)) continue;
		if (comp[nr][nc]!=-1) continue;
		if (!isreachable(nr,nc,cr,cc)) continue;
		dfs(nr,nc);
	}
}
int main() {
	FILE *fin,*fout;
	#ifdef FILEREAD
	fin=fopen("p2.in","r");
	fout=fopen("p2.out","w");
	#else
	fin=stdin;
	fout=stdout;
	#endif
	int tc;
	fscanf(fin,"%d",&tc);
	fir(T,0,tc) {
		fprintf(fout,"Case #%d:\n",T+1);
		fscanf(fin,"%d %d",&H,&W);
		fir(i,0,H) fir(j,0,W) fscanf(fin,"%d",&mp[i][j]);
		ncmp=0;
		fir(i,0,H) fir(j,0,W) comp[i][j]=-1;
		fir(i,0,H) fir(j,0,W) {
			if (comp[i][j]==-1 && isreachable(i,j,i,j)) {dfs(i,j);++ncmp;}
		}
		assert(ncmp<21001);
		fir(i,0,21001) ItoC[i]=-1;
		char cChar='a';
		fir(i,0,H) fir(j,0,W) {
			if (ItoC[comp[i][j]]==-1) {ItoC[comp[i][j]]=cChar++;}
			label[i][j]=ItoC[comp[i][j]];
		}
		fir(i,0,H) {
			fprintf(fout,"%c",label[i][0]);
			fir(j,1,W) fprintf(fout," %c",label[i][j]);
			fprintf(fout,"\n");
		}
	}
    return 0;
}
