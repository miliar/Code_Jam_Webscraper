#include <cstdio>
#include <cctype>

#include <map>

using namespace std;

const char *line1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyqeez";
const char *line2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupazooq";

char str[100000];

map<char, char> rec;

int main() {
	rec.clear();
	for (int i = 0; line1[i]; i++)
		rec[line1[i]] = line2[i];
	int n;
	scanf("%d", &n);
	gets(str);
	for (int i = 0; i < n; i++) {
		printf("Case #%d: ", i + 1);
		gets(str);
		for (char *p = str; *p; p++)
			if (rec.find(*p) != rec.end()) *p = rec[*p];
		printf("%s\n", str);
	}
	return 0;
}