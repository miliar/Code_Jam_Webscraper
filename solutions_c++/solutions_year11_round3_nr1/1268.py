#include <iostream>
using namespace std;

int main()
{   int cases = 0;
    long m,n,t;
    cin>>t;
    while (t--)
    {   cin >> m >> n;
        bool possible = true;
        cases++;
        char arr[m][n];
        for (int i = 0; i < m; i++)
        {       for (int j = 0; j < n; j++)
                {   cin >> arr[i][j];
                }
        }
        //search
        for (int i = 0; i < m; i++)
        {   for (int j = 0; j < n; j++)
            {   if (arr[i][j] == '#')
                {   if ((arr[i][j+1] == '#')&&(arr[i+1][j] == '#')&& (arr[i+1][j+1] == '#'))
                    {   arr[i][j] = arr[i+1][j+1] = '\/';
                        arr[i+1][j] = arr[i][j+1] = '\\';
                    }
                    else
                    {   possible = false;
                        break;
                    }
                }
            }
        }
        if (!possible)
            cout << "Case #" << cases << ":\nImpossible" << endl;
        else
        {   cout << "Case #" << cases << ":" << endl;
            for (int i = 0; i < m; i++)
            {       for (int j = 0; j < n; j++)
                    {   cout << arr[i][j];
                    }
                    cout << endl;
            }
        }
    }
    return 0;
}
