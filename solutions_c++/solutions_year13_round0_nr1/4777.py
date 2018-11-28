#include <iostream>
#include <string>

using namespace std;

int A[5][5];


void go (int t)
{
    bool full = true;
    for (int i =0; i<4; i++)
    {
	string s; cin >> s;
	for (int j=0; j<4; j++)
	{
	    if (s[j] == '.')
	    {
		A[i][j] = - 1;
		full = false;
	    }else if (s[j] == 'O')
		A[i][j] = 0;
	    else if (s[j] == 'X')
		A[i][j] = 1;
	    else if (s[j] == 'T')
		A[i][j] = 2;
	}
    }

    bool win = false;
    for (int k = 0; k < 2; k++)
    {
	bool ok = false;
	for (int i=0; i<4; i++)
	{
	    bool c1 = true, c2 = true;
	    for (int j=0; j<4; j++)
	    {
		if (A[i][j] == 1 - k or A[i][j] == -1)
		    c1 = false;
		if (A[j][i] == 1 - k or A[j][i] == -1)
		    c2 = false;
	    }
	    if (c1 or c2)
		ok = true;
	}
	bool c3 = true, c4 = true;
	for (int j=0; j<4; j++)
	{
	    if (A[j][j] == 1 - k or A[j][j] == -1)
		c3 = false;
	    if (A[j][3 - j] == 1 - k or A[j][3 - j] == -1)
		c4 = false;
	}
	if (c3 or c4)
	    ok = true;
	if (ok)
	{
	    printf ("Case #%d: %c won\n", t, (k == 1 ? 'X' : 'O'));
	    win = true;
	    break;
	}
    }
    if (!win)
    {
	if (full)
	    printf ("Case #%d: Draw\n", t);
	else
	    printf ("Case #%d: Game has not completed\n", t); 
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++)
    {
	go (i + 1);
    }
}
