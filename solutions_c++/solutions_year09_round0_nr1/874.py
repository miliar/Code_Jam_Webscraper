#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector <char> v[505][20];
char s[5010][20];
bool f[5010][20];

int main()
{
    int i,ii,j,k,l,d,n,res;
    char tmp;
    scanf("%d%d%d",&l,&d,&n);
    getchar();
    for (i=0;i<d;i++) gets(s[i]);
    for (i=0;i<n;i++)
    {
        for (j=0;j<l;j++)
        {
            tmp=getchar();
            if (tmp!='(') v[i][j].push_back(tmp);
            else
            {
                tmp=getchar();
                while (tmp!=')')
                {
                    v[i][j].push_back(tmp);
                    tmp=getchar();
                }
            }
        }
        getchar();
    }
    for (i=0;i<n;i++)
    {
        res=0;
        memset(f,0,sizeof(f));
        for (j=0;j<l;j++)
        {
            for (k=0;k<d;k++)
            {
                for (ii=0;ii<v[i][j].size();ii++)
                {
                    if (s[k][j]==v[i][j][ii]&&(j==0||f[k][j-1]))
                    {
                        f[k][j]=true;
                    }
                }
            }
        }
        for (j=0;j<d;j++)
        {
            if (f[j][l-1]) res++;
        }
        printf("Case #%d: %d\n",i+1,res);
    }
    return 0;
}
