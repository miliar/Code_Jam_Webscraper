#include<stdio.h>
#include<string.h>

char str[ 105 ];

//char temp[] ={ "abcdefghijklmnopqrstuvwxyz" };
char temp[] ={ "yhesocvxduiglbkrztnwjpfmaq" };

int main()
{

    freopen("A-small-attempt0.in","r" ,stdin);
    freopen("tex.out","w" ,stdout);
    int cases;
    scanf("%d" , &cases );
    getchar();
    for( int t = 1 ; t <= cases ; t ++ )
    {
        gets(str);
        printf("Case #%d: " ,t );
        for( int i = 0 ;i < strlen(str) ;i++ )
        if( str[i] >= 'a' && str[i] <= 'z')
        printf("%c" , temp[ str[i] - 'a' ] );
        else printf("%c",str[i]);
        printf("\n");
    }
    return 0;
}

