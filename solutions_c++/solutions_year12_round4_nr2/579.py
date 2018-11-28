#include <fstream>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <deque>
#include <iomanip>
using namespace std;

struct Bundle
{
    int a;
    int b;
};

bool compare(Bundle a, Bundle b)
{
    return a.a < b.a;
}

int main()
{
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int T;
    in >> T;
    for (int c = 0; c < T; c++)
    {
        int N, W, L;
        in >> N >> W >> L;
        int *r = new int[N];
        int *Xi = new int[N];
        int *Yi = new int[N];
        Bundle *R = new Bundle[N];
        for (int i = 0; i < N; i++)
        {
            in >> r[i];
            R[i].a = r[i];
            R[i].b = i;
        }
        sort(R, R+N, compare);
        
        int x = 0, y = 0;
        bool transpose = (W > L);
        int X = min(W, L);
        int Y = max(W, L);
        int i = 1;
        int line = -L;
        Xi[R[0].b] = 0;
        Yi[R[0].b] = 0;
        while (i < N)
        {
            x = x + R[i-1].a + R[i].a;
            if (x <= X)
            {
                y = max(0, line + R[i].a);
            }
            else
            {
                x = 0; 
                line = y + R[i-1].a;
                y = max(0, line + R[i].a);
            }
            Xi[R[i].b] = x;
            Yi[R[i].b] = y;
            i++;
        }
        if (y > Y)
        {
            cout << "Case " << c << " error!" << endl;
        }

        out << "Case #" << (c+1) << ":";
        for (int i = 0; i < N; i++)
        {
            if (transpose)
            {
                out << " " << Yi[i] << " " << Xi[i];
            }
            else
            {
                out << " " << Xi[i] << " " << Yi[i];
            }
        }
        
        out << endl;
        delete [] r;
        delete [] Xi;
        delete [] Yi;
        delete [] R;
    }
    in.close();
    out.close();
    return 0;
}
