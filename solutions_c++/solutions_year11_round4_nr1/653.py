#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <iomanip>
#include <math.h>
#include <string>
#include <string.h>
using namespace std;

#define pii pair<int,int>
#define mk make_pair

typedef long long ll;

struct tri{
    int b,e,s;
    tri(){};
    tri( int p1, int p2, int p3 ):b(p1),e(p2),s(p3){};
};

int w,walk,run,tr,n;

bool bypos( tri a, tri b ){
    if( a.e <= b.b ) return 1;
    return 0;
}

bool byspeed( tri a, tri b ){
    return a.s < b.s;
}

int main(){
     freopen("Ulaz.txt","r",stdin);
     freopen("Izlaz.txt","w",stdout);

    int tests; scanf("%d",&tests);

    for( int t = 1; t <= tests; ++t ){
        scanf("%d%d%d%d%d",&w,&walk,&run,&tr,&n);


        vector< tri > x;
        for( int i = 0; i < n; ++i ){
            int a,b,c; scanf("%d%d%d",&a,&b,&c);
            x.push_back( tri(a,b,c) );
        }

        if( x[0].b > 0 )
            x.push_back( tri(0,x[0].b,0) );
        if( x[n-1].e < w )
            x.push_back( tri(x[n-1].e,w,0) );

        for( int i = 1; i < n; ++i )
            if( x[i-1].e < x[i].b ) x.push_back( tri(x[i-1].e,x[i].b,0) );

        sort( x.begin(), x.end(), byspeed );

        double td = (double)tr;

        double sol = 0;
        for( int i = 0; i < x.size(); ++i ){
            double lo = 0, hi = td;
            double h = x[i].e - x[i].b;
            double t = h / (x[i].s + walk);
           // cout<<"T: "<<t<<" | "<<h<<" , "<<x[i].s+walk<<endl;

            double t2 = h / (run+x[i].s);

            if( t2 > td ){
                double rd = (run+x[i].s) * td;
                //cout<<rd<<endl;
                h -= rd;
                t2 = td + (h / (walk+x[i].s));
                td = 0;
            }else{
                td -= t2;
            }
            //cout<<x[i].b<<" "<<x[i].e<<" = "<<t<<" "<<t2<<" [ "<<td<<" ] "<<endl;
            sol += min(t,t2);
        }

        printf("Case #%d: %.10lf\n",t,sol);
    }


    return 0;
}
