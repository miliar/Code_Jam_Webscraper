#include<stdio.h>
#include<string.h>

char dict[5002][502], in[502];
bool flag[16][28];

int main()
{
    freopen("Alarge.in","r",stdin);
    freopen("Alarge.out","w",stdout);
    
    int wlen, dictlen, inputlen;
    
    scanf("%d%d%d",&wlen,&dictlen,&inputlen);
    
    for(int i = 0; i < dictlen; ++i)
    {
        scanf("%s",dict[i]);   
    }
    
    for(int t = 1; t <= inputlen; ++t)
    {
        memset(flag,0,sizeof(flag));
        scanf("%s",in);
        int len = strlen(in);
        int i = 0, j = 0;
        while(i < len)
        {
            if(in[i]=='(')
            {
                ++i;
                while(in[i]!=')')
                {
                   flag[j][in[i]-'a'] = true;
                   ++i;    
                }
                ++i;   
            }
            else
            {
                flag[j][in[i]-'a'] = true;
                ++i;   
            }
            ++j;
        }
        int ans = 0;
        for(int i = 0; i < dictlen; ++i)
        {
            int dlen = strlen(dict[i]);
            bool matches = true;
            for(int j = 0; matches && j < dlen; ++j)
            {
                if(!flag[j][dict[i][j]-'a'])
                matches = false;
            }   
            
            if(matches)
            ++ans;
        }
        
        printf("Case #%d: %d\n",t,ans);
    }
    
    return 0;    
}
