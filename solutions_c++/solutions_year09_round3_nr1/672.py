#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
    int t, caso=0;
    char str[100];
    char aux[100];
    int chars[150];
    int nchars;
    int i,j,k;

    scanf("%d",&t);

    while (t--) {

        scanf("%s",str);

        nchars=0;
        for(i=0;i<150;i++) chars[i]=0;
        for(i=0;i<100;i++) aux[i]=0;

        for(i=0;i<strlen(str);i++) {
            if (!chars[(int)(str[i]-'0')]++)
                nchars++;
        }

        for(int j=1; j<=nchars; ) {
            char c=0;
            for(k=0; str[k]; k++) {
                if (aux[k]==0 && c==0) c=str[k];
                if ((str[k]==c) && aux[k]==0) {
                    if (j<10) {
                    str[k] = j+'0';
                    }
                    else {
                        str[k]= (j-10)+'A';
                    }
                    aux[k] = 1;
                }
            }
            if (j==1) j=0;
            else if (j==0) j=2;
            else j++;
        }

        char * p;
        long long n = strtol(str, &p, (nchars!=1)?nchars:2);

        printf("Case #%d: %d\n",++caso,n);
    }

    return 0;
}
