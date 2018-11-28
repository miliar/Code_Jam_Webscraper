#include <fstream>

using namespace std;

int a[1024], b[1024], n;

int main()
{
    int T, x, i, j, nr;
    ifstream f("al.in");
    ofstream g("a.out");
    f >> T;
    for(x = 1; x <= T; x++){
        nr = 0;
        f >> n;
        for(i = 0; i < n; i++)
            f >> a[i] >> b[i];
        for(i = 0; i < n; i++)
            for(j = i + 1; j < n; j++)
                if(a[i] < a[j] && b[i] > b[j] || a[i] > a[j] && b[i] < b[j])
                    nr++;
        g << "Case #" << x <<": " << nr << "\n";
    }

    return 0;
}
