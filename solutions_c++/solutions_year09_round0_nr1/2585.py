#include <stdio.h>
#include <string.h>

int n,d,l;
char token[5002][18];
int number[18][27];
char str[1000];

int main()
{
    int t;
    int i,j,k;
    scanf("%d%d%d",&l,&d,&n);
    for(i=1; i<=d; i++)
        scanf("%s",token[i]);              
    
    for(i=1; i<=n; i++)
    {
        scanf("%s",str);
        int len =strlen(str);
        int cnt = 0;
        int flag= 0;
        memset(number,0,sizeof(number));
        for(j=0; j< len; j++)
        {
            if(str[j] == '(')
            {
                flag = 1;
            }
            else if( str[j] != ')')
            {
                number[cnt][str[j]-'a'] = 1;
                if(!flag)
                    cnt++;
            }
            else
            {
                flag = 0;
                cnt++;
            } 
        }
        /*
        for(j = 0; j< l; j++)
        {
            for(k=0; k<26; k++)
                printf("%d ",number[j][k]);
            printf("\n");
        }
        */
        int re = 0;
        for(j=1; j<=d; j++)
        {
            for(k=0; k<l; k++)
                if( !number[k][token[j][k]-'a'])
                    break;
            if( k == l)
                re++;
        }
        printf("Case #%d: %d\n",i,re);
    }
    //while(1);    
    return 0;
}
