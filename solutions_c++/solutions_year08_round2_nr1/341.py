#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

static int sumy[3][3];

static long long wynik() {
	long long suma = 0;
	for(int x1=0;x1<3;x1++)
	for(int x2=0;x2<3;x2++)
	for(int y1=0;y1<3;y1++)
	for(int y2=0;y2<3;y2++) {
		int x3 = (6-x1-x2)%3;
		int y3 = (6-y1-y2)%3;
		if((x1+x2+x3)%3) {
			printf("DUPA X!\n");
		}
		if((y1+y2+y3)%3) {
			printf("DUPA Y!\n");
		}
		int w1=(x1+3*y1), w2=(x2+3*y2), w3=(x3+3*y3);
		if(w1==w2 && w2==w3) {
			long long n1 = sumy[x1][y1];
			if(n1>=3)
			suma += (n1)*(n1-1)*(n1-2);
		} else if(w1==w2) {
			long long n1 = sumy[x1][y1];
			long long n2 = sumy[x3][y3];
			if(n1>=2)
			suma += n1*(n1-1)*n2;
		} else if(w3==w1) {
			long long n1 = sumy[x1][y1];
			long long n2 = sumy[x2][y2];
			if(n1>=2)
			suma += n1*(n1-1)*n2;
		} else if(w2==w3) {
			long long n1 = sumy[x2][y2];
			long long n2 = sumy[x1][y1];
			if(n1>=2)
			suma += n1*(n1-1)*n2;
		} else {
			long long n1 = sumy[x1][y1];
			long long n2 = sumy[x2][y2];
			long long n3 = sumy[x3][y3];
			suma += n1*n2*n3;
		}
	}
	return suma/6L;
}

int main() {
	int N; scanf("%d",&N);
	for(int iN=1;iN<=N;iN++) {
		int n;
		long long A,B,C,D,x0,y0,M;
		scanf("%d%lld%lld%lld%lld%lld%lld%lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		memset(sumy, 0, sizeof(sumy));
		for(int i=0;i<n;i++) {
			sumy[x0%3][y0%3]++;
			x0 = (A*x0+B)%M;
			y0 = (C*y0+D)%M;
		}
		printf("Case #%d: %lld\n",iN,wynik());
	}
	return 0;
}

