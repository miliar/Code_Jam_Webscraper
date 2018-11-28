#include <iostream>
#include <string>

using namespace std;

const char NO_ENTRY   = 0;
const size_t TABLE_SIZE = 26*26;
const size_t MAX_SIZE = 101;

void cleartable(char table[TABLE_SIZE]);
inline int hf(char a, char b);
void clearremovemap(size_t map[26]);

int main(int argc, char ** argv, char ** env)
{
	int T, C, D, N;
	cin >> T;
	string in;
	char table[TABLE_SIZE];
	char buffr[MAX_SIZE];
	uint32_t chrs;
	uint32_t numchrs_map[26];
	uint32_t remove_map[26];
	for(int t=1; t<=T; ++t)
	{
		cin >> C;
		cleartable(table);
		clearremovemap(remove_map);
		clearremovemap(numchrs_map);
		chrs = 0;
		for(int c=0; c<C; ++c)
		{
			cin >> in;
			table[hf(in[0], in[1])] = in[2];
			table[hf(in[1], in[0])] = in[2];
		}
		cin >> D;
		for(int d=0; d<D; ++d)
		{
			cin >> in;
			remove_map[ in[0] - 'A' ] |= 1<<(in[1]-'A');
			remove_map[ in[1] - 'A' ] |= 1<<(in[0]-'A');
		}
		cin >> N;
		cin >> in;
		size_t b=0;
		size_t len = in.size();
		clearremovemap(numchrs_map);
		for(size_t n=0; n<len; ++n)
		{
			buffr[b++] = in[n];
			++numchrs_map[in[n]-'A'];
			chrs |= 1<<(in[n]-'A');
			while (b>1 && table[hf(buffr[b-1], buffr[b-2])] != NO_ENTRY)
			{
				if(--numchrs_map[buffr[b-1]-'A'] == 0)
					chrs &= ~(1<<(buffr[b-1]-'A'));
				if(--numchrs_map[buffr[b-2]-'A'] == 0)
					chrs &= ~(1<<(buffr[b-2]-'A'));
				buffr[b-2] = table[hf(buffr[b-1], buffr[b-2])];
				chrs |= 1<<(buffr[b-2]-'A');
				--b;
			}
			if (chrs & remove_map[buffr[b-1]-'A'] )
			{
				clearremovemap(numchrs_map);
				chrs = 0;
				b=0;
			}
		}
		cout << "Case #" << t << ": [";
		for(size_t b1 = 0; b1<b; ++b1) 
		{
			cout << buffr[b1];
			if(b1 < b-1)
				cout << ", ";
		}
		cout << ']' << endl;
	}
	return 0;
}

void cleartable(char table[TABLE_SIZE])
{
	for(size_t i=0; i<TABLE_SIZE; ++i)
		table[i] = NO_ENTRY;
}

inline int hf(char a, char b)
{
	return (a - 'A') * 26 + b - 'A';
}

void clearremovemap(size_t map[26])
{
	for(int i=0; i<26; ++i)
	{
		map[i] = 0;
	}
}

