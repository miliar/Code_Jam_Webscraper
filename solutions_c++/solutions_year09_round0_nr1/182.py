/*
TASK: alien
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>

int l,n,d;
FILE *fout;
int used[20][30]={0};
char dic[5005][20];

int main()
{
    char temp[1000];
    freopen("A-large.in","r",stdin);
    fout = fopen("alien.out","w");
    
    scanf("%d %d %d",&l,&d,&n);
    for(int dd=0;dd<d;dd++)
    {
        scanf("%s",dic[dd]);
    }
    printf("A");
    for(int nn=0;nn<n;nn++)
    {
        scanf("%s",temp);
        int i,j,cnt=0;
        for(i=0;i<20;i++) for(j=0;j<30;j++) used[i][j] = 0;
        for(i=0;i<l;i++)
        {
            if(temp[cnt]=='(')
            {
                cnt++;
                while(temp[cnt]!=')')
                {
                    used[i][temp[cnt]-'a'] = 1;
                    cnt++;
                }
            }
            else used[i][temp[cnt]-'a'] = 1;
            cnt++;
        }
        cnt = 0;
        for(int dd=0;dd<d;dd++)
        {
            for(i=0;i<l;i++)
            {
                if(!used[i][dic[dd][i]-'a']) break;
            }
            if(i==l) cnt++;
        }
        fprintf(fout,"Case #%d: %d\n",nn+1,cnt);
    }
    return 0;
}
