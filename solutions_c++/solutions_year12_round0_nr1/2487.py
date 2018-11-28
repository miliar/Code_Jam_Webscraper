#include <stdio.h>


const char *A="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
const char *B="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char str[1000];
char tb[128];

int main(){
    int n,i,j;
    for( i=0; A[i]; i++ ) {
        tb[A[i]] = B[i];
    }
    tb['q']='z';
    tb['z']='q';
    scanf("%d",&n);
    gets(str);
    for( i=0; i<n; i++ ) {
        gets(str);
        for( j=0; str[j]; j++ ){
            str[j] = tb[str[j]];
        }
        printf("Case #%d: %s\n",i+1,str);
    }
}
