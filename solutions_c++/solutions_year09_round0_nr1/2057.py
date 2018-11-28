/* Google Code Jam 2009
 * Qualification Round
 * Problem A: Alien Language
 */


#include <cstdio>
#include <string>
#include <set>
#include <cstring>


char input[20];

std::set< std::string > dictionary;
	
int wordlen;
int dictsize;
int numcases;

std::set < char > pattern[20];

void getpattern()
{
	int c;
	scanf("\n");

	for (int part = 0; part < wordlen; part++) {
		pattern[part].clear();
		
		c = getchar();
		if (c == '(') {
			while ((c = getchar()) != ')') {
				pattern[part].insert(c);
			}
		}
		else {
			pattern[part].insert(c);
		}
	}
}

int countcandidates(int parts, std::string prefix)
{
	if (parts == wordlen) {
		return 1;
	}

	char word[30] = "";
	strcpy(word, prefix.c_str());

	int count = 0;

	std::set < char >::iterator end = pattern[parts].end();
	for (std::set < char >::iterator ll = pattern[parts].begin(); ll != end; ll++) {
		word[parts] = *ll;
		std::string wstr(word);
		if (dictionary.count(wstr)) {
			count += countcandidates(parts + 1, wstr);
		}
	}

	return count;
}

int main()
{
	scanf("%d%d%d", &wordlen, &dictsize, &numcases);

	for (int word = 0; word < dictsize; word++) {
		scanf("%s", input);
		for (int l = wordlen; l; l--) {
			input[l] = 0;
			dictionary.insert(input);
		}
	}

	for (int numcase = 1; numcase <= numcases; numcase++) {
		getpattern();
		printf("Case #%d: %d\n", numcase, countcandidates(0, ""));
	}
}
