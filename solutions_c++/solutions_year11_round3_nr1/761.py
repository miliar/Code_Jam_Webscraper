#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{

    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        cout<<"Case #"<<t+1<<":"<<endl;
         
        int R, C;
        cin>>R>>C;
        vector<vector<char> > v(R, vector<char>(C));

        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                char c;
                cin>>c;
                v[i][j] = c;
            }
        }

        for(int i=0;i<R-1;i++)
        {
            for(int j=0;j<C-1;j++)
            {
                if(v[i][j] == '#')
                {
                    if(v[i][j+1]=='#' && v[i+1][j] == '#' && v[i+1][j+1] == '#')
                    {
                        v[i][j] = v[i+1][j+1] = '/';
                        v[i][j+1] = v[i+1][j] = '\\';
                    }
                }

            }

        }
        bool f = false;
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(v[i][j] == '#')
                {
                    f = true;
                }
            }
        }
        if (f)
        {
            cout<<"Impossible";
        }
        else
        {
            for(int i=0;i<R-1;i++)
            {
                for(int j=0;j<C;j++)
                {
                    cout<<v[i][j];
                }
                cout<<endl;
            }
            for(int i=R-1;i<R;i++)
                for(int j=0;j<C;j++)
                {
                    cout<<v[i][j];
                }
        }



        cout<<endl;
    }
    return 0;
}
