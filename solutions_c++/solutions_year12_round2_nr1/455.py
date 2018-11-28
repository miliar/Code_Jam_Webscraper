#include<cstdio>
#include<algorithm>
#define ERR 1e-9

using namespace std;
const int MAX = 220;

int casos, n;
double low, high, mid, T, v[MAX];

int sup(const double &a, const double &b){
	if(a+ERR >= b){
		if(b+ERR >= a) return 0;
		return -1;
	}
	return 1;
}

int valido(int pos, double pct){
	double x, curr = pct, meta = v[pos]+((T*pct)/100.0);
	for(int i=0;i<n;i++){
		if(i == pos) continue;
		x = ((meta-v[i])/T)*100.0;
		if(sup(x, 0.0) == 1) x = 0.0;
		curr += x;
	}
	if(sup(curr, 100.0) >= 0) return 1;
	else return 0;
}

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	scanf(" %d", &n);
	T = 0.0;
	for(int i=0;i<n;i++){
		scanf(" %lf", &v[i]);
		T += v[i];
	}
	printf("Case #%d: ", inst);
	for(int i=0;i<n;i++){
		low = 0.0; high = 100.0;
		while(sup(1e-6, high-low) == 1){
			mid = (low+high)/2;
			if(!valido(i, mid)) high = mid;
			else low = mid;
		}
		printf("%lf%c", low, (i==n-1)?'\n' : ' ');
	}
	}
	return 0;
}

