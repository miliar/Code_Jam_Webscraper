#include<iostream>
#include<cmath>
using namespace std;

const char *a = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
const char *b = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

int map[26];
char buf[200]
;
void solve()
{	
	gets(buf);	
	for (int i = 0; buf[i]; i++)
		if (buf[i] >= 'a' && buf[i] <= 'z')
			buf[i] = map[buf[i] - 'a'];
	
	printf("%s\n", buf);
}

void precount() {
	for (int i = 0; a[i]; i++)
		map[a[i] - 'a'] = b[i];
	map['q' - 'a'] = 'z';
	map['e' - 'a'] = 'o';
	map['y' - 'a'] = 'a';
	int sum = 0;
	for (int i = 0; i < 26; i++)
		sum += 'a' + i - map[i];
	map['z' - 'a'] = sum;			
}

int main()
{
	precount();
	int T, t;
	for (scanf("%d\n", &T), t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		solve();
	}
}
