#include <ctime>
#include <queue>
#include <cassert>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cassert>
#include <utility>

using namespace std;

const int M = 10009;

#define forn(i, n) for (int i = 0; i < int(n); i++)

int k;
int n;
string s;
vector<string> w;

vector< map<char,int> > p;
vector<int> result;

void readData()
{
	cin >> s;
    cin >> k;
    cin >> n;

    w.resize(n);
    forn(i, n)
    	cin >> w[i];

    result = vector<int>(k, 0);
}

long long pw(long long a, int n)
{
	long long result = 1;
    forn(i, n)
    	result = (result * a) % M;
    return result;
}

long long fac(int n)
{
	long long result = 1;
    forn(i, n)
    	result = (result * (i + 1));
    return result;
}

long long fac(int n, vector<string> s)
{
	map<string,int> z;
    forn(i, s.size())
    	z[s[i]]++;

	long long result = fac(s.size());

    for (map<string,int>::iterator it = z.begin(); it != z.end(); it++)
    	result /= fac(it->second);
    return result;
}

int value(vector<string> s)
{
	int sum = 0;
    forn(i, p.size())
    {
    	int add = 1;
        map<char,int> t;
    	forn(j, s.size())
        {
        	forn(f, s[j].length())
            {
                if (p[i].count(s[j][f]) > 0)
                {
                    t[s[j][f]]++;
                }
            }
        }
        for (map<char,int>::iterator it = p[i].begin(); it != p[i].end(); it++)
        {
			add = add * pw(t[it->first], it->second);
            add %= M;
        }
        sum += add;
        sum %= M;
    }
    return sum;
}

vector<string> now;

void rec(int idx, int g)
{
	if (idx == n)
    {
    	result[g - 1] += fac(g, now) * value(now);
        result[g - 1] %= M;
        return;
    }
	if (g < k)
    {
    	now.push_back(w[idx]);
        rec(idx, g + 1);
        now.pop_back();
    }
    rec(idx + 1, g);
}

void solve()
{
	p.clear();

    s += "+";

    map<char,int> z;
    forn(i, s.length())
    {
    	if (s[i] != '+')
        {
        	z[s[i]]++;
        }
        else
        {
        	p.push_back(z);
        	z.clear();
        }
    }

    rec(0, 0);
}

int main(int argc, char* argv[])
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

	int beginIndex = atoi(argv[1]);
	int endIndex = atoi(argv[2]);

	int testCount;

	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &testCount);
	
	for (int tt = 1; tt <= testCount; tt++)
	{
		readData();

		if (beginIndex <= tt && tt <= endIndex)
		{
            cerr << "[" << clock() << "]\tRunning test " << tt << " (" << tt - beginIndex + 1 
                << " out of " << endIndex - beginIndex + 1 << ")..." << endl;
            int from = clock();
			
            solve();

            cerr << "\tCompleted in " << clock() - from << " ms." << endl;

			printf("Case #%d:", tt);
            forn(i, k)
            	cout << " " << result[i];
            printf("\n");
		}
	}

	fclose(stdin);
    fclose(stdout);
	
    return 0;
}
