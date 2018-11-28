//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

char m[64][64];
int row, col;

bool translate()
{
    //while(true)
    {
        for (int i=0;i<row;++i)
        {
            for(int j=0;j<col;++j)
            {
                if(m[i][j]=='#')
                {
                    if (i==row-1 || j==col-1)
                        return false;
                    if (m[i+1][j+1]!='#'||m[i+1][j]!='#'||m[i][j+1]!='#')
                        return false;
                    m[i][j]='/';m[i][j+1]='\\';m[i+1][j]='\\';m[i+1][j+1]='/';
                }
            }
        }
    }
    return true;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T, t;
    scanf("%d", &T);
    for (t=1; t<=T;++t)
    {
        printf("Case #%d:\n", t);
        scanf("%d %d",&row, &col);
        for (int i=0;i<row;++i)
            scanf("%s",m[i]);
        if(translate())
        {
            for(int i=0;i<row;++i)
                printf("%s\n",m[i]);
        } else
            printf("Impossible\n");
    }
    //scanf("%d", &T);
	return 0;
}