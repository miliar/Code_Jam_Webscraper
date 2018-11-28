#include <stdio.h>
#include <string.h>

int main()
{
    int t , len , i , j ;
    FILE *fin , *fout ;
    char str[101];
    char replace[27] = "yhesocvxduiglbkrztnwjpfmaq";
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A2.txt","w",stdout);
    scanf("%d\n",&t);
    
    for ( i = 1 ; i <= t ; i++ ) {
          gets(str);
          len = strlen(str);
          for ( j = 0 ; j < len ; j++ )
              if ( str[j] != ' ' )
                 str[j] = replace[str[j]-'a'] ;
          printf("Case #%d: %s\n",i,str);
    }

    return 0 ;
}
