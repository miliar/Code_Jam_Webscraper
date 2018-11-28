#include<cstdio>
#include<algorithm>
#define ERR 1e-9

using namespace std;
const int MAX = 100200;
int casos;
double A, B, k, p[MAX];

int sup(const double &a, const double &b){
	if(a+ERR >= b){
		if(b+ERR >= a) return 0;
		return -1;
	}
	return 1;
}

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	scanf(" %lf %lf", &A, &B);
	for(int i=1;i<=A;i++) scanf(" %lf", &p[i]);
	for(int i=2;i<=A;i++) p[i]=p[i-1]*p[i];

	k = B+2.0;
	for(int x=0;x<=A;x++){
		double ok = B-A+(double)(x+x)+1.0;
		double nok = ok+B+1.0;
		double prob = p[(int)A-x];
		double nv = (ok*prob) + (nok*(1-prob));
		if(sup(k, nv) == -1) k = nv;
	}
	printf("Case #%d: %lf\n", inst, k);
	}
	return 0;
}

