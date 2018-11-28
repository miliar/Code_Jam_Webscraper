#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include<string>

using namespace std;

char arr[26];
char inp[101];
int main(void){
    int T;


    string str = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";

    string ans = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    for(int i = 0; i<str.size(); i++)
    {
        if(str[i] >= 'a' && str[i] <= 'z')
        {
            arr[str[i] - 'a'] = ans[i];
        }
    }

    for(int i = 0; i<26; i++)
    {
        if(arr[i] >= 'a' && arr[i] <= 'z')
        {
        }
        else
        {
            arr[i] = '?';
            if(i + 'a' == 'z')
            {
                arr[i] = 'q';
            }
            else if(i + 'a' == 'q')
            {
                arr[i] = 'z';
            }
        }
        //printf("%c = %c\n",i + 'a', arr[i]);
    }

    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);

    scanf("%d",&T);
    getchar();
    for(int t = 0; t<T; t++)
    {
        gets(inp);
        printf("Case #%d: ", t + 1);
        for(int i = 0; i<strlen(inp); i++)
        {
            if(inp[i] >= 'a' && inp[i] <= 'z')
            {
                printf("%c", arr[inp[i] - 'a']);
            }
            else
            {
                printf("%c",inp[i]);
            }
        }

        puts("");
    }
    return 0;
}
