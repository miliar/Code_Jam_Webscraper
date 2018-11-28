#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <cmath>

using namespace std;

const unsigned SHOTS = 10000000;
const unsigned MAX_RAND = RAND_MAX;

istream& seekeoln(istream& is)
{
    char c;
    do
    {
        is.get(c);
    } while (c != '\n');
    return is;
}

int main()
{
    srandom(time(0));
    
    unsigned N;
    seekeoln(cin >> N);
    
    for (unsigned i = 0; i < N; ++i)
    {
        double f, R, t, r, g;
        cin >> f >> R >> t >> r >> g;
        if (g <= 2 * f)
        {
            cout << 1;
        }
        else
        {
            r += f;
            g -= 2 * f;
            t += f;
            
            const double l = g + 2 * r;
            
            unsigned acc = 0;
            for (unsigned j = 0; j < SHOTS; ++j)
            {
                const double dR = random() / double(MAX_RAND) * R;
                const double angle = random() / double(MAX_RAND) * M_PI / 2;
                const double deltaX = dR * cos(angle);
                const double deltaY = dR * sin(angle);
                
                if (dR > R - f)
                    ++acc;
                else if (deltaX < r || deltaY < r)
                    ++acc;
                else
                {
                    const unsigned dX = (deltaX - r) / l;
                    const unsigned dY = (deltaY - r) / l;
                    
                    if (deltaX - r > l * dX + g || deltaY - r > l * dY + g)
                        ++acc;
                }
            }
            cout << "Case #" << (i + 1) << ": " << setprecision(6) << (double(acc) / SHOTS) << endl;
        }
    }

}
