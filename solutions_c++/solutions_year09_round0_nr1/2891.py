#include <iostream>
#include <list>

using namespace std;

int L, D, N;
list<char*> words;
list<char*>::iterator Iter_word;

int TestWords(char *tmpl)
{
	int count = 0, i;

	list<char*> groups;
	list<char*>::iterator Iter_group;

	for (i=0; i<strlen(tmpl); i++)
	{
		char *w = (char *)malloc( 30 );

		if (tmpl[i] == '(')
		{
			int pos = (int)(strchr(tmpl+i, ')')-tmpl);
			strncpy(w, tmpl+i+1, pos-i-1);
			*(w+pos-i-1) = '\0';
			i = pos;
		}
		else
		{
			strncpy(w, tmpl+i, 1);
			*(w+1) = '\0';
		}

		groups.push_back(w);
	}

	for (Iter_word = words.begin(); Iter_word != words.end(); Iter_word++)
	{
		bool yra = true;

		for (i=0, Iter_group = groups.begin();
			 i<L && Iter_group != groups.end();
			 i++, Iter_group++)
		{
			if (strchr(*Iter_group, (*Iter_word)[i]) == NULL)
			{
				yra = false;
				break;
			}
		}

		if (yra) count++;
	}

	return count;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%d %d %d", &L, &D, &N);

	for(int di=0; di<D; di++)
	{
		char *word = (char *)malloc( L+1 );
		scanf ("%s", word);
		words.push_back(word);
	}

	int count;

	for(int ni=1; ni<=N; ni++)
	{
		char *tmpl = (char *)malloc( L*30 );
		scanf ("%s", tmpl);

		count = TestWords(tmpl);

		cout << "Case #" << ni << ": " << count << endl;
		free(tmpl);
	}

	return 0;
}