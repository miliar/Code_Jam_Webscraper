#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iomanip>

#define EPS 1e-10
#define PI (2.*acos(0))

using namespace std;

double f,R,t,r,g;

bool equal(double a, double b){
    return abs(a-b)<EPS;
}

bool inside(double y, double x){
    double dist2=y*y+x*x;
    return dist2<R*R;
}

double corresp(double k){
    return sqrt(R*R-k*k);
}

double integr(double x){
    if (equal(x,0.)) return 0;
    return corresp(x)*x/2. + PI*R*R*(PI/2.-acos(x/R))/(2.*PI);
}

double area(double y, double x){
    bool ul=inside(y+g,x),ur=inside(y+g,x+g),br=inside(y,x+g);
    if (ur) return g*g;
    else if (ul && br){
        double xc=corresp(y+g);
        return (xc-x)*g + integr(x+g)-integr(xc)-y*(x+g-xc);
    }
    else if (!ul && br){
        return integr(x+g)-integr(x)-y*g;
    }
    else if (ul && !br){
        double xc1=corresp(y+g),xc2=corresp(y);
        return (xc1-x)*g + integr(xc2)-integr(xc1)-y*(xc2-xc1);
    }
    else{
        double xc=corresp(y);
        return integr(xc)-integr(x)-y*(xc-x);
    }
}

int main(){
    int n;
    cin>>n;
    for (int cn=0;cn<n;++cn){
        cin>>f>>R>>t>>r>>g;
        double A_total,A_void=0.;
        A_total=PI*R*R;
        R-=t+f;
        r+=min(g/2.,f);
        g-=min(g,f*2.);
        for (double i=r;i<R;i+=g+(2.*r)){
            double xlim=corresp(i);
            for (double j=r;j<xlim;j+=g+(2.*r)){
                A_void+=area(i,j);
            }
        }
        double prob=(A_total-4.*A_void)/A_total;
        cout<<"Case #"<<cn+1<<": "<<fixed<<setprecision(6)<<prob<<endl;
    }
}
