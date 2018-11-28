#include <stdio.h>
#include <string.h>
#include "stdlib.h"
#include "unistd.h"
#include "math.h"
#include <string>
#include <sys/types.h>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <set>
using namespace std;

int main(int argc, char *argv[]) {
//processing...
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		map<int, int> m;
		int N;
		scanf("%d", &N);
		for(int i=1; i<=N; ++i){
			int A, B;
			scanf("%d %d", &A, &B);
			m[A]=B;
		}
		int is=0;
		map<int,int>::iterator it;
		for(it=m.begin(); it!=m.end(); ++it){
			map<int,int>::iterator it2;
			for(it2=m.begin(); it2!=m.end(); ++it2){
				if(((it->first)<(it2->first)) && ((it->second)>(it2->second))){
					++is;
				}
			}
		}
		printf("Case #%d: %d\n", t, is);
	}
}







