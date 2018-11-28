
#include <iostream>
#include <vector>
#include <map>

using namespace std;

#include <cmath>

//#define debug

int main() {

    unsigned int N;
    cin >> N;

    for (int u = 0; u < N; u++) {
        unsigned int num;
        cin >> num;

        #ifdef debug
        cerr << "num readed " << num << endl;
        #endif

        int *x = new int[num], *y = new int[num], *z = new int[num];
        int *vx = new int [num], *vy = new int[num], *vz = new int[num];

        #ifdef debug
        cerr << "mem allocated " << num << endl;
        #endif

        int psx = 0, psy = 0, psz = 0;
        int ppx = 0, ppy = 0, ppz = 0;
        double prec = ((double)1)/((double)num);

        #ifdef debug
        cerr << "prec " << prec << endl;
        #endif
        for (int i = 0; i < num; i++) {
            cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
            #ifdef debug
            cerr << " (" << x[i] << ", " << y[i] << ", " << z[i] << ") (" << vx[i] << ", " << vy[i] << ", " << vz[i] << ") " << endl;
            #endif
//            sx += ((double)vx[i])*prec; sy += ((double)vy[i])*prec; sz += ((double)vz[i])*prec;
//            px += ((double)x[i]) *prec; py += ((double)y[i]) *prec; pz += ((double)z[i]) *prec;

            psx += vx[i]; psy += vy[i]; psz += vz[i];
            ppx += x[i]; ppy += y[i]; ppz += z[i];
        }

        double sx = ((double)psx)*prec, sy = ((double)psy)*prec, sz = ((double)psz)*prec;
        double px = ((double)ppx)*prec, py = ((double)ppy)*prec, pz = ((double)ppz)*prec;
        
        #ifdef debug
        cerr << u << " Readed... " << endl;
        cerr << " v: (" << sx << ", " << sy << ", " << sz <<" )  pos: (" << px << ", " << py << ", " << pz << ") " << endl;
        #endif

        // calculating min distance
        double min_d = 0.0, min_t = 0.0;

        if (!((sx == 0) && (sy == 0) && (sz == 0))) {
            double sq = (sx*sx + sy*sy + sz*sz);
            min_t = - ((px*sx) / sq + (py * sy )/sq + (pz*sz) /sq);
        }

        if (min_t < 0)
            min_t = 0;
        double min_x = min_t*sx + px, min_y = min_t*sy + py, min_z = min_t*sz + pz;

        #ifdef debug
        cerr << u << " t calc " << endl;
        #endif


        min_d = sqrt( min_x*min_x + min_y *min_y + min_z*min_z);
        printf("Case #%d: %.7f %.7f\n", u+1, min_d, min_t);
//        cout << "Case #" << u+1 << ": " << result << endl;
/*
        delete x;
        delete y;
        delete z;
        delete vx;
        delete vy;
        delete vz;

*/
    }

    return 0;
}
