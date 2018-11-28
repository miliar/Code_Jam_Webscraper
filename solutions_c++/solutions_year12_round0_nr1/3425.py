#include <iostream>
#include <map>
using namespace std;

int main() {
    FILE * input;
    input = fopen("A-small-attempt1.in", "r");
    FILE * output;
    output = fopen("A-small-attempt1.out", "w");
    
    int T;    		// num cases
    char G[102];	// string
    int i, j, k;  	// iterators
    
    map<char, char> mapping;
    char googlerese[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char english[] =    "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    for(i = 0; i < strlen(googlerese); i++) {
		if(mapping.find(googlerese[i]) == mapping.end()) {
			mapping.insert(pair<char, char>(googlerese[i], english[i]));
		}
	}
	// q in googlerese was missing but it's goten from the hints
	mapping.insert(pair<char, char>('q', 'z'));
	// q in english was missing, in googlerese it matches with the missing z
	mapping.insert(pair<char, char>('z', 'q'));
	
    fscanf(input, "%d\n", &T);
    
    for(i = 1; i <= T; i++)
    {
		// get string in Googlerese
		fgets(G, sizeof G, input);
		j = 0;
		fprintf(output, "Case #%d: ", i);
		while(G[j] != '\0' && G[j] != '\n') {
			fprintf(output, "%c", mapping[G[j++]]);
		}
		fprintf(output, "\n");
	}
	
	getchar();
	return 0;
}
