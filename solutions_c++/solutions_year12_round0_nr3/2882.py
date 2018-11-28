#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
using namespace std;

bool isrecycled(int m, int n)
{
    char ms[10], ns[10], nw[10];
    sprintf(ms, "%d", m);
    sprintf(ns, "%d", n);
    int maxm=strlen(ms)-1;
    nw[maxm+1]='\0';
    for(int i=1; i<=maxm; i++){
        char *nwp=nw;
        memcpy(nwp, ms+maxm+1-i, i);
        nwp+=i;
        memcpy(nwp, ms, maxm+1-i);

        if(memcmp(nw, ns, maxm+1)==0){
            //cout << m << ' ' << n << endl;
            return true;
        }
    }
    return false;
}

int main()
{
    ifstream in("C-small-attempt0.in");
    ofstream out("ans.out");
    int t;
    in >> t;
    in.ignore(50, '\n');
    for(int i=0; i<t; i++){
        int a, b;
        in >> a >> b;
        int ans=0;
        out << "Case #" << i+1 << ": ";
        for(int i=a; i<=b; i++){
            for(int j=a; j<=b; j++){
                if(i!=j){
                    ans+=isrecycled(i, j);
                }
            }
        }
        out << ans/2 << endl;
    }
    //cout << isrecycled(12345, 34512) << endl;
    return 0;
}


