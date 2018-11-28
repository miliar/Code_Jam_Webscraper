#include <cstdio>
#include <cstring>

char m[200][200];
double w1[200], w2[200], w3[200];

double wp(int n, int i, int ig) {
    int q=0, sum=0;
    for (int j=0; j<n; j++)
        if (m[i][j]!='.' && j!=ig) {
            q++;
            sum+=m[i][j]-'0';
        }
    return (double) sum/q;
}

int main() {
    int nt;

    scanf("%d",&nt);
    for (int ct=1; ct<=nt; ct++) {
        int n;
        scanf(" %d",&n);
        printf("Case #%d:\n",ct);
        for (int i=0; i<n; i++)
            scanf(" %s",m[i]);

        for (int i=0; i<n; i++) {
            w1[i] = wp(n, i, -1);
        }

        for (int i=0; i<n; i++) {
            int q=0;
            double sum=0;
            for (int j=0; j<n; j++)
                if (m[i][j]!='.') {
                    q++;
                    sum+= wp(n,j,i);
                }
            w2[i]=sum/q;
        }

        for (int i=0; i<n; i++) {
            int q=0;
            double sum=0;
            for (int j=0; j<n; j++)
                if (m[i][j]!='.') {
                    q++;
                    sum+= w2[j];
                }
            w3[i]=sum/q;
            printf("%.8lf\n",0.25*w1[i]+0.5*w2[i]+0.25*w3[i]);
        }
    }
    return 0;
}
