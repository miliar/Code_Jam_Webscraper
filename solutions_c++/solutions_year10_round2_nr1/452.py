#include <stdio.h>
#include <string.h>
#include <map>
#include <iostream>
using namespace std;

char buf[200];
char part[200];
string strbuf,strpart;
map <string,int> dict;
int main()
{
    int t,tt,m,n;
    int len,i,j,k,kk,pp,count;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for (tt = 1; tt <= t; tt ++)
    {
        scanf("%d%d",&m,&n);
        getchar();
        dict.clear();
        count = 0;
        for (i = 0; i < m; i ++)
        {
            scanf("%s",buf);
            len = strlen(buf);
            pp = 0;
            strbuf = "";
            for (j = 0; j < len; j = k)
            {
                k = j + 1;
                while (k < len && buf[k] != '/')
                    k ++;
                for (kk = j; kk < k; kk ++)
                    part[kk - j] = buf[kk];
                part[k - j] = '\0';
                strpart = part;
                strbuf += "/" + strpart;
                dict[strbuf] = 1;
                //cout << strbuf <<endl;
            }
        }
        for (i = 0; i < n; i ++)
        {
            scanf("%s",buf);
            len = strlen(buf);
            pp = 0;
            strbuf = "";
            for (j = 0; j < len; j = k)
            {
                k = j + 1;
                while (k < len && buf[k] != '/')
                    k ++;
                for (kk = j; kk < k; kk ++)
                    part[kk - j] = buf[kk];
                part[k - j] = '\0';
                strpart = part;
                strbuf += "/" + strpart;
                //cout << strbuf <<endl;
                if (dict[strbuf] == 0)
                {
                    count ++;
                    dict[strbuf] = 1;
                }
            }
        }
        printf("Case #%d: %d\n",tt,count);
    }
    return 0;
}
