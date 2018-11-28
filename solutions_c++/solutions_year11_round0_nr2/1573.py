#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int main()
{
    freopen("C:\\Users\\¼Ó·ÆÃ¨\\Downloads\\B-large.in", "r", stdin);
    freopen("D:OUTPUT.txt", "w", stdout);
    int dic1[250][250],dic2[250][250];
    int find=0;
    int i, j,k;
    int test,pp;
    scanf("%d",&test);
    for (pp=1; pp<=test; pp++)
    {
        int C,D,N;
        int i;
        char s[201];
        memset(dic1,0,sizeof(dic1));
        memset(dic2,0,sizeof(dic2));
        scanf("%d",&C);
        for (i=1; i<=C; i++)
        {
            scanf("%s",s);
            dic1[s[0]][s[1]]=s[2];
            dic1[s[1]][s[0]]=s[2];
        }
        scanf("%d",&D);
        for (i=1; i<=D; i++)
        {
            scanf("%s",s);
            dic2[s[1]][s[0]]=1;
            dic2[s[0]][s[1]]=1;
        }
        scanf("%d",&N);
        scanf("%s",s);
        for (i=1; i<N; i++)
        {
            if (dic1[s[i]][s[i-1]]!=0)
            {
                s[i]=dic1[s[i]][s[i-1]];
                s[i-1]=0;
            }
            else
            {
                for (j=i-1; j>=0; j--)
                    if (dic2[s[i]][s[j]]!=0)
                    {
                        for (k=0; k<=i; k++)
                            s[k]=0;
                        i++;
                        break;
                    }
            }
        }
        printf("Case #%d: [",pp);
        j=0;
        k=0;
        for (i=0;i<N;i++)
        if (s[i]!=0) j++;
        for (i=0; i<N; i++)
            if (s[i]!=0)
            {
                if (k==0) k++;
                else printf(" ");
                printf("%c",s[i]);
                j--;
                if (j!=0) printf(",");
            }
        printf("]\n");
    }
}
