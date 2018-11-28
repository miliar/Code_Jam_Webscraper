#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

string str[55];
char ans[55][55];
bool f[55][55];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,n,m,i,j,num,k=1;
    bool flag;
    scanf("%d",&c);
    while(c--)
    {
        num=0;
        scanf("%d%d",&n,&m);
        for( i=0; i<n; ++i)
        {
            cin >> str[i];
            for( j=0; j<m; ++j)
            {
                if(str[i][j]=='#') num++;
            }
        }
        printf("Case #%d:\n",k++);
        if(num%4!=0)
        {
            printf("Impossible\n");
        }
        else
        {
            flag=1;
            memset(f,0,sizeof(f));
            memset(ans,'0',sizeof(ans));
            for( i=0; i<n; ++i)
            {
                for( j=0; j<m; ++j)
                {
                    if(!f[i][j])
                    {
                        f[i][j]=1;
                        if(str[i][j]=='#')
                        {
                            if(str[i][j+1]=='#' && str[i+1][j]=='#' && str[i+1][j+1]=='#')
                            {
                                f[i][j+1]=f[i+1][j]=f[i+1][j+1]=1;
                                ans[i][j]='/';
                                ans[i][j+1]='\\';
                                ans[i+1][j]='\\';
                                ans[i+1][j+1]='/';
                            }
                            else
                            {
                                ans[i][j]='#';
                                flag=0;
                            }
                        }
                        else
                        {
                            ans[i][j]=str[i][j];
                        }
                    }
                }
            }
            if(flag==0) 
            {
                printf("Impossible\n");
                continue;
            }    
            for( i=0; i<n; ++i)
            {
                for( j=0; j<m; ++j)
                {
                    printf("%c",ans[i][j]);
                }
                printf("\n");
            }
        }
    }
    return 0;
}












