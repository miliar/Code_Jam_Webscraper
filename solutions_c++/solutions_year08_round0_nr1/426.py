#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

char buf[200];
vector<string> Q;

inline int pos( string s){
	return int( lower_bound( Q.begin(),Q.end(), s ) - Q.begin() );
}

int msw(){
	int ns,nq,mn;
	gets(buf); sscanf(buf, "%d", &ns);
	Q = vector<string>(ns);
	for(int j = 0; j < ns; ++j) { gets(buf); Q[j] = string(buf); }
	sort(Q.begin(), Q.end());
	gets(buf); sscanf(buf,"%d", &nq);

	vector<int> A(ns);
	for(int j = 0; j < nq; ++j){
		gets(buf); int q = pos(string(buf));
		mn = -1;
		for(int j = 0; j < ns; ++j)
			if( j != q && ( mn == -1 || A[j] < A[mn] ) )
				A[q] = A[mn=j]+1;

	}
	return *min_element(A.begin(),A.end());
}

int main(){
	freopen("Ain.txt","r",stdin);
	freopen("Aout.txt","w",stdout);

	int N;
	gets(buf); sscanf(buf,"%d", &N);

	for(int nc = 1; nc <= N; ++nc){
		fprintf(stderr,"%d / %d ",nc,N);
		int r = msw();
		printf( "Case #%d: %d\n", nc, r);
		fprintf(stderr," = %d          \r",r);
	}
}
