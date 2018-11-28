#include<cstdio>
#include<map>
#include<set>

using namespace std;

unsigned long
hashf(unsigned char *str)
{
    unsigned long hash = 5381;
    int c;

    while (c = *str++)
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
}

int T,N,M,t,i,j,k;
char dict[11000][20];
char curword[11000][20];
unsigned long hash[11000];
int pts[11000];
char alph[101][27];
map < unsigned long, bool > haschar;

int main() {
    scanf("%d",&T);
    for(t=1;t<=T;t++) {
        printf("Case #%d:",t);

        scanf("%d %d",&N,&M);
        gets(dict[0]); /* junk */

        for(i=0;i<N;i++)
            gets(dict[i]);

        for(i=0;i<M;i++)
            gets(alph[i]);

        /* for each alphabet */
        for(i=0;i<M;i++) {
            /* initialize stuff */
            for(j=0;j<N;j++)
                pts[j]=0;
            for(j=0;j<N;j++) {
                char *p,*q;
                p=dict[j];
                q=curword[j];
                while(*p) {
                    *q='_';
                    q++;
                    p++;
                }
                *q=0;
            }
            for(j=0;j<N;j++)
                hash[j] = hashf((unsigned char*)curword[j]);
//            for(j=0;j<N;j++)
//                printf("%s %s %lu\n",dict[j],curword[j],hash[j]);

            /* each leter in alphabet */
            for(j=0;j<26;j++) {
                haschar.clear();
                for(k=0;k<N;k++) {
                    char *c = dict[k];
                    while(*c) {
                        if(*c == alph[i][j])
                            haschar[hash[k]]=true;
                        c++;
                    }
                }

                /* each word in dict */
                for(k=0;k<N;k++) {
                    if(haschar[hash[k]]) {
                        char *p,*q;
                        p=dict[k];
                        q=curword[k];
                        bool foundanything = false;
                        while(*p) {
                            if(*p == alph[i][j]) {
                                *q = alph[i][j];
                                foundanything = true;
                            }
                            p++;
                            q++;
                        }
                        if(foundanything) {
                            hash[k] = hashf((unsigned char*)curword[k]);
//                            char *c = dict[k];
//                            while(*c) {
//                                haschar[hash[k]].insert(*c);
//                                c++;
//                            }
                        }
                        else
                            pts[k]++;
                    }
                }
            }
//            for(j=0;j<N;j++)
//                printf("%s %d\n",dict[j],pts[j]);
            int maxpts=-1,maxptsword=-1;
            for(j=0;j<N;j++)
                if(pts[j] > maxpts) {
                    maxpts = pts[j];
                    maxptsword = j;
                }
            printf(" %s",dict[maxptsword]);
        }
//        printf("%d\n",haschar[1].count('v'));
//        printf("hi\n");
        printf("\n");
    }
    return 0;
}
