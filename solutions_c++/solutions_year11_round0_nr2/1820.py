#include <iostream>
#include <fstream>
#include <algorithm>
#include <climits>
#include <cstring>
#include <climits>
#include <cmath>




using namespace std;

char combine[500][500];
bool oppose[500][500];
char res[500];
char str[500];
int C,D,N;





int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);

    int T;
    scanf("%d",&T);

    for(int loop=1;loop<=T;loop++)
    {
        memset(combine,-1,sizeof(combine));
        memset(oppose,false,sizeof(oppose));
        scanf("%d",&C);
        for(int i=0;i<C;i++)
        {
            scanf("%s",str);
            combine[str[0]][str[1]]=str[2];
            combine[str[1]][str[0]]=str[2];

        }
        //puts("jackie");
        scanf("%d",&D);
        for(int i=0;i<D;i++)
        {
            scanf("%s",str);
            oppose[str[0]][str[1]]=oppose[str[1]][str[0]]=true;
        }
        scanf("%d",&N);
        scanf("%s",str);
        //puts("jackielll");
        int len=0;
        for(int i=0;i<N;i++)
        {
            if(len==0)
            {
                res[len++]=str[i];
            }
            else if(combine[str[i]][res[len-1]]!=-1)
            {
                res[len-1]=combine[str[i]][res[len-1]];
            }
            else
            {
                bool bingo=true;
                for(int j=0;j<len;j++)
                {
                    if(oppose[str[i]][res[j]])
                    {
                        bingo=false;
                        break;
                    }
                }
                if(!bingo)
                {
                    len=0;
                }
                else
                {
                    res[len++]=str[i];
                }
            }
        }

        printf("Case #%d: [",loop);
        for(int i=0;i<len;i++)
        {
            if(i)
            printf(", %c",res[i]);
            else
            printf("%c",res[i]);
        }
        puts("]");
    }
















    return 0;
}
