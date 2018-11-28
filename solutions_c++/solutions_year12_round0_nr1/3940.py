#include <cstdio>
#include <cstring>
#define MAX 1000
using namespace std;

char key['z'+10];
char line[MAX];

void break_cipher()
{
    key['y'] = 'a';
    key['e'] = 'o';
    key['q'] = 'z';
    key['z'] = 'q';

    FILE *fkey = fopen("A.key", "r");
    char cipher[MAX], plain[MAX];
    for(int i = 0; i < 3; i++)
    {
        fgets(cipher, MAX, fkey);
        fgets(plain, MAX, fkey);
        for(int j = 0; cipher[j]; j++)
            if (cipher[j] != ' ' && cipher[j] != '\n')
                key[cipher[j]] = plain[j];
    }
}

void decrypt()
{
    for(int i = 0; line[i] ; i++)
        if (line[i] != ' ' && line[i] != '\n')
            line[i] = key[line[i]];
}

int main()
{
	break_cipher();
	int T; scanf("%d ", &T);
	for(int t = 1; t <= T; t++)
    {
        gets(line);
        decrypt();
        printf("Case #%d: %s\n", t, line);
    }
	return 0;
}
