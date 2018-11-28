#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<PII> VPII;

typedef vector<double> VD;
typedef vector<string> VS;

typedef long long LL;

char* conv = "yhesocvxduiglbkrztnwjpfmaq";

int main(){ 	
	int cases;
	scanf("%d\n", &cases);
	
	for(int caseNr = 1; caseNr <= cases; caseNr++){
		// go for it!	
		printf("Case #%d: ", caseNr);
		
		while(true){
			char c;
			scanf("%c", &c);
			if(c != ' ' && !(c >= 'a' && c <= 'z'))
				break;
			char d = conv[c - 'a'];
			if (c==' ')
				printf(" ");
			else
				printf("%c", d);
		}
		printf("\n");
		
		fflush(stdout);
	}
	
	return 0;
}
