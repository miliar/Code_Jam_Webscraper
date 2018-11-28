#include <cstdio>
#include <cstdlib>
#include <map>

using namespace std;


int TRIALS;

void trial(int T) {
    printf("Case #%d:\n", T);
    int W; int L; int U; int G;
    scanf("%d%d%d%d", &W,&L,&U,&G);
    map<int, double> LB;
    map<int, double> UB;
    LB.clear();
    UB.clear();
    //Do stuff
    for (int i = 0; i < L; i++)
    {
        int X; double Y;
        scanf("%d %lf", &X, &Y);
        LB[X] = Y;
    }
    for (int i = 0; i < U; i++)
    {
        int X; double Y;
        scanf("%d %lf", &X, &Y);
        UB[X] = Y;
        map<int, double>::iterator it = LB.lower_bound(X);
        if (it->first == X) continue;
        double lx = it->first; double ly = it->second;
        it--;
        LB[X] = ((double)X - it->first) / (lx - it->first) * (ly - it->second) + it->second;
    }
    double area = 0.0;
    double prevH = 0.0;
    int xpos = 0;
    map<double, int> ch;
    ch.clear();
    for (map<int,double>::iterator lb = LB.begin(); lb != LB.end(); lb++)
    {
        map<int, double>::iterator it = UB.lower_bound(lb->first);
        if (it->first != lb->first)
        {
            double lx = it->first; double ly = it->second;
            it--;
            UB[lb->first] = (double)(lb->first - it->first) / (lx - it->first) * (ly - it->second) + it->second;
        }
        area += (UB[lb->first] - LB[lb->first] + prevH) * (lb->first - xpos);
        ch[area] = lb->first;
        xpos = lb->first;
        prevH = UB[lb->first] - LB[lb->first];
    }
    for (int i = 1; i < G; i++)
    {
        double slice = area / G * i;
        map<double, int>::iterator it = ch.upper_bound(slice);
        int width = it->second;
        double uh = UB[it->second] - LB[it->second];
        it--;
        width -= it->second;
        double lh = UB[it->second] - LB[it->second];
        double target = slice - it->first;
        double lx = 0.0;
        double ux = (double)width;
        while (lx < ux - 1E-8)
        {
            double x = (lx + ux) / 2;
            double ar = (lh + lh + (uh-lh) * x / width) * x;
            if (ar < target) lx = x;
            else ux = x;
        }
        printf("%f\n", lx + it->second);
    }
}

int main(int argc, char* argv[]) {
    scanf("%d", &TRIALS);
    for (int T = 1; T <= TRIALS; T++) {
        trial(T);
    }

    return 0;
}
