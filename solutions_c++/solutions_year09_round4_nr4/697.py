#include <iostream>
#include <cstdio>
#include <queue>
#include <stack>
#include <cctype>
#include <sstream>
#include <vector>
#include <fstream>
#include <cmath>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

struct circ {
    double x,y,r;
    circ(double a, double b, double c) {
        x=a; y=b; r=c;
    }
};

int main() {
        freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;

    for( int test=1; test<=T; test++ ) {
        int N;
        vector<circ> c;
        cin >> N;
        for( int i=0; i<N; i++ ) {
            double x,y,r;
            cin >> x >> y >> r;
            c.push_back( circ(x,y,r) );
        }

        double best=INT_MAX;
        if(c.size()==3) {
            for( int i=0; i<c.size(); i++ ) {
                for( int j=i+1; j<c.size(); j++ ) {
                    int other=(i==0&&j==1)?2:(i==0&&j==2)?1:0;
                    //cout << i << " " << j << " " << other << endl;
                    //if one doesn't contain the other
                    double comp;
                    if( hypot(c[i].x-c[j].x,c[i].y-c[j].y)>=c[i].r+c[j].r )
                        comp=(hypot(c[i].x-c[j].x,c[i].y-c[j].y)+c[i].r+c[j].r)/2.0;
                    else if( hypot(c[i].x-c[j].x,c[i].y-c[j].y)+min(c[i].r,c[j].r) <= max(c[i].r,c[j].r) )
                        comp=max(c[i].r,c[j].r);
                    else
                        comp=hypot(c[i].x-c[j].x,c[i].y-c[j].y)/2.0+max(c[i].r,c[j].r), cout <<"3"<<endl;
                    best=min(best,max(comp,c[other].r));

                    //cout << best << endl;
                }
            }
        }
        else if(c.size()==2) {
            best=max(c[0].r,c[1].r);
        }
        //cout << "Case #" << test << ": " << best/2.0 << endl;
        else if(c.size()==1) best=c[0].r;

        printf("Case #%d: %.6lf\n",test,best);
    }


    return 0;
}
