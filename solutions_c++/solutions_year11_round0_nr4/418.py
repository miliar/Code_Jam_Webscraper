#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int L[1001];
bool visited[1001];
int N;
int l;
double p;

double ansL[1001];

void getListOfN(int b){
	if (b>1)
		getListOfN(b-1);
	else{
		ansL[1] = 0;
		return;
	}
	vector< int > V(b);
	vector< bool > vi(b);
	for (int i=0; i<b; i++)
		V[i] = i;

	ansL[b] = 0;
	int toB = 0;
	do {
		vi.assign(b, false);
		for (int i=0; i<b; i++)
			if (!vi[i]){
				int l=0;
				int j = i;
				while (!vi[j]){
					vi[j] = true;
					j = V[j];
					l++;
				}
				if (l==b)
					toB++;
				else
					ansL[b] += ansL[l];
			}
	} while (next_permutation(V.begin(), V.end()));
	double ff = 1;
	for (int i=1; i<=b; i++)
		ff *= i;
	ansL[b] += ff;
	ansL[b] /= (ff-toB);
	printf("%d %lf\n", b, ansL[b]);
}

int main(){
	//getListOfN(10);
	int t;
	scanf("%d", &t);
	for (int it=1; it<=t; it++){
		scanf("%d", &N);
		memset(visited, 0, sizeof(visited));
		for (int i=0; i<N; i++)
			scanf("%d", L+i);
		double ans = 0;
		for (int i=0; i<N; i++)
			if (!visited[i]){
				int j = i;
				int l=0;
				while (!visited[j]){
					visited[j] = true;
					j = L[j]-1;
					l++;
				}
				if (l>1)
					ans += l;
			}
		printf("Case #%d: %lf\n", it, ans);
	}
	return 0;
}
