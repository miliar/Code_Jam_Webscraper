
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <regex.h>

using namespace std;

#ifdef LARGE

#define FILE_NAME	"A-large.in"
#define FILE_OUT	"A-large.out"

#else
#define FILE_NAME	"A-small-attempt0.in"
#define FILE_OUT	"A-small.out"
#endif


int match_regular_expression(const char *regex, const char *str)
{
	regex_t er;
	int ret_val = 0;
	
	regcomp(&er, regex, REG_EXTENDED|REG_NOSUB);
	
	if (regexec(&er, str, 0, NULL, 0) == 0)
		ret_val = 1;
	
	regfree(&er);
	
	return ret_val;
}


int main()
{
	int num_letters;
	int num_words;
	int num_cases;
	FILE *fp_in, *fp_out;
	int i, j;
	int match = 0, test_case = 1;
	bool ok_insert = false;
	char aux_str[70];
	
	fp_in = fopen(FILE_NAME, "r");
	fp_out = fopen(FILE_OUT, "w");
	
	fscanf(fp_in, "%d %d %d", &num_letters, &num_words, &num_cases);
	printf("%d %d %d\n", num_letters, num_words, num_cases);

	char words[num_words][30];
	vector<string> cases(num_cases);
	string::iterator p_str;

	for (i = 0; i < num_words; i++) {
		fscanf(fp_in, "%s", &words[i][0]);
		//printf("%s\n", &words[i][0]);
	}
	
	/* read test cases */
	for (i = 0; i < num_cases; i++) {
		fscanf(fp_in, "%s", aux_str);
		cases[i] = aux_str;
		
		p_str = cases[i].begin();
		while (p_str < cases[i].end()) {
			
			if (*p_str == '(' || ok_insert == true) {
				ok_insert = true;
				
				if (*p_str == '(')
					p_str++;
				
				if ( (*p_str != '(') && (*p_str != ')') && ((p_str+1) != cases[i].end())
					  && (*(p_str + 1) != '(') && (*(p_str+1) != ')')) {
					
					p_str++;
					p_str = cases[i].insert(p_str, '|');
					p_str++;
				} else {
					p_str++;
					ok_insert = false;
				}
			} else {
				p_str++;	
			}
		}
		
		//cout << cases[i] << endl;
		for (j = 0; j < num_words; j++) {
			if (match_regular_expression(cases[i].c_str(),  &words[j][0]))
				match++;
		}
		fprintf(fp_out, "Case #%d: %d\n", test_case, match);
		test_case++;
		match = 0;
	}
	
	fclose(fp_in);
	fclose(fp_out);
	
	return 0;
}
