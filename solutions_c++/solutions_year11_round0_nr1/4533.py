/**/
#include <algorithm>
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <limits.h>
#include <cstdlib>
#include <vector>
#include <math.h>
#include <map>
using namespace std;

int main(int argc, char** argv) {
    freopen ("entrada.txt","r",stdin);
    freopen ("salida.txt","w",stdout);
    int casos;
    cin>>casos;
    char c;
    int pos, n;
    int pa, pn, ta,tn;
    for (int ncasos=1; ncasos<=casos; ncasos++){
        cin>>n;
        pa=pn=1; ta=tn=0;
        while (n--){
            cin>>c>>pos;
            if (c=='O'){
                tn+=abs(pos-pn);
                if (tn<ta) tn=ta;
                pn=pos;
                tn++;
            }
            else{
                ta+=abs(pos-pa);
                if (ta<tn) ta=tn;
                pa=pos;
                ta++;
            }
        }

        cout<<"Case #"<<ncasos<<": "<<((ta>tn)?ta:tn)<<endl;
    }
    return 0;
}

/**/
