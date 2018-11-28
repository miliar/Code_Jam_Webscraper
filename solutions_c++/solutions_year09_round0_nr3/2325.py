#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

char *Wel="welcome to code jam";        // 19
char Buf[10240];
int Count=0;

void Match(char *ps, char *pw) 
{
    if(*pw=='\0') {
        ++Count;
        return;
    }
    
    char *pc=ps;
    while(*pc) {
        pc=strchr(pc, *pw);
        if(NULL==pc)
            return;                        
        
        Match(pc+1, pw+1);
        ++pc;
    }
}    

int main(int arg, char *argv)
{
    int t;

    fgets(Buf, sizeof(Buf), stdin);
    t=atoi(Buf);
    int lc=1;
    for(int i=1; i<=t; ++i) {
        fgets(Buf, sizeof(Buf), stdin);
        ++lc;
        //int len=strlen(Buf);
        Count=0;
        Match(Buf, Wel);                    

        printf("Case #%d: %04d\n", i, Count);        
    }
    return 0;    
}

