#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cmath>
#include <numeric>
#include <cassert>
#include <bitset>

using namespace std;
char buf[50], buf2[50];

inline bool solve(int tc){
	scanf("%s", buf);
	int s = strlen(buf);
	strcpy(buf2, buf);
	next_permutation(buf2, buf2+s);
	if(strcmp(buf,buf2)>=0){
		buf2[s++] = '0';
		buf2[s] = '\0';
		sort(buf2, buf2+s);
		int i = 0;
		while(buf2[i] == '0') ++i;
		swap(buf2[i], buf2[0]);
	}
	else{
		assert(strcmp(buf, buf2)<0);
	}
	printf("Case #%d: %s\n", tc, buf2);
	return true;
}

int main (int argc, char const *argv[]) {
	int n; scanf("%d",&n);
	for(int k=1;solve(k)&&k<n;k++);
	return 0;
}