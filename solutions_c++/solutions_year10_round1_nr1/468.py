#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

unsigned N, K;

void compact(string::iterator i, string::iterator e)
{
    string::iterator j = i;
    while (i != e)
    {
	if (*i == '.')
	    i++;
	else
	    *j++ = *i++;
    }

    while (j != e)
	*j++ = '.';
}

inline bool in(int i, int j)
{
    return (0 <= i && i < (int)N && 0 <= j && j < (int)N);
}

bool scan(const vector<string>& v, char c)
{
    unsigned m = 0;

    for (unsigned i = 0; i < N; ++i)
    {
	bool con = false;
	unsigned cnt = 0;
	for (unsigned j = 0; j < N; ++j)
	{
	    if (v[i][j] == c)
	    {
		if (con)
		    cnt++;
		else
		{
		    con = true;
		    cnt = 1;
		}
	    }
	    else
	    {
		con = false;
		cnt = 0;
	    }
	    m = max(m, cnt);
	}
    }

    for (unsigned i = 0; i < N; ++i)
    {
	bool con = false;
	unsigned cnt = 0;
	for (unsigned j = 0; j < N; ++j)
	{
	    if (v[j][i] == c)
	    {
		if (con)
		    cnt++;
		else
		{
		    con = true;
		    cnt = 1;
		}
	    }
	    else
	    {
		con = false;
		cnt = 0;
	    }
	    m = max(m, cnt);
	}
    }

    for (unsigned l = 0; l < 2*N-1; ++l)
    {
	bool con = false;
	unsigned cnt = 0;
	for (int i = (int)min(l,N-1), j = max(0,int(l-N+1)); in(i,j); i--, j++)
	{
	    if (v[i][j] == c)
	    {
		if (con)
		    cnt++;
		else
		{
		    con = true;
		    cnt = 1;
		}
	    }
	    else
	    {
		con = false;
		cnt = 0;
	    }
	    m = max(m, cnt);
	}
    }

    for (unsigned l = 0; l < 2*N-1; ++l)
    {
	bool con = false;
	unsigned cnt = 0;
	for (int i = max(0,(int)(N-1-l)), j = max(0,(int)(l-N+1)); in(i,j); i++, j++)
	{
	    if (v[i][j] == c)
	    {
		if (con)
		    cnt++;
		else
		{
		    con = true;
		    cnt = 1;
		}
	    }
	    else
	    {
		con = false;
		cnt = 0;
	    }
	    m = max(m, cnt);
	}
    }

    return m >= K;
}

int main()
{
    unsigned T;
    while (cin >> T)
    {
	for (unsigned t = 1; t <= T; ++t)
	{
	    cin >> N >> K;
	    vector<string> v(N);
	    for (unsigned i = 0; i < N; ++i)
	    {
		string s;
		cin >> s;
		reverse(s.begin(), s.end());
		compact(s.begin(), s.end());
		v[N-1-i] = s;
	    }

	    // for (unsigned i = 0; i < N; ++i)
	    // {
	    // 	cout << v[i] << endl;
	    // }

	    bool r = scan(v, 'R');
	    bool b = scan(v, 'B');

	    string res;
	    if (r && b)
		res = "Both";
	    else if (r)
		res = "Red";
	    else if (b)
		res = "Blue";
	    else
		res = "Neither";

	    cout << "Case #" << t << ": " << res << endl;
	}
    }

    return 0;
}
