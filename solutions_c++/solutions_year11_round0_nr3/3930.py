#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t, T, n, s, sx, i, m, c;
    ifstream f("C-large.in");
    ofstream g("a.out");
    f >> T;
    for(t = 1; t <= T; t++){
        s = sx = 0;
        f >> n;
        m = 1000001;
        for(i = 0; i < n; i++){
            f >> c;
            if(c < m)
                m = c;
            s += c;
            sx ^= c;
        }
        g << "Case #" << t <<": ";
        cout << s << endl;
        if(!sx)
            g << (s - m);
        else
            g << "NO";
        g << "\n";
    }
    return 0;
}
