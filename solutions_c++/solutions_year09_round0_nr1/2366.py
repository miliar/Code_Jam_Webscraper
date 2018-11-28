#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
	int i,l,k,j;
	int D, N, L;
	string s;
	char word[30];
	vector <string> words;

	bool word_ok[5010];
	scanf("%d %d %d", &L, &D, &N);
	for (i=0; i<D; i++)
	{
		scanf("%s", word);
		string s(word);
		words.push_back(s);
	}

	bool ok;
	char ch;
	char pat[1000];
	int num = 0, pos = 0;
	string str;
	for (i=0; i<N; i++) // testy
	{
		scanf("%s", pat);
		string s(pat);

		for (l=0; l<D; l++) word_ok[l] = true;

		pos = 0;
		for (k=0; k<L; k++) // tokeny
		{
			if (s[pos] == '(') // mamy grupe
			{
				str = "";
				while (s[++pos] != ')') str += s[pos]; // doczytujemy grupe do konca
				pos++;
				for (l=0; l<D; l++) if (word_ok[l]) // dla wszystkich dobrych slow
				{
					ok = false;
					for (j=0; j<str.size(); j++) if (words[l][k] == str[j]) ok = true; // jezeli znak sie zgadza
					if (!ok) word_ok[l] = false;
				}
				//printf("grupa: %s\n", str.c_str());
			}
			else  // mamy znak
			{
				ch = s[pos++];
				//printf("znak: %c\n", ch);
				for (l=0; l<D; l++) if (word_ok[l]) if (words[l][k] != ch) word_ok[l] = false;
			}
		}

		num = 0;
		for (l=0; l<D; l++) if (word_ok[l]) num++;
		printf("Case #%d: %d\n", i+1, num);
	}

	//for (i=0; i<D; i++) printf("%s\n", words[i].c_str());

	char c;
	scanf("%c", &c);
	return 0;
}

