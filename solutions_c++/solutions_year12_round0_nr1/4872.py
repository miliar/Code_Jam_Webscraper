#include<cstdio>
#include<iostream>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int t,i,first;
	char c;
	char key[100] = "";
	char a[] = {"ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv"};
	char b[] = {"ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup"};
	key['z' - 'a'] = 'q';
	key['q' - 'a'] = 'z';
	for(i = 0; i < strlen(a); i++) {
		key[a[i] - 'a'] = b[i];
	}
	scanf("%d", &t);
	scanf("%*c");
	for(i = 1; i < t + 1; i++){
		first = 1;
		while(scanf("%c", &c) != EOF && c != '\n') {
			if(first == 1) {
				printf("Case #%d: ", i);
				first = 0;
			}
			if(c == ' ') printf(" ");
			else printf("%c", key[c - 'a']);
		}
		printf("\n");
	}
	return 0;
}