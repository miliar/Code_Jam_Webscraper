#include <cstdio>

using namespace std;

int main(){
    int ncas;
    scanf("%d", &ncas);
    for(int cas = 1; cas <= ncas; ++cas){
	int N, K;
	scanf("%d%d", &N, &K);
	printf("Case #%d: %s\n", cas, ((K&((1<<N)-1)) == (1<<N)-1) ? "ON" : "OFF");
    }
}
