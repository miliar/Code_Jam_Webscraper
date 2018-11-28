#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main (int argc, char * const argv[]) 
{
	freopen("input31.txt", "rt", stdin);
	freopen("output31.txt", "wt", stdout);
	
	int T; 
	cin >> T;
	
	for(int i = 0; i < T; i++) 
    {
		int R, C;
		cin >> R;
		cin >> C;
        
        vector <string> pat;
        pat.clear();
        for (int j = 0; j < R; j++)
        {
            string s;
            cin >> s;
            pat.push_back(s);
        }
        
        bool impossible = false;
        for (int j = 0; j < R && impossible == false; j++)
        {
            int c = 0;
            for (int k = 0; k < C; k++)
            {
                if (pat[j][k] == '.')
                {
                    if (c % 2 != 0)
                    {
                        impossible = true;
                        break;
                    }
                    c = 0;
                }
                else
                    c++;
            }
            if (c % 2 != 0)
            {
                impossible = true;
                break;
            }
        }
        if (impossible == false)
        {
            for (int j = 0; j < C && impossible == false; j++)
            {
                int c = 0;
                for (int k = 0; k < R; k++)
                {
                    if (pat[k][j] == '.')
                    {
                        if (c % 2 != 0)
                        {
                            impossible = true;
                            break;
                        }
                        c = 0;
                    }
                    else
                        c++;
                }
                if (c % 2 != 0)
                {
                    impossible = true;
                    break;
                }
            }
        }
        
        cout << "Case #" << i+1 << ":" << endl;
        if (impossible == true)
        {
            cout << "Impossible" << endl;
        }
        else
        {
            for (int j = 0; j < R; j++)
            {
                int c = 0;
                for (int k = 0; k < C; k++)
                {
                    if (pat[j][k] == '#')
                    {
                        if (j == 0 || pat[j-1][k] == '.' || pat[j-1][k] == 'C'|| pat[j-1][k] == 'D')
                        {
                            if (c % 2 == 0)
                                pat[j][k] = 'A';
                            else
                                pat[j][k] = 'B';
                        }
                        else
                        {
                            if (pat[j-1][k] == 'A')
                                pat[j][k] = 'C';
                            else if (pat[j-1][k] == 'B')
                                pat[j][k] = 'D';
                        }
                        c++;
                    }
                    else
                        c = 0;
                }
            }
            for (int j = 0; j < R; j++)
            {
                for (int k = 0; k < C; k++)
                {
                    if (pat[j][k] == 'A' || pat[j][k] == 'D')
                        pat[j][k] = '/';
                    else if (pat[j][k] == 'B' || pat[j][k] == 'C')
                        pat[j][k] = '\\';
                }
            }
            for (int j = 0; j < R; j++)
            {
                cout << pat[j] << endl;
            }
        }
	}
	
	return 0;
}

