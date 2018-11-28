#include <iostream>
#include <list>
#include <string.h>

int possible(char *pattern, char *testword, int depth, std::list<char *>::iterator d_begin, std::list<char *>::iterator d_end) {
	int count = 0;
	if(*pattern == '(') {
		char *endp = strchr(pattern, ')');
		
		testword[depth+1]='\0';
		for(pattern++; pattern<endp; pattern++){
			testword[depth]=*pattern;
			
			std::list<char *>::iterator it;
			
			for(it=d_begin; it!=d_end; it++) {
				if(strncmp(*it, testword, depth+1) == 0) {
					break;
				}
			}
			if(it!=d_end) {
				count += possible(endp+1, testword, depth+1, it, d_end);
			}
		}
	}
	else if(*pattern == '\0') {
		return 1;
	}
	else {
		testword[depth]=*pattern;
		testword[depth+1]='\0';
		std::list<char *>::iterator it;
			
		for(it=d_begin; it!=d_end; it++) {
			if(strncmp(*it, testword, depth+1) == 0) {
				break;
			}
		}
		if(it!=d_end) {
			count += possible(pattern+1, testword, depth+1, it, d_end);
		}
	}
	return count;
}

int main(int arcgc, char *argv[]) {
	int L,D,N;
	std::list<char*> dictionary;
	
	std::cin >> L >> D >> N;
	
	for(int w=0; w<D; w++) {
		char *buffer = new char[L+2];
		std::cin >> buffer;
		dictionary.push_back(buffer);
	}

	for(int c=1; c<=N; c++) {
		char *pattern = new char[L*30 + 5];
		std::cin >> pattern;
		
		char *testword = new char[L+2];
		printf("Case #%d: %d\n", c, possible(pattern, testword, 0, dictionary.begin(), dictionary.end()));
	}
}
