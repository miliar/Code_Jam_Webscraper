#include <cstdio>
#include <cstring>

using namespace std;

char in[] = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvqz";
char out[] = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupzq";
char d[256];

char r[128];

int main(){
	int tc, tcn;
	for(int i=0; i<256; ++i)
		d[i] = i;
	for(int i=0; i<strlen(in); ++i)
		d[in[i]] = out[i];
	scanf("%d", &tcn);
	fgets(r, 128, stdin);
	for(tc=0; tc<tcn; ++tc){
		fgets(r, 128, stdin);
		for(int i=0; i<128; ++i)
			r[i] = d[r[i]];
		printf("Case #%d: %s", tc+1, r);
	}
}
