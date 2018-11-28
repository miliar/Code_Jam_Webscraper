#include <cstdio>
#include <memory.h>
#include <vector>
using namespace std;

class VocNode
{
public:
	VocNode()
	{
		memset(Edges, 0, sizeof(Edges));
		IsFinal = false;
	}
	VocNode *Edges[30];

	bool IsFinal;
};

VocNode Root;
int L, D, N;

void AddWord(char *word)
{
	VocNode *current = &Root;
	while(*word)
	{
		*word -= 'a';
		if(current->Edges[*word])
		{
			current = current->Edges[*word];
		}
		else
		{
			current->Edges[*word] = new VocNode();
			current = current->Edges[*word];
		}
		word++;
		if(!*word)
		{
			current->IsFinal = true;
		}
	}
}

struct UnclearLetter
{
	int PossibilitiesNum;
	char *Letters;
};

class UnclearWord
{
public:
	UnclearWord() {Length = 0; }
	UnclearLetter Word[20];
	int Length;
};


int CheckWord(UnclearWord &w, int CurLetter, VocNode *node)
{
	if(CurLetter == w.Length && node->IsFinal) return 1;
	int result = 0;
	for(int i = 0; i < w.Word[CurLetter].PossibilitiesNum; i++)
	{
		VocNode *next =  node->Edges[w.Word[CurLetter].Letters[i]];
		if(!next) continue;

		result += CheckWord(w, CurLetter+1, next);
	}
	return result;
}

int main(void)
{
	//freopen("TaskA.in", "rt", stdin);
	freopen("A-small-attempt0.in", "rt", stdin);
	
	freopen("TaskA.out", "wt", stdout);
	scanf("%d %d %d\n", &L, &D, &N);
	char buf[256];
	for(int i = 0; i < D; i++)
	{
		gets(buf);
		AddWord(buf);
	}

	vector<char> temp;
	temp.reserve(30);
	for(int i = 0; i < N; i++)
	{
		gets(buf);
		char *cur = buf;
		UnclearWord Word;

		while(*cur)
		{
			if(*cur == '(')
			{
				temp.clear();
				cur++;
				while(*cur && *cur != ')')
				{
					temp.push_back(*cur - 'a');
					cur++;
				}
				cur++;
				if(temp.size() > 0)
				{
					//sort(temp.begin(), temp.end());
					Word.Word[Word.Length].PossibilitiesNum = temp.size();
					Word.Word[Word.Length].Letters = new char [temp.size()];
					memcpy(Word.Word[Word.Length].Letters, &temp[0], sizeof(char) * temp.size());
					Word.Length++;
				}
			}
			else
			{
				Word.Word[Word.Length].PossibilitiesNum = 1;
				Word.Word[Word.Length].Letters = new char [1];
				Word.Word[Word.Length].Letters[0] = *cur - 'a';
				Word.Length++;
				cur++;
			}
		}
		printf("Case #%d: %d\n", i+1, CheckWord(Word, 0, &Root));
	}

	return 0;
}