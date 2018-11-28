#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Token
{
public:
	int length;
	char *letters;

	Token()
	{
		length = 0;
		letters = 0;
	}

	void toString()
	{
		cout<<"Len:"<<length<<'\t';
		for(int i = 0; i < length; i++)
			cout<<letters[i]<<'\t';
	}

	int match(char c)
	{
		for(int i = 0; i < length; i++)
		{
			if(letters[i] == c) return 1;
		}

		return 0;
	}

	~Token()
	{
		delete[] letters;
	}
};

class Pattern
{
public:
	int length;
	Token *tokens;

	Pattern()
	{
		length = 0;
		tokens = 0;
	}

	Pattern(int len, string str_pattern)
	{
		set(len, str_pattern);
	}

	void set(int len, string str_pattern)
	{
		length = len;
		tokens = new Token[length];
		read(str_pattern);
	}

	void read(string str_pattern)
	{
		int p = 0;
		for(int i = 0; i < length; i++)
		{
			if(p >= str_pattern.length())
				break;
			if(str_pattern[p] == '(')
			{
				p++;
				tokens[i].length = 0;
				while(str_pattern[p] != ')' && p < str_pattern.length())
				{
					tokens[i].length ++;
					p++;
				}
				if(tokens[i].length != 0)
				{
					tokens[i].letters = new char[tokens[i].length];
					for(int j = 0; j < tokens[i].length; j++)
					{
						tokens[i].letters[j] = str_pattern[p - tokens[i].length + j];
					}
				}
				p++;
			}
			else if(str_pattern[p] == ')')
			{
				p++;
			}
			else
			{
				tokens[i].length = 1;
				tokens[i].letters = new char[tokens[i].length];
				tokens[i].letters[0] = str_pattern[p];
				p++;
			}
		}
	}

	int match(string str_word)
	{
		for(int i = 0; i < length; i++)
		{
			if(tokens[i].match(str_word[i]) == 0) return 0;
		}
		return 1;
	}

	void toString()
	{
		cout<<"Pattern:"<<endl;
		for(int i = 0; i < length; i++)
		{
			cout<<"Token #"<<i + 1<<':'<<'\t';
			tokens[i].toString();
			cout<<endl;
		}
		cout<<endl;
	}

	~Pattern()
	{
		if(tokens != 0)
			delete[] tokens;
	}
};

int L, D, N;
int *match;
string *words;
string *patterns;

char *infilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Alien Language\\test.in";
char *outfilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Alien Language\\out.txt";

void readfile();
void writefile();
void init();

void main()
{
	readfile();
	init();
	writefile();
}

void readfile()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}
	infile>>L>>D>>N;
	infile.close();

	infile.open(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}
	char skip[20];
	infile.getline(skip, 20);
	words = new string[D];
	patterns = new string[N];
	for(int i = 0; i < D; i++)
	{
		getline(infile, words[i], '\n');
	}
	for(i = 0; i < N; i++)
	{
		getline(infile, patterns[i], '\n');
	}
	infile.close();
}

void writefile()
{
	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}
	for(int i = 0; i < N; i++)
	{
		outfile<<"Case #"<<i + 1<<": "<<match[i]<<'\n';
	}
	outfile.close();
}

void init()
{
	match = new int[N];
	for(int i = 0; i < N; i++)
	{
		match[i] = 0;
	}
	Pattern *p;
	for(i = 0; i < N; i++)
	{
		p = new Pattern();
		p->set(L, patterns[i]);
		for(int j = 0; j < D; j++)
		{
			match[i] += p->match(words[j]);
		}
		delete p;
	}
}