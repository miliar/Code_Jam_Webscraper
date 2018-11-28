#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char t[1000];
int main() {
	int z;
	scanf("%d",&z);
	for (int Zz=1;Zz<=z;Zz++) {
		printf("Case #%d: ", Zz);
		scanf("%s",t);
		int n = strlen(t);
		if (next_permutation(t,t+n))
			puts(t);
		else {
			t[n++]='0';
			t[n]=0;
			sort(t,t+n);
			for(int i=0;t[i];i++)
				if (t[i]!='0') {
					swap(t[i],t[0]);
					break;
				}
			sort(t+1,t+n);
			puts(t);
		}
	}
	return 0;
}
