#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>
#include <cstring>
#include <vector>
using namespace std;
typedef long long LL;
#define S 1005
int n,t,txt;
char ch[8][8];
bool x,o;
int xrow[6],orow[6],xcol[6],ocol[6];

int main()
{
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k;
    scanf("%d",&t);
    while(t--)
    {
        gets(ch[0]);
        x = o = false;
        printf("Case #%d: ",++txt);
        for(int i = 0; i < 4; ++i)gets(ch[i]);
        memset(xrow, 0, sizeof xrow);
        memset(orow, 0, sizeof orow);
        memset(xcol, 0, sizeof xcol);
        memset(ocol, 0, sizeof ocol);
        bool over = true;
        for(int i = 0; i < 4; ++i)for(int j = 0; j < 4; ++j)
        {
            if(ch[i][j] == 'X' || ch[i][j] == 'T')xrow[i]++,xcol[j]++;
            else if(ch[i][j] == 'O' || ch[i][j] == 'T')orow[i]++,ocol[j]++;
            else over = false;
        }
        bool x = false, o = false;
        int x1 = 0, o1 = 0, x2 = 0, o2 = 0;
        for(int i = 0; i < 4; ++i)
        {
            if(ch[i][i] == 'X' || ch[i][i] == 'T')x1++;
            if(ch[i][i] == 'O' || ch[i][i] == 'T')o1++;
            if(ch[i][3-i] == 'X' || ch[i][3-i] == 'T')x2++;
            if(ch[i][3-i] == 'O' || ch[i][3-i] == 'T')o2++;
        }
        if(x1 == 4 || x2 == 4)x = true;
        if(o1 == 4 || o2 == 4)o = true;


        for(int i = 0; i < 4; ++i)
        {
            if(xrow[i] == 4 || xcol[i] == 4)x = true;
            if(orow[i] == 4 || ocol[i] == 4)o = true;
        }
        if(x && o)cout <<"Draw" << endl;
        else if(x)cout <<"X won" << endl;
        else if(o)cout <<"O won" << endl;
        else if(!over)cout <<"Game has not completed" << endl;
        else cout <<"Draw" << endl;

    }
    return 0;
}
