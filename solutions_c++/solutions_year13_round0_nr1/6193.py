#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("salida2.out","w",stdout);
    int t,con,x,o,w;
    char re[4][4];
    cin>>t;
    for(int a=0;a<t;a++)
    {
        con=0;w=-1;x=0;o=0;
        for(int b=0;b<4;b++){cin>>re[b][0]>>re[b][1]>>re[b][2]>>re[b][3];}
        for(int b1=0;b1<4;b1++)
        {
            for(int b2=0;b2<4;b2++)
            {
                if(re[b1][b2]!='.')
                {
                    if(re[b1][b2]=='X'){x++;con++;}
                    if(re[b1][b2]=='O'){o++;con++;}
                    if(re[b1][b2]=='T'){x++;o++;con++;}
                }
            }
            if(x==4){w=0;break;}
            if(o==4){w=1;break;}
            x=0;o=0;
        }
        if(w==-1)
        {
            x=0;o=0;
            for(int c1=0;c1<4;c1++)
            {
                for(int c2=0;c2<4;c2++)
                {
                    if(re[c2][c1]!='.')
                    {
                        if(re[c2][c1]=='X'){x++;}
                        if(re[c2][c1]=='O'){o++;}
                        if(re[c2][c1]=='T'){x++;o++;}
                    }
                }
                if(x==4){w=0;break;}
                if(o==4){w=1;break;}
                x=0;o=0;
            }
        }
        if(w==-1)
        {
            x=0;o=0;
            for(int d1=0;d1<4;d1++)
            {
                if(re[d1][d1]!='.')
                {
                    if(re[d1][d1]=='X'){x++;}
                    if(re[d1][d1]=='O'){o++;}
                    if(re[d1][d1]=='T'){x++;o++;}
                }
            }
            if(x==4)w=0;if(o==4)w=1;
        }
        if(w==-1)
        {
            x=0;o=0;
            for(int d1=0;d1<4;d1++)
            {
                if(re[d1][3-d1]!='.')
                {
                    if(re[d1][3-d1]=='X'){x++;}
                    if(re[d1][3-d1]=='O'){o++;}
                    if(re[d1][3-d1]=='T'){x++;o++;}
                }
            }
            if(x==4)w=0;if(o==4)w=1;
        }
        //bien hasta aki
        if(w==0)printf("Case #%d: X won\n",a+1);
        else if(w==1)printf("Case #%d: O won\n",a+1);
        else if(con==16)printf("Case #%d: Draw\n",a+1);
        else printf("Case #%d: Game has not completed\n",a+1);
    }
}
