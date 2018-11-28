#include<cstdio>
#include<algorithm>
#include<map>

using namespace std;
const int MAX = 550;

int n, sum, casos, v[MAX];
map <int, int> mapa;
bool res;

void imprime(int m1, int m2){
	bool first = true;

	for(int i=0;i<n;i++){
		if(((1<<i)&m1) && ((1<<i)&m2)) continue;
		if(!((1<<i)&m1)) continue;
		if(first == false) printf(" ");
		first = false;;
		printf("%d", v[i]);
	}
	printf("\n");
	first = true;
	for(int i=0;i<n;i++){
		if(((1<<i)&m1) && ((1<<i)&m2)) continue;
		if(!((1<<i)&m2)) continue;
		if(first == false) printf(" ");
		first = false;
		printf("%d", v[i]);
	}
	printf("\n");
}

int main(){
	scanf(" %d", &casos);
	for(int inst=1;inst<=casos;inst++){
	scanf(" %d", &n);
	for(int i=0;i<n;i++) scanf(" %d", &v[i]);
	printf("Case #%d:\n", inst);

	mapa.clear();
	res = false;
	for(int mask=0;mask<(1<<20);mask++){
		sum = 0;
		for(int i=0;i<n;i++)
			if(((1<<i)&mask)>0) sum += v[i];
		if(mapa.count(sum) == 0) mapa[sum] = mask;
		else{
			res = true;
			imprime(mapa[sum], mask);
			break;
		}
	}
	if(res == false) printf("Impossible\n");
	}
	return 0;
}


