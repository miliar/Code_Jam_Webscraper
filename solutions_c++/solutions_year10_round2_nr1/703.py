#include <stdio.h>
#include <string.h>

char kamus[5000][105];
int indeks[5000];
char kodePar[5000][105];

int main () {
    
    int t,n,m,hasil,nKamus,len,x,coa,ctr;
    bool cek;
    char input[105];
    char temp[100];
    char seb[105];
    
    scanf("%d",&t);
    for(int c=1;c<=t;c++) {
        hasil = 0;
        nKamus = 0;
        scanf("%d %d\n",&n,&m);
        for(int i=0;i<n;i++) {
            scanf("%s",input);
            len = strlen(input);
            coa = 0;
            for(int k=0;k<100;k++) {
                seb[k] = '\0';
            }
            seb[0] = '/';
            ctr = 1;
            for(int j=1;j<len;j++) {
                x = 0;
                for(int k=0;k<100;k++) {
                    temp[k] = '\0';
                }
                while(input[j]!='/' && j<len) {
                    temp[x] = input[j];
                    j++;
                    x++;
                }
                cek = true;
                for(int k=0;k<nKamus;k++) {
                    if(strcmp(temp,kamus[k]) == 0 && coa == indeks[k] && strcmp(seb,kodePar[k])==0) {
                        cek = false;
                        break;
                    }
                }
                if(cek) {
                    strcpy(kamus[nKamus],temp);
                    indeks[nKamus] = coa;
                    strcpy(kodePar[nKamus],seb);
                    nKamus++;
                }
                coa++;
                for(int xx = 0; xx <strlen(temp);xx++) {
                    seb[ctr+xx] = temp[xx];
                }
                seb[ctr+strlen(temp)] = '/';
                ctr = ctr+strlen(temp)+1;
            }
        }
        
        for(int i=0;i<m;i++) {
            scanf("%s",input);
            len = strlen(input);
            coa = 0;
            for(int k=0;k<100;k++) {
                seb[k] = '\0';
            }
            seb[0] = '/';
            ctr = 1;
            for(int j=1;j<len;j++) {
                x = 0;
                for(int k=0;k<100;k++) {
                    temp[k] = '\0';
                }
                while(input[j]!='/' && j < len) {
                    temp[x] = input[j];
                    j++;
                    x++;
                }
                cek = true;
                for(int k=0;k<nKamus;k++) {
                    if(strcmp(temp,kamus[k]) == 0 && coa == indeks[k] && strcmp(seb,kodePar[k])==0 ) {
                        cek = false;
                        break;
                    }
                }
                if(cek) {
                    hasil++;
                    strcpy(kamus[nKamus],temp);
                    indeks[nKamus] = coa;
                    strcpy(kodePar[nKamus],seb);
                    nKamus++;
                }
                coa++;
                for(int xx = 0; xx <strlen(temp);xx++) {
                    seb[ctr+xx] = temp[xx];
                }
                seb[ctr+strlen(temp)] = '/';
                ctr = ctr+strlen(temp)+1;
            }
        }
        
        printf("Case #%d: %d\n",c,hasil);
    }
    
    while (getchar()!=EOF);
    return 0;
}
