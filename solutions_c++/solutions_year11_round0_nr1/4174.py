#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int bptr = 0, optr = 0;
int vp;
char valid;
vector< pair<char,int> > vct, ovct, bvct;
int temp;
int updateNxt(char ch, int cnt)
{
    int I;
    valid = vct[cnt].first;
    vp = vct[cnt].second;
    if(ch == 'O')
    {
        for(I = optr; I < ovct.size(); I = I + 1)
            if(ovct[I].first == ch)
                return ovct[I].second;
    }
    else
    {
        for(I = bptr; I < bvct.size(); I = I + 1)
            if(bvct[I].first == ch)
                return bvct[I].second;
    }
}

int main(void)
{
    int cnt,bp,bnxt,op,onxt,push;
    char ch;
    int I,J,T,N,num;

    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);

    cin>>T;
    for(I = 1; I <= T; I = I + 1)
    {
        vct.clear();
        ovct.clear();
        bvct.clear();
        bp = 1; op = 1; push = 0;    cnt = 0;   optr = 0;   bptr = 0;

        cin>>N;
        for(J = 1; J <= N; J = J + 1)
        {
            cin>>ch>>num;
            vct.push_back(make_pair(ch,num));
            if(ch=='O')
                ovct.push_back(make_pair(ch,num));
            else
                bvct.push_back(make_pair(ch,num));
        }

        onxt = updateNxt('O', 0);
        bnxt = updateNxt('B', 0);
        for(J = 0; cnt != vct.size(); J = J + 1)
        {
            if(onxt == op)
            {
                if(push == 0 && valid == 'O' && vp == op)
                {
                    cnt = cnt + 1;
                    push = 1;
                    optr = optr + 1;
                    onxt = updateNxt('O', cnt);
                }
            }
            else if(onxt > op)
                op = op + 1;
            else
                op = op - 1;

            if(bnxt == bp)
            {
                if(push == 0 && valid == 'B' && vp == bp)
                {
                    cnt = cnt + 1;
                    bptr = bptr + 1;
                    bnxt = updateNxt('B', cnt);
                }
            }
            else if(bnxt > bp)
                bp = bp + 1;
            else
                bp = bp - 1;
            push = 0;
        }

        cout<<"Case #"<<I<<": "<<J<<endl;
    }

    return 0;
}