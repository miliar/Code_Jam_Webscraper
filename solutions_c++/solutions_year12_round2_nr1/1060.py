#include <stdio.h>
#include <algorithm>
using namespace std;

int s[1000];
double pos[1000];
void solve(){
    int n;
    scanf("%d",&n);
    double X =0;
    for (int i=0;i<n;i++) scanf("%d",&s[i]),X+=s[i];
    
    for (int i=0;i<n;i++){
      double up = 1 , low = 0;
      double best = 1;
           while ( up - low > 1e-12){
            double mid = (up+low)/2;
            double ellima = 0;
            for (int j=0;j<n;j++){
              pos[j] = (((double) s[j]) - ((double) s[i]))/((double) X);
              if ( i != j && pos[j] < mid ) ellima+= mid - pos[j];
            }
            if ( ellima > 1 - mid) best = min(best,mid),up = mid;
            else  low = mid;

        }
    printf("%.6lf ",100*best);
    }


}


int main(){
    int t;
    scanf("%d",&t);
    for (int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
        putchar('\n');
    }
    return 0;
}
