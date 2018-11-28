#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

#define sz size()
#define pb push_back
#define len length()
#define clr clear()

#define eps 0.0000001
#define PI  3.14159265359

char s[555][555];

int main() {

    FILE *ff=fopen("A-large.in", "r"), *gg=fopen("A-large.out", "w");
    //FILE *ff=fopen("A-small-attempt00.in", "r"), *gg=fopen("A-small-attempt00.out", "w");

    int tt,ttt,n,i,j,l,br,q,br1;
    double wp[555],owp[555],oowp[555];

    fscanf(ff,"%d", &ttt);
    for(tt=1;tt<=ttt;tt++) {

        fscanf(ff,"%d", &n);
        for(i=0; i<n; i++) {
            fscanf(ff,"%s", &s[i]);
            br=0; wp[i]=0;
            for(j=0; j<n; j++) if (s[i][j]!='.') {
                wp[i]+=(s[i][j]-'0');
                br++;
            }

            wp[i]/=double(br);
            //printf("wp[%d] = %.5lf\n", i,wp[i]);
        }

        for(i=0; i<n; i++) {
            br=0; owp[i]=0;
            for(j=0; j<n; j++) if(s[i][j]!='.') {
               br++;
               q=0;
               br1=0;
               for(l=0; l<n; l++) if (l!=i && s[j][l]!='.') {
                   br1++;
                   q+=s[j][l]-'0';
               }
               if (br1>0) owp[i]+=double(q)/double(br1);
            }
            owp[i]/=double(br);
            //printf("owp[%d] = %.5lf\n", i,owp[i]);
        }

        for(i=0; i<n; i++) {
            br=0; oowp[i]=0;
            for(j=0; j<n; j++) if(s[i][j]!='.') {
               br++;
               oowp[i]+=owp[j];
            }
            oowp[i]/=double(br);
            //printf("oowp[%d] = %.5lf\n", i,oowp[i]);
        }

        fprintf(gg,"Case #%d:\n", tt);
        for(i=0; i<n; i++) fprintf(gg,"%.9lf\n", 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
    }

    fclose(ff); fclose(gg);

    return 0;
}
