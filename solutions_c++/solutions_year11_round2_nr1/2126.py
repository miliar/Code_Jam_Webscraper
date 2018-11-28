#include <iostream>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

#define SORT(v) sort(v.begin(),v.end());
#define REVERSE(v) reverse(v.begin(),v.end());

char arr[100][100];
long double WP[100][3],OWP[100],OOWP[100];
int N;

long double getWP(int pl)
{
    long double res;
    long double tot = 0.0, win = 0.0;

    for(int i=0; i<N; i++)
    {
        if(arr[pl][i] != '.')
        {
            tot++;
            if(arr[pl][i] == '1')
                win++;
        }
    }

    WP[pl][1] = win;
    WP[pl][2] = tot;
    res = win / tot;
    return res;
}

long double getOWP(int pl)
{
    long double res = 0.0, val = 0.0;
    long double tot = 0.0;

    for(int i=0; i<N; i++)
    {
        if(pl != i && arr[pl][i] != '.')
        {
            if(arr[i][pl] == '1')
                val = 1.0;
            else
                val = 0.0;
            long double l1 = (WP[i][1] - val);
            long double l2 = (WP[i][2]-1);
            res = res + l1/l2;
            tot++;
        }
    }

    res = res/tot;
    return res;
}

long double getOOWP(int pl)
{
    long double res = 0.0;
    long double tot = 0.0;

    for(int i=0; i<N; i++)
    {
        if(pl != i && arr[pl][i] != '.')
        {
            res = res + OWP[i];
            tot++;
        }
    }

    res = res/tot;
    return res;
}

int main(void)
{
    int I,J,T;
    string str;

    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);

    cin>>T;

    for(I=1; I<=T; I=I+1)
    {
        cin>>N;
        for(J=0; J<N; J=J+1)
        {
            cin>>str;
            for(int k=0; k<str.size(); k=k+1)
                arr[J][k] = str[k];
        }

        for(J=0; J<N; J=J+1)
            WP[J][0] = getWP(J);

        for(J=0; J<N; J=J+1)
            OWP[J] = getOWP(J);

        for(J=0; J<N; J=J+1)
            OOWP[J] = getOOWP(J);


        long double res[100];
        for(J=0; J<N; J=J+1)
            res[J] = (0.25 * WP[J][0] + 0.50 * OWP[J] + 0.25 * OOWP[J]);

        cout<<"Case #"<<I<<":"<<endl;
        for(J=0; J<N; J=J+1)
            cout<<res[J]<<endl;
    }

    return 0;
}