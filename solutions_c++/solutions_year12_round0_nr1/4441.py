#include<cstring>
#include<cstdio>
#include<iostream>

using namespace std;

#define FOR(i,a,b) for(int i = (a);i<(b);i++)
#define max_n 105

char t[max_n];
char res[max_n];
char ch[max_n];

void rob(){
ch[0] = 'y';
ch[1] = 'h';
ch[2] = 'e';
ch[3] = 's';
ch[4] = 'o';
ch[5] = 'c';
ch[6] = 'v';
ch[7] = 'x';
ch[8] = 'd';
ch[9] = 'u';
ch[10] = 'i';
ch[11] = 'g';
ch[12] = 'l';
ch[13] = 'b';
ch[14] = 'k';
ch[15] = 'r';
ch[16] = 'z';
ch[17] = 't';
ch[18] = 'n';
ch[19] = 'w';
ch[20] = 'j';
ch[21] = 'p';
ch[22] = 'f';
ch[23] = 'm';
ch[24] = 'a';
ch[25] = 'q';




}




int main(){
    rob();
    int tC; scanf("%d\n",&tC);
    FOR(nrT,1,tC+1){
        int poz = 0;
        char C = getchar();
        while(C!='\n'){
          t[poz++]=C;
          C = getchar();
        }
        printf("Case #%d: ",nrT);
        FOR(i,0,poz){
            if(t[i]!=' ')
              printf("%c",ch[t[i]-'a']);
            else printf(" ");
        }
        printf("\n");
    }
    return 0;
}
