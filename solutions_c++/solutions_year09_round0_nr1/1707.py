
#include <string.h>
#include <stdio.h>

int L, D, N;

struct dtnode
{
	int term;
	dtnode* alf[26];
	dtnode() : term(0) { memset(alf, 0, sizeof(alf)); }
};

dtnode root;

void initDict()
{
	memset(&root, 0, sizeof(dtnode));
}

void insertWord(char *w)
{
	int l = strlen(w);
	dtnode *t = &root;
	for (int i = 0; i < l; i++)
	{
		if (t->alf[w[i]-'a'] == NULL)
			t->alf[w[i]-'a'] = new dtnode();
		t = t->alf[w[i]-'a'];
		if (i == l-1)
			t->term = 1;
	}
}

int findWord(char *w, int l)
{
	dtnode *t = &root;
	for (int i = 0; i < l; i++)
	{
		if (t == NULL)
			return 0;
		if (t->alf[w[i]-'a'] == NULL) // no prefix is found
			return 0;
		t = t->alf[w[i]-'a'];
	}
	return 2-t->term;
}

void test()
{
	initDict();
	insertWord("aba");
	insertWord("abaa");
	insertWord("acba");
	insertWord("abca");
}

char curWord[30];
int idx = 0;

int findWordRec(char *w)
{
	int l = strlen(w);
	int i, j;
	int res = 0;
	if (l == 0)
	{
		int r = findWord(curWord, idx);
		return (r == 1);
	}
	for (i = 0; i < l; )
	{
		if (w[i] == '(')
		{
			j = i+1;
			while (w[j]!=')') j++; //shouldn't overrun
			for (i = i+1; i < j; i++)
			{
				curWord[idx] = w[i];
				idx++;
				if (findWord(curWord, idx) > 0) //prefix or full word
					res += findWordRec(&w[j+1]);
				idx--;
			}
			i = i+1;
			return res;
		}
		else
		{
			curWord[idx] = w[i];
			idx++;
			if (findWord(curWord, idx) == 0)
				return 0;
			res += findWordRec(&w[i+1]);
			idx --;
			return res;
		}
	}
	return res;
}
int main()
{
	FILE *fp=fopen("A-small-attempt0.in", "rt");
	FILE *fpo=fopen("output.out", "wt");
	fscanf(fp, "%d%d%d", &L, &D, &N); 
	for (int i = 0; i < D; i++)
	{
		char word[100];
		fscanf(fp,"%s", word);

		insertWord(word);
	}

	for (int i = 0; i < N; i++)
	{
		char word[1000];
		fscanf(fp,"%s", word);
		idx = 0;
		memset(curWord, 0 , 30);
		int res = findWordRec(word);
		fprintf(fpo, "Case #%d: %d\n", i+1, res);
	}
	fclose(fp);
	fclose(fpo);
}
