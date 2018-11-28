#include <cstdio>
#include <cstring>

char w[200][20];
char ord[20][30];

bool cand[200];
char know[20];

bool match(char *s, char *t, char gu) {
    for (int i=0; s[i]; i++)
        if ((s[i] == gu || t[i]==gu) && (s[i]!=t[i])) return false;
    return true;
}

int main() {
    int nt;

    scanf(" %d",&nt);
    for (int ct=1; ct<=nt; ct++) {
        int n,m;
        int res, wres, poss;
        scanf("%d%d",&n,&m);
        for(int i=0; i<n; i++)
            scanf(" %s",w[i]);
        for(int i=0; i<m; i++)
            scanf(" %s",ord[i]);

        printf("Case #%d:", ct);
        for (int k=0; k<m; k++) {
            res=-1;
            for (int ch=0; ch<n; ch++) {
                int l = strlen(w[ch]);
                int pts=0;

                for (int i=0; i<n; i++)
                    if (strlen(w[i])==l) cand[i]=true;
                    else cand[i]=false;

                memset(know, 0, sizeof(know));
                for (int i=0; i<26; i++) {
                    char gu = ord[k][i];
                    bool ex=false;
                    for (int j=0; j<n; j++)
                        if (cand[j] && strchr(w[j], gu)) {
                            ex = true;
                            break;
                        }


                    if (ex) {
                        // if (ch==2) printf("\nguess %c",gu);
                        if (!strchr(w[ch], gu)) {
                            pts++;
                            for (int j=0; j<n; j++)
                                cand[j]=cand[j] && !strchr(w[j], gu);
                            continue;
                        }

                        for (int j=0; j<l; j++)
                            if (w[ch][j]==gu) know[j]=gu;

                        poss=0;

                        for (int j=0; j<n; j++) {
                            if (cand[j] && !match(w[j], know, gu)) cand[j]=false;
                            if (cand[j]) poss++;
                        }
                    }
                }

                // printf("\n = %d\n",pts);

                if (pts > res) {
                    res = pts;
                    wres = ch;
                }
            }
            printf(" %s", w[wres]);
            // printf(" %s(%d)", w[wres],res);
        }

        printf("\n");
    }
    return 0;
}
