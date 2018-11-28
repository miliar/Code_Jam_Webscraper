#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <set>
using namespace std;
const double PI = acos(-1.0);


int main() {
    freopen("A-large.in","r",stdin);
    freopen("A.txt","w",stdout);
	int Tn;
	scanf("%d", &Tn);
	int n,K;
	for (int T = 1; T <= Tn; T++) {
		scanf("%d%d",&n,&K);
		printf("Case #%d: ", T);
		if(K%(1<<n)+1 == (1<<n)){
            puts("ON");
		}else{
            puts("OFF");
		}
	}
	return 0;
}
