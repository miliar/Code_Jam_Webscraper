#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
    e-0   j-u   p-r
    m-l   y-a   s-n
    l-g   c-e   k-i
    d-s   x-m   v-p
    n-b   r-t   i-d
    a-y   b-h   f-c
    g-v   h-x   o-k
    q-    t-w   u-j
    w-f   z-
 */
int Loop,Loo;
int num[30]={'y'-'a','h'-'a','e'-'a','s'-'a','o'-'a','c'-'a','v'-'a','x'-'a',
             'd'-'a','u'-'a','i'-'a','g'-'a','l'-'a','b'-'a','k'-'a','r'-'a',
             'z'-'a','t'-'a','n'-'a','w'-'a','j'-'a','p'-'a','f'-'a','m'-'a',
             'a'-'a','q'-'a'};

char str[102];
int main(void)
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,len;
    char c;
    scanf("%d%*c",&Loop);

    for(Loo=1;Loo<=Loop;++Loo)
        {
            printf("Case #%d: ",Loo);
            gets(str);
            len = strlen(str);
            for(i=0;i<len;++i)
                {
                    if((str[i]>='a'&&str[i]<='z'))
                        {
                            c = num[str[i]-'a']+'a';
                            printf("%c",c);
                        }
                    else
                        printf("%c",str[i]);
                }
            printf("\n");
        }
    return 0;
}
