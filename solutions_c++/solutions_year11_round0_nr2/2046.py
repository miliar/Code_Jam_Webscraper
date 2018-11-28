#include<cstdio>
#include<vector>
using namespace std;

int N, C;

int len;
vector<char> opposed[26];
char rule[26][26];
int count[26];
char cur;
char ruleStr[4]; // 3+\0

char input[101];
int inlen;

void clear() {
	len = 0;
	memset( count, 0, sizeof(int)*26);
}

char r;
void append(char cur) {
	if( len == 0 ) {
		input[len] = cur;
		count[cur-'A']++;
		len++;
		return;
	}
	r = rule[input[len-1]-'A'][cur-'A'];
	if( r != 0 ) {
		count[input[len-1]-'A']--;
		input[len-1] = r;
		cur = r;
		count[r-'A']++;
	} else {
		// Test opposed
		input[len] = cur;
		count[cur-'A']++;
		len++;
	}
	
	for( vector<char>::iterator it=opposed[cur-'A'].begin(); 
			it!=opposed[cur-'A'].end(); it++ ) {
		if( count[*it-'A'] > 0 ) {
			clear();
			return;
		}
	}
	
}

void printRslt(int i) {
	printf("Case #%d: [", i);
	for( int j=0; j<len; j++ ) {
		printf( "%c", input[j] );
		if( j<len-1 )
			printf(", ");
	} 		
	printf("]\n");
}

int main() {
	scanf("%d", &N);
	for( int i=1; i<=N; i++ ) {
		len = 0;
		for( int j=0; j<26; j++ ) opposed[j].clear();
		for( int j=0; j<26; j++ )
			memset(rule[j],0,sizeof(char)*26);
		clear();
	
		scanf("%d", &C);
		for( int j=0; j<C; j++ ) { // Merge
			scanf("%s", ruleStr ); 
			rule[ruleStr[0]-'A'][ruleStr[1]-'A'] = ruleStr[2];
			rule[ruleStr[1]-'A'][ruleStr[0]-'A'] = ruleStr[2];
		}	
		scanf("%d", &C); // Oppoesed
		for( int j=0; j<C; j++ ) {
			scanf("%s", ruleStr);
			opposed[ ruleStr[0]-'A' ].push_back(ruleStr[1]);
			opposed[ ruleStr[1]-'A' ].push_back(ruleStr[0]);
		}
		scanf("%d %s", &inlen, input);
		for( int j=0; j<inlen; j++ ) {
			append(input[j]);
		}
		
		printRslt(i);
	}	

	return 0;
}
