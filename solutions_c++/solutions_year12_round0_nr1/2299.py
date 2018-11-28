#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
using namespace std;

void translate(char* input, char* map);

int main(int argc, char** argv)
{

    char const* s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char const* s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    char char_map[26];
    char str[1000];
    FILE *fp1, *fp2;
    int lines;

    for(; *s1 != '\0'; ++s1, ++s2) {
      if(!isspace(*s1))  
				char_map[*s1 - 'a'] = *s2;
    }
		char_map[25] = 'q';
    char_map['q'-'a'] = 'z';
		/*
		for(int i = 0; i < 26; ++i)
			cout << char_map[i] << " ";
 		cout << endl;
		*/
		fp1 = fopen("A-small-attempt5.in","r");
    fp2 = fopen("result.out","w");
    if(fp1 == NULL)
        return 1;
    sscanf(fgets(str, sizeof(str), fp1), "%d", &lines);
    for(int i = 0; i < lines; ++i) {
        fgets(str, sizeof(str), fp1);
				int len = strlen(str) - 1;
				if(str[len] == '\n') str[len] = '\0';
        translate(str, char_map);
        fprintf(fp2, "Case #%d: %s\n", i+1, str);
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}

void translate(char* input, char* map)
{
    for(; *input != '\0'; ++input) {
        if(!isspace(*input))
            *input = map[*input - 'a'];
    }
}
