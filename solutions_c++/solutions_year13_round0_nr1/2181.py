#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <functional>

using namespace std;

int main()
{
    int i,j,k,l;
    int T,t;

    freopen("A-large.in","r",stdin);
    freopen("output-A.txt","w",stdout);

    cin>>T;
    for(t=1;t<=T;++t)
    {
        char board[5][5];
        string ans;
        bool chck=true;
        int dotCount=0;

        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
            {
                cin>>board[i][j];
            }

        for(i=0;i<4&&chck;++i)
        {
            int countx[200]={0};
            for(j=0;j<4&&chck;++j)
            {
                countx[board[i][j]]++;
                dotCount+=board[i][j]=='.'?1:0;
            }
            if(countx['X']+countx['T']==4)
            {
                ans="X won";
                chck=false;
            }
            if(countx['O']+countx['T']==4)
            {
                ans="O won";
                chck=false;
            }
        }

        for(j=0;j<4&&chck;++j)
        {
            int countx[200]={0};
            for(i=0;i<4&&chck;++i)
            {
                countx[board[i][j]]++;
                //dotCount+=board[i][j]=='.'?1:0;
            }
            if(countx['X']+countx['T']==4)
            {
                ans="X won";
                chck=false;
            }
            if(countx['O']+countx['T']==4)
            {
                ans="O won";
                chck=false;
            }
        }

        if(chck)
        {
            int countx[200]={0};
            for(i=0,j=0;i<4;++i)
            {
                countx[board[i][j]]++;
                ++j;
                //dotCount+=board[i][j]=='.'?1:0;
            }
            if(countx['X']+countx['T']==4)
            {
                ans="X won";
                chck=false;
            }
            if(countx['O']+countx['T']==4)
            {
                ans="O won";
                chck=false;
            }
        }

        if(chck)
        {
            int countx[200]={0};
            for(i=0,j=3;i<4;++i)
            {
                countx[board[i][j]]++;
                --j;
                //dotCount+=board[i][j]=='.'?1:0;
            }
            if(countx['X']+countx['T']==4)
            {
                ans="X won";
                chck=false;
            }
            if(countx['O']+countx['T']==4)
            {
                ans="O won";
                chck=false;
            }
        }

        if(chck)
        {
            if(dotCount==0)
                ans="Draw";
            else
                ans="Game has not completed";
        }

        cout<<"Case #"<<t<<": "<<ans<<endl;


    }


    return 0;
}
