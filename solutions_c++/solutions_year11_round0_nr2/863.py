#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int CAS,c,d,n;
char comb[30][30],oppo[30][2];
char st[255],list[255];
int listp;
int used[30];
bool isOppo()
{
    int xt,yt;
    for(int i = 0;i < d;i++)
    {
        xt = oppo[i][0];
        yt = oppo[i][1];
        if(used[xt]!=0 && used[yt]!=0)
            return true;
    }
    return false;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int xt,yt,zt;
    scanf("%d",&CAS);
    for(int cas = 1;cas <= CAS;cas++)
    {
        scanf("%d",&c);
        memset(comb,0xff,sizeof(comb));
        memset(oppo,0xff,sizeof(oppo));
        for(int i = 0;i < c;i++)
        {
            scanf("%s",st);
            xt = st[0]-'A';
            yt = st[1]-'A';
            zt = st[2]-'A';
            comb[xt][yt] = comb[yt][xt] = zt;
        }
        //printf("%d\n",comb['R'-'A']['R'-'A']);
        scanf("%d",&d);
        for(int i = 0;i < d;i++)
        {
            scanf("%s",st);
            xt = st[0]-'A';
            yt = st[1]-'A';
            oppo[i][0] = xt;
            oppo[i][1] = yt;
        }
        scanf("%d",&n);
        scanf("%s",st);
        memset(used,0,sizeof(used));
        listp = 0;
        for(int i = 0;i < n;i++)
        {
            list[listp++] = st[i];
            used[st[i]-'A']++;
            if(listp>1)
            {
                xt = list[listp-1] - 'A';
                yt = list[listp-2] - 'A';
                if(comb[xt][yt] != -1)
                {
                    listp--;
                    list[listp-1] = comb[xt][yt]+'A';
                    used[xt]--;used[yt]--;used[list[listp-1]]++;
                }
            }
            if(isOppo() == true)
            {
                listp = 0;
                memset(used,0,sizeof(used));
            }
            //printf("listp:%d list:",listp);
            //for(int j = 0;j < listp;j++)
            //    printf("%c ",list[j]);
            //printf("\n");
        }
        printf("Case #%d: [",cas);
        for(int i = 0;i < listp-1;i++)
            printf("%c, ",list[i]);
        if(listp!=0)
            printf("%c",list[listp-1]);
        printf("]\n");
    }
    fclose(stdin);
    fclose(stdout);
    //system("pause");
}
