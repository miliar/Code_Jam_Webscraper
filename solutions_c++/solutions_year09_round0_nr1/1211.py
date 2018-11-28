/*
TASK: code_jam_a
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char word[5010][20];
char str[10010];
int pos[100][300];

int main()
{
    int l,d,n,i,cc,ans=0,len,top,state,j;
    
    scanf("%d%d%d", &l,&d,&n);
    
    for(i=0;i<d;i++)
    {
        scanf("%s", word[i]);
//        printf("%s\n", word[i]);
    }
    
    for(cc=0;cc<n;cc++)
    {
        scanf("%s",str);
        
        len = strlen(str);
        top=0;
        state=0;
        
        for(i=0;i<100;i++)
            for(j=0;j<300;j++)
                pos[i][j]=0;
        
        for(i=0;i<len;i++)
        {
            if(str[i]=='(')
            {
                state=1;
            }
            else if(str[i]==')')
            {
                state=0;
                top++;
            }
            else
            {
                if(state==1)
                {
                    pos[top][ str[i] ]=1;
//                    printf("pos %d %c = 1\n", top, str[i]);
                }
                else
                {
                    pos[top][ str[i] ]=1;
                    top++;
                }
            }
            
        }
        
        ans=0;
        
        for(i=0;i<d;i++)
        {
            for(j=0;j<l;j++)
            {
//                printf("word %d %d = %c\n", i,j, word[i][j]);
//                printf("pos %d %d\n", j, word[i][j]);
                if(pos[j][ word[i][j] ]==0)
                    break;
            }
                    
            if(j==l)
                ans++;
        }
        
        printf("Case #%d: %d\n", cc+1,ans);
    }
    
    return 0;
}
