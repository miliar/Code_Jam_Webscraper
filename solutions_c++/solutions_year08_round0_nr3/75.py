#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <cassert>

using namespace std;

typedef size_t s_t;

int read_n( std::istream& is )
{
        int N;
        is >> N;
        string dummy;
        getline( cin, dummy );
        return N;
}


double PI = 3.1415926535;

double sq( double x ) { return x * x; }

double partial_sphere( double r, double q, double a0, double a1 )
{
        assert( a1 <= r );
        assert( a0 < a1 );
        double w =
                ( sq(r)*asin(a1/r)-sq(r)*asin(a0/r)+a1*sqrt(sq(r)-sq(a1))-a0*sqrt(sq(r)-sq(a0))+(2*a0-2*a1)*q )
                * 0.5; 
        //if( p < 0 ) { return 0; }
        return w;
}

double counter( double r, double x )
{
        //cerr << r << ", " << x << endl;

        assert( 0 <= x );
        assert( 0 <= r );
        assert( x <= r );
        return sqrt( sq( r ) - sq( x ) );
}

int main()
{
        string dummy;

        cout.setf(ios_base::fixed, ios_base::floatfield);
        cout.precision(6);

        cerr.setf(ios_base::fixed, ios_base::floatfield);
        cerr.precision(6);

        int N = read_n( cin );
        for( int i = 0 ; i < N ; i++ ) {
                double f, R, t, r, g;
                cin >> f >> R >> t >> r >> g;
                getline( cin, dummy );
                //cerr << f << "," << R << "," << t << "," << r << "," << g << endl;

                if( g <= f * 2.0f ) {
                        cout << "Case #" << (i+1) << ": 1.000000" << endl;
                        continue;
                }

                double S = PI * sq(R);
                double ir = R - t; // フレームをのぞいた分の半径
                double is = PI * sq(ir); // フレームをのぞいた分の面積
                double unit = r + g + r; // ユニット＝ガットの半径＋スクウェア+ガットの半径

                double aaa = 0;

                double y = 0;
                double ir2 = ir - f;

                while( y + r + f <= ir2 ) {
                        //cerr << ir2 << ", " << (y + r + f) << endl;
                        double x = 0;
                        while( x + r + f < ir2 ) {
                                double x0 = x + r + f;
                                double x1 = x + r + g - f;
                                double y0 = y + r + f;
                                double y1 = y + r + g - f;

                                if( counter( ir2, x0 ) <= y0 ||
                                    counter( ir2, y0 ) <= x0 ) {
                                        // 範囲外
                                } else if( x1 <= ir2 && y1 <= counter( ir2, x1 ) &&
                                    y1 <= ir2 && x1 <= counter( ir2, y1 ) ) {
                                        //cerr << "a\n";
                                        // 正方形
                                        aaa += sq( g - f - f );
                                        //cerr << "A: " << sq( g - f - f ) << endl;
                                } else if( y1 <= counter( ir2, x0 ) && x1 <= counter( ir2, y0 ) ) {
                                        //cerr << "b\n";
                                        // 右上欠け
                                        double a0 = counter( ir2, y1 );
                                        double a1 = x1;
                                        double j = partial_sphere( ir2, y0, a0, a1 );
                                        assert( x0 < a0 );
                                        double m = ( a0 - x0 ) * ( y1 - y0 );
                                        double k = j + m;
                                        //cerr << "B: " << a0 << ":" << a1 << ":" << j << ":" << k << endl;
                                        aaa += k;
                                } else if( y1 <= counter( ir2, x0 ) && counter( ir2, y0 ) < x1 ) {
                                        //cerr << "c\n";
                                        // 右上、右下欠け
                                        double a0 = y0;
                                        double a1 = y1;
                                        double j = partial_sphere( ir2, x0, a0, a1 );
                                        //cerr << "C: " << a0 << ":" << a1 << ":" << j << endl;
                                        aaa += j;
                                } else if( counter( ir2, x0 ) < y1 && x1 <= counter( ir2, y0 ) ) {
                                        //cerr << "d\n";
                                        // 左上、右上欠け
                                        double a0 = x0;
                                        double a1 = x1;
                                        double j = partial_sphere( ir2, y0, a0, a1 );
                                        //cerr << "D: " << a0 << ":" << a1 << ":" << j << endl;
                                        aaa += j;
                                } else if( x0 < counter( ir2, y0 ) && y0 < counter( ir2, x0 ) ) {
                                        //cerr << "e\n";
                                        // 三角
                                        double a0 = x0;
                                        double a1 = counter( ir2, y0 );
                                        double j = partial_sphere( ir2, y0, a0, a1 );
                                        //cerr << "E: " << a0 << ":" << a1 << ":" << j << endl;
                                        aaa += j;
                                }
                                x += unit;
                        }
                        y += unit;
                }

                float num = (aaa*4.0f);
                //cerr << num << "/" << S << "=" << (1.0-num/S) << endl;
                
                cout << "Case #" << (i+1) << ": " << (1.0-num/S) << endl;
        }

        return 0;
}
