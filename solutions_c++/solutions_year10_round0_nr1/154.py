#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int nTC;
int N, nSnap;

int main () {
    scanf ("%d", &nTC);
    
    for (int tc = 1; tc <= nTC; tc++) {
        scanf ("%d%d", &N, &nSnap);
        
        int perlu = (1 << N);
        
        bool on;
        if (nSnap % perlu == perlu - 1)
           on = true;
        else {
             on = false;
        }
        
        printf ("Case #%d: ", tc);
        if (on)
           puts ("ON");
        else
            puts ("OFF");
    }
    
    return 0;
}
