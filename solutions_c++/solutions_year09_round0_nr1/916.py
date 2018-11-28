#include <cstdio>
#include <vector>
#include <set>
#include <string>

using namespace std;

int result;

typedef vector<char> pos_letter;

vector<pos_letter> recv;
set<string> dic;

void solvefor(int L, int t, char* buffer)
{
	if (L == t)
	{
		++result;
		return ;
	}

	for(int i = 0; i < recv[t].size(); ++i)
	{
		buffer[t] = recv[t][i];
		buffer[t+1] = '\0';

		if (dic.find(buffer) != dic.end())
			solvefor(L, t+1, buffer);
	}
}

void solve(int L, char* inp)
{
	recv.clear();

	while(*inp)
	{
		pos_letter let;
		if (*inp == '(')
		{
			while(*(++inp) != ')')
			{
				let.push_back(*inp);
			}
		}
		else
			let.push_back(*inp);
		recv.push_back(let);
		++inp;
	}

	char buffer[1024];
	solvefor(L, 0, buffer);
}

void make_dic(char* word)
{
	char temp[1024] = {0};
	int len = 0;
	while(*word)
	{
		temp[len++] = *word++;
		dic.insert(temp);
	}
}

int main()
{
	freopen("D:/downloads/A-large.in", "r", stdin);
	freopen("C:/Users/kiheon/Desktop/output.txt", "w", stdout);

	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);
	for(int i = 0; i < D; ++i)
	{
		char word[1024];
		scanf("%s", &word);

		make_dic(word);
	}

	for(int i = 0; i < N; ++i)
	{
		char inp[1024];
		scanf("%s", &inp);
		result = 0;
		solve(L, inp);
		printf("Case #%d: %d\n", i+1, result);
	}
}