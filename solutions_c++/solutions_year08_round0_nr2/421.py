#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

char buf[200];

void ntr(int &na, int &nb){
	na = nb = 0;
	int T,NA,NB;
	gets(buf); sscanf(buf, "%d", &T);
	gets(buf); sscanf(buf, "%d %d", &NA,&NB);
	vector<int> A(NA+NB), B(NA+NB);
	int nt = 0;
	for(int j = 0; j < NA; ++j) {
		gets(buf);
		int sth, stm, enh, enm;
		sscanf(buf, "%d:%d %d:%d", &sth, &stm, &enh, &enm);
		int st = (sth*60+stm)*2+1;
		int en = (enh*60+enm+T)*2;
		A[nt] = st; B[nt] = en; ++nt;
	}
	for(int j = 0; j < NB; ++j) {
		gets(buf);
		int sth, stm, enh, enm;
		sscanf(buf, "%d:%d %d:%d", &sth, &stm, &enh, &enm);
		int st = (sth*60+stm)*2+1;
		int en = (enh*60+enm+T)*2;
		B[nt] = st; A[nt] = en; ++nt;
	}
	sort(A.begin(), A.end());
	sort(B.begin(), B.end());

	int nd = 0;
	for(int j = 0; j < NA+NB; ++j){
		if( A[j] & 1 ) { if(--nd < 0) { nd = 0; ++na;} }
		else ++nd;
	}
	nd = 0;
	for(int j = 0; j < NA+NB; ++j){
		if( B[j] & 1 ) { if(--nd < 0) { nd = 0; ++nb;} }
		else ++nd;
	}
}

int main(){
	freopen("Bin.txt","r",stdin);
	freopen("Bout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		int na,nb;
		fprintf(stderr,"%d / %d ",nc,N);
		ntr(na,nb);
		printf("Case #%d: %d %d\n", nc, na, nb);
		fprintf(stderr, "Case #%d: %d %d\n", nc, na, nb);
	}
}
