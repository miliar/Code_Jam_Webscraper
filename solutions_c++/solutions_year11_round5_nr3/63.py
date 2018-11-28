#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

#define lint long long

#define sz size()
#define pb push_back
#define mp make_pair

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[200][200];
int dx[8],dy[8];

int C[200][200];
int VF[200][200], VT[200][200];
int X[20000], Y[20000], sx;

int m,n;

bool T(int x1, int y1, int x2, int y2) {
	int k;
	SFOR(k,2*A[x1][y1],2*A[x1][y1]+2) if (((x1+dx[k])%m == x2) && ((y1+dy[k])%n == y2)) return true;
	return false;
}

bool ProceedX() {
	int i,j,x,y;
	int xx;
	FOR(xx,sx) {
		i = X[xx];
		j = Y[xx];
		SFOR(x,m-1,m+2) SFOR(y,n-1,n+2) if (VF[(i+x)%m][(j+y)%n] == 0) if (T((i+x)%m,(j+y)%n,i,j)) {
			VF[(i+x)%m][(j+y)%n] = 1;
			VT[i][j] = 1;
			i = (i+x)%m;
			j = (j+y)%n;
			SFOR(x,m-1,m+2) SFOR(y,n-1,n+2) if (VT[(i+x)%m][(j+y)%n] == 0) if (T(i,j,(i+x)%m,(j+y)%n)) {
				C[(i+x)%m][(j+y)%n]--;
				if (C[(i+x)%m][(j+y)%n] == 0) return true;
				if (C[(i+x)%m][(j+y)%n] == 1) { X[sx] = (i+x)%m; Y[sx] = (j+y)%n; sx++; }
			}
			break;
		}
	}
	return false;
}

int solve() {
	int i,j,x,y;
	memset(C,0,sizeof(C));
	memset(VF,0,sizeof(VF));
	memset(VT,0,sizeof(VT));
	FOR(i,m) FOR(j,n) {
		SFOR(x,m-1,m+2) SFOR(y,n-1,n+2) if (T((i+x)%m,(j+y)%n,i,j)) C[i][j]++;
	}
	FOR(i,m) FOR(j,n) if (C[i][j] == 0) return 0;
	sx = 0;
	FOR(i,m) FOR(j,n) if (C[i][j] == 1) { X[sx] = i; Y[sx] = j; sx++; }
	if (ProceedX()) return 0;
	int ans = 1;
	int i1,j1;
	FOR(i,m) FOR(j,n) if (VT[i][j] == 0) {
		sx = 0;
		ans = (ans*2)%1000003;
		i1 = i;
		j1 = j;
		SFOR(x,m-1,m+2) SFOR(y,n-1,n+2) if (VF[(i+x)%m][(j+y)%n] == 0) if (T((i+x)%m,(j+y)%n,i,j)) {
			VF[(i+x)%m][(j+y)%n] = 1;
			VT[i][j] = 1;
			i = (i+x)%m;
			j = (j+y)%n;
			SFOR(x,m-1,m+2) SFOR(y,n-1,n+2) if (VT[(i+x)%m][(j+y)%n] == 0) if (T(i,j,(i+x)%m,(j+y)%n)) {
				C[(i+x)%m][(j+y)%n]--;
				if (C[(i+x)%m][(j+y)%n] == 0) return true;
				if (C[(i+x)%m][(j+y)%n] == 1) { X[sx] = (i+x)%m; Y[sx] = (j+y)%n; sx++; }
			}
			break;
		}
		ProceedX();
		i = i1;
		j = j1;
	}
	return ans;
}

int main() {
	int i,j;
	FILE* fp = fopen("C.in","r");
	FILE* fp1 = fopen("C.out","w");
	int t,tt;
	fscanf(fp,"%d",&tt);
	FOR(t,tt) {
		fprintf(fp1,"Case #%d: ",t+1);
//		printf("Case #%d: ",t+1);
		fscanf(fp,"%d%d",&m,&n);
		dx[0] = 1; dx[1] = m-1; dy[0] = dy[1] = 0;
		dy[2] = 1; dy[3] = n-1; dx[2] = dx[3] = 0;
		dx[4] = dy[4] = 1; dx[5] = m-1; dy[5] = n-1;
		dx[6] = dy[7] = 1; dx[7] = m-1; dy[6] = n-1;
		char ch;
		FOR(i,m) FOR(j,n) {
			do { fscanf(fp, "%c", &ch); } while ((ch != '/') && (ch != '\\') && (ch != '|') && (ch != '-')); 
			if (ch == '|') A[i][j] = 0;
			if (ch == '-') A[i][j] = 1;
			if (ch == '\\') A[i][j] = 2;
			if (ch == '/') A[i][j] = 3;
		}
		fprintf(fp1,"%d\n",solve());
	}
	fclose(fp);
	fclose(fp1);
    return 0;
}