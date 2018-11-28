#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int N,K;
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",cn);
		if((K&((1<<N)-1)) == ((1<<N)-1)) printf("ON\n");
		else printf("OFF\n");
	}
}
