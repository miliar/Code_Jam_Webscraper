#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

int array[100], n;
char seq[100];

int get(char *s) {
	int r = -1;
	for(int i = 0; s[i]; i++) {
		if(s[i] == '1') {
			r = i;
		}
	}
	return r;
}

int read() {
	scanf("%d",&n);
	for(int i = 0; i < n; i++) {
		scanf("%s",seq);
		array[i] = get(seq);
	}
}

int casos = 1;
void process() {
	int ct = 0;
	for(int i = 0; i < n; i++) {		
		for(int j = i; j < n; j++) {
			if(array[j] <= i) {			
				ct += (j-i);
				int tmp = array[j];				
				for(int k = j; k > i; k--) {
					array[k] = array[k-1];					
				}				
				array[i] = tmp;
				break;
			}
		}
	}
	printf("Case #%d: %d\n",casos++,ct);
}

int main() {

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t;
	scanf("%d",&t);
	while(t--) {
		read();
		process();
	}
	
	return 0;
}
