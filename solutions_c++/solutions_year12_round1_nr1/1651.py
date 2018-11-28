#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <cfloat>
using namespace std;
#define DEBUG
#ifdef DEBUG
#define dprint(var) cout << #var << '=' << var << endl
#else
#define dprint(var)
#endif

#define minF(x, y) (x<y? x: y)
//#define SUM_X(x) (((x)*(x)-(x))/2)

int t, a, b;
float p[99999];
float avg=0.;

void ikeeped(int mist, int pos, float chance)
{
    if(pos==a){
        if(mist==0){
            //dprint(chance*(b-a+1));
            avg+=chance*(b-a+1);
        }
        else{
            avg+=chance*(2*b-a+2);
        }
    }
    else{
        ikeeped(mist, pos+1, chance*p[pos]);
        ikeeped(mist+1, pos+1, chance*(1.-p[pos]));
    }
}
void ibks(int mist, int pos, float chance, int bks, int fmst)
{
    if(pos==a){
        if(mist==0 || pos-bks<=fmst){
            //cout << b-a+1+bks*2 << endl;
            avg+=chance*(b-a+1+bks*2);
        }
        else{
            //cout << 2*b-a+2+bks*2 << endl;
            //dprint(fmst);
            //dprint(a);
            avg+=chance*(2*b-a+2+bks*2);
        }
    }
    else{
        ibks(mist, pos+1, chance*p[pos], bks, fmst);
        if(p[pos]<1.)
            ibks(mist+1, pos+1, chance*(1.-p[pos]), bks, fmst==-1? pos : fmst);

    }
}
int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("output.txt");
    in >> t;
    out << fixed;

    for(int i=0; i<t; i++){
        avg=0.;
        in >> a >> b;
        float y;
        for(int j=0; j<a; j++)
            in >> p[j];

        float keeped=1.;
        for(int j=0; j<a; j++)
            keeped*=p[j];
        keeped*=b-a+1;
        ikeeped(0, 0, 1.);
        y=avg;
        //dprint(avg);
        y=minF(y, b+2.);
        for(int j=1; j<=a; j++){
            avg=0.;
            ibks(0, 0, 1., j, -1);
            y=minF(y, avg);
        //dprint(avg);
        }
        //dprint(keeped);


        out << "Case #" << i+1 << ": "  << setprecision(6)<< y << endl;
    }
    return 0;
}



/*
        for(int j=0; j<n; j++){

        }
*/
