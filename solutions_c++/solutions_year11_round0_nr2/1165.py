#include <stdio.h>
#include <string.h>

static void input_combine (char combine[26][26])
{
	unsigned n;
	scanf ("%u", &n);
	while (n--) {
		char s[16];
		scanf ("%s", s);
		char a = s[0] - 'A';
		char b = s[1] - 'A';
		char c = s[2];
		combine[a][b] = c;
		combine[b][a] = c;
	}
}

static void input_oppose (char oppose[26])
{
	unsigned n;
	scanf ("%u", &n);
	while (n--) {
		char s[16];
		scanf ("%s", s);
		char a = s[0];
		char b = s[1];
		oppose[a - 'A'] = b;
		oppose[b - 'A'] = a;
	}
}

static void work ()
{
	char combine[26][26] = { {0} };
	char oppose[26] = {0};

	input_combine (combine);
	input_oppose (oppose);

	char result[128];
	unsigned len = 0;
	unsigned inputlen;
	scanf ("%u", &inputlen);
	while (inputlen--) {
		char c;
		scanf (" %c", &c);
		if (len && combine[c-'A'][result[len-1]])
			result[len-1] = combine[c-'A'][result[len-1]] - 'A';
		else if (len && oppose[c-'A'] && memchr (result, oppose[c-'A']-'A', len))
			len = 0;
		else
			result[len++] = c - 'A';
	}
	putchar ('[');
	for (unsigned j=0; j<len; ++j) {
		if (j)
			printf (", ");
		putchar (result[j] + 'A');
	}
	puts ("]");
}

int main ()
{
	unsigned T;
	scanf ("%u", &T);
	for (unsigned k=1; k<=T; ++k) {
		printf ("Case #%u: ", k);
		work ();
	}
	return 0;
}
