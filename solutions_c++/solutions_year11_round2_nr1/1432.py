#include <cstdio>
using namespace std;

char c[123][123];
double wp[123],owp[123],oowp[123];

void solve (int test){
     int n;
     scanf ("%d",&n);
     for (int i=0;i<n;++i){
         scanf ("%s",c[i]);
     }
     printf ("Case #%d:\n",test);
     int br,br2;
     for (int i=0;i<n;++i){
         wp[i]=0.0;
         owp[i]=0.0;
         br=0;
         for (int j=0;j<n;++j){
             if (c[i][j]=='1' || c[i][j]=='0'){
                ++br;
                wp[i]+=(c[i][j]-'0');
             }
         }
         wp[i]/=br;
         br=0;
         double tmp=0.0;
         for (int j=0;j<n;++j){
             if (c[i][j]=='.' || j==i) continue;
             ++br;
             tmp=0.0;
             br2=0;
             for (int i2=0;i2<n;++i2){
                 if (i2!=i && (c[j][i2]=='1' || c[j][i2]=='0')){
                    tmp+=(c[j][i2]-'0');
                    ++br2;
                 }
             }
             //printf ("a %lf",owp);
             owp[i]+=(tmp/br2);
         }
         owp[i]/=br;
     }
     for (int i=0;i<n;++i){
         oowp[i]=0.0;
         br=0;
         for (int j=0;j<n;++j){
             if (i==j || c[i][j]=='.') continue;
             ++br;
             oowp[i]+=owp[j];
         }
         oowp[i]/=br;
     }
     for (int i=0;i<n;++i){
         //printf ("%lf %lf %lf\n",wp[i],owp[i],oowp[i]);
         printf ("%.7lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
     }
}

int main (){
    int t;
    scanf ("%d",&t);
    for (int i=0;i<t;++i){
        solve (i+1);
    }
    return 0;
}
