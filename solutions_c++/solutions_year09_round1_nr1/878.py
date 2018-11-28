#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define SIZE 20
#define MAX 2000000
int mas[11][MAX];

struct Number
{
	int digits[SIZE];
	int base;
	Number():base(10)
	{
		memset(digits, 0, sizeof(int) * SIZE);
	}

	Number(int a, int aBase) : base(aBase)
	{
		memset(digits, 0, sizeof(int) * SIZE);
		int c = 0;
		while (a > 0)
		{
			digits[c] = a % base;
			a /= base;
			c++;
		}
	}

	Number transform()
	{
		int x = 0;
		for (int i = 0; i < SIZE; i++)
			x += digits[i] * digits[i];
		return Number(x, base);
	}
	long long toLong()
	{
		long long  res = 0;
		for (int i = SIZE - 1; i >= 0; i--)
			res = res * base + digits[i];
		return res;
	}
};

string strings[10];
int strCount;

void split( const string& s, const string& delim =" " ) {
    strCount = 0;
    string t;
    for ( int i = 0 ; i != s.size() ; i++ ) {
        if ( delim.find( s[i] ) != string::npos ) {
            if ( !t.empty() ) {
				strings[strCount] = t;
				strCount++;
                t = "";
            }
        } else {
            t += s[i];
        }
    }
    if ( !t.empty() ) {
		strings[strCount] = t;
		strCount++;
    }
}

vector<int> splitInt( const string& s, const string& delim =" " ) {    
    vector<int> res;
	split(s);
    for ( int i = 0 ; i < strCount; i++ )
        res.push_back( atoi( strings[i].c_str() ) );
    return res;
}

int hist[MAX];

bool isHappy(Number a)
{
	int h = 0;
	bool f = true;
	while (true)
	{
		long long l = a.toLong();
		hist[h] = l;
		h++;
		if (l == 1)
			break;
		if (mas[a.base][l] == 1)
		{
			break;
		}
		if (mas[a.base][l] == 2 || mas[a.base][l] == 3)
		{
			f = false;
			break;
		}
		mas[a.base][l] = 3;
		a = a.transform();
	}
	for (int i = 0; i < h; i++)
		mas[a.base][hist[i]] = f ? 1 : 2;
	return f;
}
set<int> happies[11];

set<int> join (set<int> a, set<int> b)
{
	set<int> res;
	for (set<int>::iterator it = a.begin(); it != a.end(); it++)
	{
		int z = *it;
		if (b.find(z) != b.end())
			res.insert(z);
	}
	return res;

}

int main()
{
	freopen("output.txt", "w", stdout);
	memset(mas, 0, sizeof(int) * MAX * 11);
	for (int i = 2; i < 11; i++)
	{
		//printf("BASE: %d", i);
		for (int j = 2; j < 1000000; j++)
			if (isHappy(Number(j, i)))
			{
				//printf("%d\n", j);
				//happies[i].insert(j);
			}

	}
	int T;
	char s[100];
	scanf("%d", &T);gets(s);
	for (int t = 0; t < T; t++)
	{
		gets(s);
		string ss(s);
		vector<int> v = splitInt(ss);
		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
		/*set<int> res = join(happies[v[0]], happies[v[1]]);
		for (int i = 2; i < v.size(); i++)
			res = join(res, happies[v[i]]);*/
		int res = -1;
		for (int i = 2; i < 1000000; i++)
		{
			bool f = true;
			for (int j = 0; j < v.size(); j++)
				if (mas[v[j]][i] == 2)
				{
					f = false;
					break;
				}
			if (f)
			{
				res = i;
				break;
			}
		}
		if (res == -1)
			printf("ERROR");
		else
			printf("Case #%d: %d\n", t+1, res);		
	}

	fclose(stdout);
	return 0;
}