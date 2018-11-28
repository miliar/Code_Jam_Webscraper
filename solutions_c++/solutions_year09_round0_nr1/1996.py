#include <iostream>
#include <fstream>
#include <string>

char GET_LETTER_INDEX(char);
#define LETTERS 26
#define LEFT_PAREN '('
#define RIGHT_PAREN ')'
#define GET_LETTER_INDEX(x) ((x)-97)

using namespace std;

class Letter
{
private:
	Letter *next[LETTERS];
public:
	Letter();
	~Letter();
	void insert(const string *const, unsigned int);
	const int find_count(const string *const, unsigned int);
};
Letter::Letter()
{
	memset(next, 0, LETTERS*sizeof(Letter *));
}
Letter::~Letter()
{
	int i;
	for (i=0; i<LETTERS; i++)
		delete next[i];
}
void Letter::insert(const string *const str, unsigned int pos = 0)
{
	Letter *n = next[GET_LETTER_INDEX(str->operator[](pos))];
	if (!n)
	{
		n = new Letter();
		next[GET_LETTER_INDEX(str->operator[](pos))] = n;
	}
	if (++pos < str->length())
		n->insert(str, pos);
}
static int find_helper(Letter *const child, const string *const buf, unsigned int pos)
{
	if (child)
	{
		if (++pos >= buf->length())
			return 1;
		return child->find_count(buf, pos);
	}
	return 0;
}
const int Letter::find_count(const string *const buf, unsigned int pos = 0)
{
	int count;
	unsigned int open, close;
	char cur = buf->operator[](pos);
	if (cur == LEFT_PAREN)
	{
		count = 0;
		close = buf->find_first_of(RIGHT_PAREN, pos);
		for (open=pos+1; open<close; open++)
			count += find_helper(next[GET_LETTER_INDEX(buf->operator[](open))], buf, close);
		return count;
	}
	else
		return find_helper(next[GET_LETTER_INDEX(cur)], buf, pos);
}

int main(const int argc, const char *const argv[])
{
	ifstream in;
	int L, D, N, i;
	string buf;
	Letter dictionary;
	if (argc < 2)
		return -1;
	in.open(argv[1]);
	in >> L >> D >> N;
	for (i=0; i<D; i++)
	{
		in >> buf;
		dictionary.insert(&buf);
	}
	for (i=0; i<N;)
	{
		in >> buf;
		cout << "Case #" << ++i << ": " << dictionary.find_count(&buf) << endl;
	}
	in.close();
	return 0;
}
