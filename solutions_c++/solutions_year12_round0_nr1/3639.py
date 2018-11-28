#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

const string F = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv ";
const string G = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup ";

char m[300];
char st[10000];

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	memset(m, ' ', sizeof(m));
	for (int i = 0; i < F.length(); ++i)
		m[F[i]] = G[i];
	m['z'] = 'q', m['q'] = 'z';
	
	int T;
	scanf("%d%*c", &T);
	for (int cs = 1; cs <= T; ++cs) {
		gets(st);
		int l = strlen(st);
		printf("Case #%d: ", cs);
		for (int i = 0; i < l; ++i)
			printf("%c", m[st[i]]);
		printf("\n");
	}
	
	return 0;
}
