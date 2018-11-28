#include <cstdio>

using namespace std;

int main(){
	char line[101];
	char map [26];
	char sampleInput[] = "zqejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char sampleOutput[] = "qzour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	for(int i = 0; sampleInput[i] != '\0'; i++)
		if(sampleOutput[i] != ' ')
			map[sampleInput[i] - 'a'] = sampleOutput[i];

	gets(line);
	for(int t = 1; t <= 30; t++){
		gets(line);
		for(int i = 0; line[i] != '\0'; i++)
			if(line[i] >= 'a' && line[i] <= 'z')
				line[i] = map[line[i] - 'a'];
		printf("Case #%d: %s\n", t, line);
	}

}