#include<iostream>
#include<string>
#include<vector>
using namespace std;

void print(int i, string str)
{
    cout << "Case #" << i << ": " << str << endl;
}

/*
 * 0 - X won
 * 1 - O won
 * 2 - otherwise
 */
int check( string str)
{
    bool is_x = true;
    bool is_y = true;

    for (int i=0;i<str.size();++i)
    {
        if ( str[i] == '.') return 2;
        if ( str[i] == 'X') is_y=false;
        if ( str[i] == 'O') is_x=false;
    }

    return is_x ? 0 : (is_y ? 1 : 2);
}

int main()
{
    int T;
    cin >> T;
    string str;
    getline(cin, str);
    for (int t=0;t<T;++t)
    {
        vector<string> vs;
        for (int j=0;j<4;++j)
        {
            getline(cin, str);
            vs.push_back(str);
        }
        getline(cin,str);

        bool is_x = false;
        bool is_o = false;
        for (int i=0;i<4;++i)
        {
            str = "";
            for (int j=0;j<4;++j)
            {
                str += vs[i][j];
            }
            if ( check(str) == 0)
            {
                is_x = true;
            } else if ( check(str) == 1)
            {
                is_o = true;
            }
        }
        
        for (int i=0;i<4;++i)
        {
            str = "";
            for (int j=0;j<4;++j)
            {
                str += vs[j][i];
            }
            if ( check(str) == 0)
            {
                is_x = true;
            } else if ( check(str) == 1)
            {
                is_o = true;
            }
        }
            
        str = "";
        for (int i=0;i<4;++i)
        {
            str += vs[i][i];
        }
        if ( check(str) == 0)
        {
            is_x = true;
        } else if ( check(str) == 1)
        {
            is_o = true;
        }
        
        str = "";
        for (int i=0;i<4;++i)
        {
            str += vs[i][3-i];
        }
        
        if ( check(str) == 0)
        {
            is_x = true;
        } else if ( check(str) == 1)
        {
            is_o = true;
        }

        if ( is_x)
        {
            print(t+1, "X won");
            continue;
        }

        if ( is_o)
        {
            print(t+1, "O won");
            continue;
        }

        bool draw = true;
        for (int i=0;i<4;++i)
        {
            for (int j=0;j<4;++j)
            {
                if ( vs[i][j] == '.') draw=false;
            }
        }

        if ( draw)
        {
            print( t+1, "Draw");
            continue;
        }

        print( t+1, "Game has not completed");
    }

}

