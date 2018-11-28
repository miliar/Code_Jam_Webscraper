#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <cstdlib>

using namespace std;
#define MAX 1000010


string antes;
char buffer[MAX], buffer2[MAX];


bool ehMenor() {

	for(int i = 0; i < (int) antes.size(); i++) {
		if(buffer[i] > antes[i]) return false;
		else if(buffer[i] == antes[i]) continue;
		else break;
	}
		
return true;
}
int main() {


	int t, count = 1;
	scanf("%d", &t);
	for(;t;t--) {
		scanf("%s", buffer);
		antes = buffer;
		next_permutation(buffer, buffer+(int)strlen(buffer));
		
		if(ehMenor() == true) {
			buffer2[0] = '0';
			int i;
			for(i = 0; i < (int) antes.size(); i++)
				buffer2[i+1] = antes[i];
			buffer2[i+1] = '\0';
			next_permutation(buffer2, buffer2 + (int)strlen(buffer2));
			printf("Case #%d: %s\n", count++, buffer2);
		}
		else printf("Case #%d: %s\n", count++, buffer);
	}




return 0;
}
