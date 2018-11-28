#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>

#define MAX 16

using namespace std;
FILE *in; FILE *out;

struct Set
{
	int ans;
	vector <string> words;
};

int n, m;
vector <string> init;
vector <string> words[MAX];
map < string, int > position;

string eval(string letters)
{
	int best = -1;
	string ret = "boo";
	
	vector < Set > a;
	for (int len = 0; len < MAX; len++) if (words[len].size() > 0)
	{
		Set add;
		add.ans = 0;
		add.words = words[len];
		a.push_back(add);
	}

	for (int idx = 0; idx < (int)letters.size(); idx++)
	{
		if (a.size() == 0) break;
		for (int i = 0; i < (int)a.size(); i++)
		{
			if (a[i].ans > best)
			{
				best = a[i].ans;
				ret = a[i].words[0];
			}
			if (a[i].ans == best)
			{
				for (int c = 0; c < (int)a[i].words.size(); c++)
					if (position[ret] > position[a[i].words[c]])
						ret = a[i].words[c];
			}
		}
		
		vector < Set > rep;
		for (int i = 0; i < (int)a.size(); i++) if (a[i].words.size() > 1)
		{
			int found = 0;
			for (int c = 0; c < (int)a[i].words.size(); c++)
				for (int j = 0; j < (int)a[i].words[c].size(); j++)
					if (a[i].words[c][j] == letters[idx]) found = 1;
			
			if (!found)
			{
				rep.push_back(a[i]);
				continue;
			}
			
			map < int, vector <string> > sep;
			for (int c = 0; c < (int)a[i].words.size(); c++)
			{
				int mask = 0;
				for (int j = 0; j < (int)a[i].words[c].size(); j++)
					if (a[i].words[c][j] == letters[idx]) mask |= (1 << j);
				sep[mask].push_back(a[i].words[c]);
			}
			
			for (map < int, vector <string> > :: iterator it = sep.begin(); it != sep.end(); it++)
			{
				Set add;
				add.ans = a[i].ans + !it->first;
				add.words = it->second;
				rep.push_back(add);
			}
		}
		a = rep;
	}
	
	/*
	for (int wrd = 0; wrd < (int)init.size(); wrd++)
	{
//		cout << "Trying word " << init[wrd] << endl;

		int len = (int)init[wrd].size();
		vector <int> lett(26, 0);
		set < pair <string, int> > poss;
		
		for (int i = 0; i < (int)words[len].size(); i++)
		{
			for (int c = 0; c < (int)words[len][i].size(); c++)
				lett[words[len][i][c] - 'a']++;
			poss.insert(make_pair(words[len][i], len));
		}
		
		int cur = 0, idx = -1;
		while (poss.size() > 1)
		{
			idx++;
			if (lett[letters[idx] - 'a'] <= 0) continue;
			
			int found = 0;

			for (int i = 0; i < (int)init[wrd].size(); i++)
				if (init[wrd][i] == letters[idx]) found = 1;
			cur += !found;

//			cout << "idx is " << idx << " with letters " << letters << endl;
//			cout << "  -- trying character " << letters[idx] << endl;
//			cout << "  -- remaining words are:";
//			for (set < pair <string, int> > :: iterator it = poss.begin(); it != poss.end(); it++)
//				cout << " " << it->first;
//			cout << endl;

			set < pair <string, int> > rep;
			for (set < pair <string, int> > :: iterator it = poss.begin(); it != poss.end(); it++)
			{
				int cnt = 0, diff = 0;
				for (int i = 0; i < len; i++)
				{
					if ((it->first[i] == letters[idx]) == (init[wrd][i] == letters[idx]))
						cnt += (it->first[i] == letters[idx]);
					else diff = 1;
				}
				if (diff == 1)
				{
					for (int i = 0; i < len; i++)
						lett[it->first[i] - 'a']--;
				}
				else
				{
					if (it->second - cnt > 0)
						rep.insert(make_pair(it->first, it->second - cnt));
				}
			}
			poss = rep;
		}
//		cout << " -- current answer is " << cur << endl;
		if (best < cur) {best = cur; ret = init[wrd];}
	}
	*/
	return ret;
}

void doWork(int testNum)
{
	init.clear();
	position.clear();
	for (int i = 0; i < MAX; i++)
		words[i].clear();
	
	fscanf(in, "%d %d", &n, &m);
	for (int i = 0; i < n; i++)
	{
		char buff[32];
		fscanf(in, "%s", buff);
		init.push_back(buff);
		words[(int)strlen(buff)].push_back(buff);
		position[buff] = i;
	}
	
	vector <string> ans;
	for (int i = 0; i < m; i++)
	{
		char buff[32];
		fscanf(in, "%s", buff);
		ans.push_back(eval(buff));
	}
	
	for (int i = 0; i < (int)ans.size(); i++)
		fprintf(out, "%s%c", ans[i].c_str(), i + 1 == (int)ans.size() ? '\n' : ' ');
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("TheKillerWord.in", "rt");
	out = fopen("TheKillerWord.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
