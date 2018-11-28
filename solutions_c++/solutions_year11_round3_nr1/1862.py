#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main(){
    int test, r, c;
    char t;
    cin >> test;
    vector< string > grid(0);
    for (int cs = 1; cs <= test; cs++)
    {
        cin >> r >> c;
        string temp;
        int count = 0;
        grid.clear();
        grid.resize(0);
        for (int i = 0; i < r; i++)
        {
            temp = "";
            for (int j = 0; j < c; j++)
            {
                cin >> t;
                temp += t;
                if (t == '#') 
                {
                    count++;
                }
            }
            grid.push_back(temp);
        }
        cout << "Case #" << cs << ":" << endl;
        int flag = 1;
        if (count % 4 != 0)
            cout << "Impossible" << endl;
        else
        {
            for (int i = 0; i < r; i++)
            {
                if (flag == 0) break;
                for (int j = 0; j < c; j++)
                {
                    if (grid[i][j] != '#') continue;
                    if ((j == c-1) || (i == r-1) || (grid[i][j+1] != '#') || (grid[i+1][j] != '#') || (grid[i+1][j+1] != '#'))
                    {  
                        cout << "Impossible" << endl;
                        flag = 0;
                        break;
                    }
                    grid[i][j] = '/';
                    grid[i][j+1] = '\\';
                    grid[i+1][j] = '\\';
                    grid[i+1][j+1] = '/';
                }
            }
            if (flag)
            {
                for (int i = 0; i < r; i++)
                {
                    for (int j = 0; j < c; j++)
                    {
                        cout << grid[i][j];
                    }
                    cout << endl;
                }
            }
        }
    }
    return 0;
}
