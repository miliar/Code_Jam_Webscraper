#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
char s[10][10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        for (int i=0;i<4;i++)
            scanf("%s",s[i]);
        bool winx=false,wino=false,blank=false;
        for (int i=0;i<4;i++)
        {
            int cntt1=0,cntt2=0,cntt3=0,cntt4=0;
            for (int j=0;j<4;j++)
            {
                if (s[i][j]=='.') blank=true;
                if (s[i][j]=='X'||s[i][j]=='T')
                    cntt1++;
                if (s[i][j]=='O'||s[i][j]=='T')
                    cntt2++;
                if (s[j][i]=='X'||s[j][i]=='T')
                    cntt3++;
                if (s[j][i]=='O'||s[j][i]=='T')
                    cntt4++;
            }
            if (cntt1==4||cntt3==4) winx=true;
            if (cntt2==4||cntt4==4) wino=true;
        }
        int cntt1=0,cntt2=0,cntt3=0,cntt4=0;
        for (int i=0;i<4;i++)
        {
            if (s[i][i]=='X'||s[i][i]=='T') cntt1++;
            if (s[i][i]=='O'||s[i][i]=='T') cntt2++;
            if (s[i][3-i]=='X'||s[i][3-i]=='T') cntt3++;
            if (s[i][3-i]=='O'||s[i][3-i]=='T') cntt4++;
        }
        if (cntt1==4||cntt3==4) winx=true;
        if (cntt2==4||cntt4==4) wino=true;
        printf("Case #%d: ",ii);
        if (winx) puts("X won");
        else if (wino) puts("O won");
        else if (blank) puts("Game has not completed");
        else puts("Draw");
    }
    return 0;
}

