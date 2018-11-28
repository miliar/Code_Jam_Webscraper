#include <iostream>
#include <vector>
#include <string>
using namespace std;

string pat;

vector <string> word;

bool pg[20][30];
bool cw[5005][20][30];

int precalc()
{
	memset(cw, 0, sizeof cw);
	for (int i = 0; i < word.size(); ++i)
		for (int j = 0; j < word[i].size(); ++j)
			cw[i][j][word[i][j] - 'a'] = true;
}

int gentok(string& x)
{
	int p = 0, b = 0;
	memset(pg, 0, sizeof pg);	
	for (int i = 0; i < x.size(); ++i)
	{
		if (x[i] == '(') { b = 1; continue; }
		if (x[i] == ')')
		{
			p++;
			b = 0;
			continue;			
		}
		pg[p][x[i] - 'a'] = true;
		if (!b) ++p;
	}
}

int main()
{
	int L, D, N, cnt;
	
	freopen("f:/ain.txt", "r", stdin);
	freopen("f:/ao.txt", "w", stdout);
	
	cin >> L >> D >> N;
	
	int T, i;
	string tw;	
	for (i = 0; i < D; ++i)
	{
		cin >> tw;
		word.push_back(tw);
	} 
	
	sort(word.begin(), word.end());
	precalc();
	for (T = 1; T <= N; ++T)
	{
		cnt = 0;
		cin >> pat;
		gentok(pat);
		
		for (i = 0; i < word.size(); ++i)
		{
			int flag = 1;
			for (int x = 0; x < L; ++x)
				if (pg[x][word[i][x] - 'a'] == 0) { flag = 0; break; }
			cnt += flag;
		}
		cout << "Case #" << T << ": " << cnt << endl;
	}
	
}
