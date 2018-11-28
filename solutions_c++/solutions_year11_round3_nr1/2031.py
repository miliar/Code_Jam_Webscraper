#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

#define SORT(v) sort(v.begin(),v.end());
#define REVERSE(v) reverse(v.begin(),v.end());

int R,C;
char RC[51][51];

int solve()
{
    int ret = 1, flag = 0, cnt = 0;

    for(int i=0; i<R; i++)
    {
        flag = 0;
        cnt = 0;
        for(int j=0; j<C; j++)
        {
            if(RC[i][j] == '#')
                cnt++;
            else if(cnt % 2 != 0)
                return 0;
            else
                cnt = 0;
        }
    }
    if(cnt % 2 != 0)
        return 0;
    return ret;
}

int main(void)
{
    string str;
    int I,J,T,imp;

    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);

    cin>>T;

    for(I=1; I<=T; I++)
    {
        cin>>R>>C;

        for(J=0; J<R; J++)
        {
            cin>>str;
            for(int p=0; p<str.size(); p++)
                RC[J][p] = str[p];
        }

        int ret = solve();

        if(ret == 0)
        {
            cout<<"Case #"<<I<<":"<<endl<<"Impossible"<<endl;
        }
        else
        {
            imp = 0;
            cout<<"Case #"<<I<<":"<<endl;

            for(J=0; J<R; J++)
            {
                for(int k=0; k<C; k++)
                {
                    if(RC[J][k] == '#')
                    {
                        RC[J][k] = '/';
                        RC[J][k+1] = '\\';
                        if(J+1 >= R || k+1 >= C)
                        {
                            cout<<"Impossible"<<endl;
                            imp = 1;
                            break;
                        }
                        else
                        {
                            RC[J+1][k] = '\\';
                            RC[J+1][k+1] = '/';
                        }
                        k++;
                    }
                }
                if(imp == 1)
                    break;
            }

            if(imp == 0)
                for(J=0; J<R; J++)
                {
                    for(int k=0; k<C; k++)
                    {
                        cout<<RC[J][k];
                    }
                    cout<<endl;
                }
        }
    }

    return 0;
}