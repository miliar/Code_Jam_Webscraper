#include <cstdio>
#include <memory.h>
#include <vector>
#include <queue>
using namespace std;

char Input[1024];

char TheText[] = "welcome to code jam";
const int TextLength = 18;

class Letter
{
public:
	Letter()
	{
		memset(VariantsForLength, 0, sizeof(VariantsForLength));
	}
	char code;
	vector<int> LettersAfter[30];
	long long VariantsForLength[TextLength+1];
};



long long Result;


int main(void)
{
	//freopen("TaskC.in", "rt", stdin);
	//freopen("C-small-attempt0.in", "rt", stdin);
	//freopen("C-small-attempt1.in", "rt", stdin);
	freopen("C-large.in", "rt", stdin);
	freopen("TaskC.out", "wt", stdout);
	for(int i = 0; i <= TextLength; i++)
	{
		if(TheText[i] == ' ') TheText[i] = 29;
		else				  TheText[i] -= 'a';
	}

	
	int N;
	scanf("%d\n", &N);
	for(int Test = 0; Test < N; Test++)
	{
		Letter PreparedInput[1024];

		Result = 0;

		printf("Case #%d: ", Test+1);
		gets(Input);
		int Len = strlen(Input);
		for(int i = Len-1; i >= 0; i--)
		{
			int code = 29;
			if(Input[i] != ' ') code = Input[i] - 'a';

			PreparedInput[i].code = code;

			for(int j = 0; j < i; j++)
			{
				PreparedInput[j].LettersAfter[code].push_back(i);
			}
		}

		for(int TextI = TextLength; TextI >= 0; TextI --)
		{
			for(int i = 0; i < Len; i++)
			{
				if(PreparedInput[i].code == TheText[TextI])
				{
					long long SubResult = 0;

					if(TextI == TextLength)
					{
						PreparedInput[i].VariantsForLength[TextI] = 1;
					}
					else
					{
						char NextCode = TheText[TextI+1];
						for(int j = 0; j < PreparedInput[i].LettersAfter[NextCode].size(); j++)
						{
							int Value = PreparedInput[PreparedInput[i].LettersAfter[NextCode][j]].VariantsForLength[TextI+1];
							SubResult = SubResult + Value;
							SubResult %= 10000;
						}
						PreparedInput[i].VariantsForLength[TextI] = SubResult;
					}
				}
			}
		}
		for(int i = 0; i < Len; i++)
		{
			if(PreparedInput[i].code == TheText[0])
			{
				Result += PreparedInput[i].VariantsForLength[0];
				Result %= 10000;
			}
		}
		/*if(Result < 1000) printf("0");
		if(Result < 100) printf("0");
		if(Result < 10) printf("0");*/
		printf("%0.4d\n", Result);
	}
	return 0;
}