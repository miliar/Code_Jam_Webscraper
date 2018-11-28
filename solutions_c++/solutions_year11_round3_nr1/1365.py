#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main()
{
    int T, t;
    cin >> T;
    for (t=0;t<T;++t)
    {
        int R, C,i,j;
        cin>>R>>C;
        vector<vector<char> > mat(R);
        //bool has_white=false;
        //bool has_blue=false;
        for(i=0;i<R;++i)
        {
            mat[i].reserve(C);
            for(j=0;j<C;++j)
            {
                char ch;
                cin>>ch;
                //if(ch=='#')bas_blue=true;
                //else has_white=true;
                mat[i].push_back(ch);
            }
        }
        cout<<"Case #"<<t+1<<": "<<endl;
        if(R>1&&C>1)
        {
            for(i=0;i<R-1;++i)
            {
                for(j=0;j<C-1;++j)
                {
                    if(mat[i][j]=='#'
                       &&mat[i][j+1]=='#'
                       &&mat[i+1][j]=='#'
                       &&mat[i+1][j+1]=='#')
                    {
                        mat[i][j]='/';
                        mat[i][j+1]='\\';
                        mat[i+1][j]='\\';
                        mat[i+1][j+1]='/';
                    }
                }
            }
            for(i=0;i<R;++i)
            {
                for(j=0;j<C;++j)
                {
                    if(mat[i][j]=='#')break;
                }
                if(j<C)break;
            }
            if(i<R||j<C)cout<<"Impossible"<<endl;
            else
            {
                for(i=0;i<R;++i) {
                    for(j=0;j<C;++j)
                    {
                        cout<<mat[i][j];
                    }
                    cout<<endl;
                }
            }
        }
        else
        {
            for(i=0;i<R;++i) {
                for(j=0;j<C;++j)
                {
                    if(mat[i][j]=='#')break;
                }
                if(j<C)break;
            }
            if(i<R||j<C)cout<<"Impossible"<<endl;
            else
            {
                for(i=0;i<R;++i) {
                    for(j=0;j<C;++j)
                    {
                        cout<<mat[i][j];
                    }
                    cout<<endl;
                }
            }
        }

    }

    return 0;
}
