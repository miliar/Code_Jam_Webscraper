#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
double p[101000];
double mic[101000];
// mic[i] keep p that no any char before or eq i wrong
void solve(int test){
    int a,b;

    scanf("%d %d",&a,&b);
    for(int i=0;i<a;i++){
        scanf("%lf",&p[i]);
        if(i)p[i]*=p[i-1];
    }
    double relP=1;
    double ans=b+2;
    double wrong=0;
    double A=0;

    for(int i=1;i<=a;i++){
        // suppose we start from character i
        A=0;
        relP=1;
        int key = max(0,a-i)+1;
        A+=p[i-1]*(key+b-i);
        A+=(1-p[i-1])*(key+b-i+b+1);
        // del + enter
        /*
        for(int j=1;j<=a;j++){
            //first wrong is character j
            int rKey=0;
            if(j>i){
                //perfect
                rKey=key+b-i;
                // more type
                //A+=relP*rKey;
            }
            else{
                rKey=key+b-i+b+1;
                // more type + whole type + enter
            }
            A+=relP*(1-p[j-1])*rKey;
            relP*=p[j-1];
            //printf("%d %lf\n",j,relP);
        }*/
        //A+=relP*(key+b-i); // P that all correct
        if(A<ans)ans=A;
    }
    printf("Case #%d: %.10lf\n",test,ans);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)solve(i);
}
