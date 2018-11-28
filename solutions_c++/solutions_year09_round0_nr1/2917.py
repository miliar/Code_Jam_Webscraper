#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define MAXWORDS 5050
#define MAXLEN 20
#define MAXALPH 35

char word[MAXWORDS][MAXLEN];
char test[MAXALPH*MAXLEN];
bool lett[MAXLEN][MAXALPH];

int main() {
	int lenWord, numWords, numQueries;

	scanf("%d%d%d",&lenWord,&numWords,&numQueries);

	for (int i=0;i<numWords;i++)
		scanf("%s",word[i]);

	for (int query=0;query<numQueries;query++) {
		int len, actLett=0, result=0;
		bool openBracket=false;

		scanf("%s",test);

		len=strlen(test);

		for (int i=0;i<len;i++) {
			if (test[i]=='(')
				openBracket=true;
			else if (test[i]==')') {
				openBracket=false;
				actLett++;
			}
			else {
				lett[actLett][test[i]-'a']=true;

				if (!openBracket)
					actLett++;
			}
		}

		for (int i=0;i<numWords;i++) {
			bool corrWord=true;

			for (int j=0;j<lenWord;j++)
				if (!lett[j][word[i][j]-'a'])
					corrWord=false;

			if (corrWord)
				result++;
		}

		printf("Case #%d: %d\n",query+1,result);

		for (int i=0;i<lenWord;i++)
			fill(lett[i],lett[i]+MAXALPH,false);
	}

	return 0;
}
