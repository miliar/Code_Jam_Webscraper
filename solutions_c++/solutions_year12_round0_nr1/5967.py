#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
    char che[200];

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    char test[27] ={"yhesocvxduiglbkrztnwjpfmaq"} ;
    int times ,n;
    gets(che);
    times = atoi(che);
    int cases =0;
    while(times--)
    {
        gets(che);
        printf("Case #%d: ",++cases);
        for(int i = 0 ; i < strlen(che) ; i++)
        {
            if(che[i]>= 'a' && che[i] <='z')
            {
                putchar(test[che[i]-'a'] );
            }
            else putchar(che[i]);
        }
        puts("");
    }


    return 0 ;
}
