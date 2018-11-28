#include <iostream>
#include <map>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;
const int MAX=10;
const double E=1e-7;
int A,B;
double p[MAX];

double subset(int x,int d){
    double pro=1.0;
    for(int i=0;i<A;i++){
        if(x&(1<<i))
            pro*=p[i];
        else
            pro*=(1.0-p[i]);
    }

    if(d==A){
        return pro*(d+B+1);
    }

    bool flag=1;
    for(int i=0;i<A-d;i++){
        if(!(x&(1<<i))){
            flag=0;
            break ;
        }
    }

    if(flag)
        return pro*(d+B-(A-d)+1);


    return pro*(d+B-(A-d)+1+B+1);
}

//double firstCorrect(){
//    double pf=1.0;
//    for(int i=0;i<A;i++)
//        pf*=p[i];
//
//    return pf*(B-A+1);
//}
//
//double lastCorrect(){
//    double
//    return ;
//}

int dbcmp (double val){
    if(val>-E&&val<E)
        return 0;
    return val>0?1:-1;
}

int main(){
//    freopen("A-small-attempt0.in","r",stdin);
//    freopen("o.txt","w",stdout);
    int T,num=1;
    cin>>T;
    while(T--){
        cin>>A>>B;

        double ans=0.0;
        double minVal=1+B+1;
//        cout<<minVal<<endl;

        for(int i=0;i<A;i++)
            cin>>p[i];

        for(int d=0;d<=A;d++){
            ans=0.0;
            for(int i=0;i<(1<<A);i++){
////                if(d==1)
////                    cout<<"         "<<subset(i,d)<<endl;
                ans+=subset(i,d);
            }

//            cout<<d<<" "<<ans<<endl;

            if(dbcmp(ans-minVal)<0){
                minVal=ans;
            }

        }

        printf("Case #%d: %lf\n",num++,minVal);
    }
    return 0;
}
