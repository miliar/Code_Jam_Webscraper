#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

#define PI 3.1415926

int main(int argv, char** argc)
{
    ifstream in("C-large.in");
    int test;
    in >> test;

    for (int i=0; i<test; ++i)
    {
        double f, R, t, r, g;
        in >> f >> R >> t >> r >> g;
        
        t += f;
        r += f;
        g -= 2*f;

        double result=0;
        if (g <= 0)
        {
            result = 1;
            cout << "Case #" << i+1 << ": " << result << endl;
            continue;
        }

        int n;
        double nnn = ((R-t + r) / (g + 2*r));
        if (nnn > (int)nnn)
            n = (int)nnn + 1;
        else
            n = (int)nnn;

        //cout << nnn << " " << n << endl;

        double x = -r;
        double y = -r;
        vector<vector<int> > points(2*n);
        vector<vector<double> > cx(2*n);
        vector<vector<double> > cy(2*n);

        for (int j=0; j<2*n; ++j)
        {
            points[j].resize(2*n, 0);
            cx[j].resize(2*n, 0);
            cy[j].resize(2*n, 0);
        }

        for (int p=0; p<n; ++p)
        {
            x = -r;
            y += 2*r;
            for (int q=0; q<n; ++q)
            {
                x += 2*r;
                cx[p*2][q*2] = x;
                cy[p*2][q*2] = y;

                if (pow(x, 2) + pow(y, 2) <= pow(R - t, 2))
                    points[p*2][q*2] = 1;
                else
                    points[p*2][q*2] = 0;

                x += g;
                cx[p*2][q*2+1] = x;
                cy[p*2][q*2+1] = y;

                if (pow(x, 2) + pow(y, 2) <= pow(R - t, 2))
                    points[p*2][q*2+1] = 1;
                else
                    points[p*2][q*2+1] = 0;

            }
            y += g;
            x = -r;
            for (int q=0; q<n; ++q)
            {
                x += 2*r;
                cx[p*2+1][q*2] = x;
                cy[p*2+1][q*2] = y;

                if (pow(x, 2) + pow(y, 2) <= pow(R - t, 2))
                    points[p*2+1][q*2] = 1;
                else
                    points[p*2+1][q*2] = 0;

                x += g;
                cx[p*2+1][q*2+1] = x;
                cy[p*2+1][q*2+1] = y;

                if (pow(x, 2) + pow(y, 2) <= pow(R - t, 2))
                    points[p*2+1][q*2+1] = 1;
                else
                    points[p*2+1][q*2+1] = 0;
            }
        }
        
        vector<vector<int> > square(n);
        for (int j=0; j<n; ++j)
            square[j].resize(n, 0);

        for (int p=0; p<n; ++p)
        {
            for (int q=0; q<n; ++q)
            {
                int count = 0;
                count += points[p*2][q*2];
                count += points[p*2][q*2+1];
                count += points[p*2+1][q*2];
                count += points[p*2+1][q*2+1];
                square[p][q] = count;
            }
        }

        /*
        cout << "points: " << endl;
        for (int p=2*n-1; p>=0; --p)
        {
            for (int q=0; q<2*n; ++q)
                cout << points[p][q] << " ";
            cout << endl;
        }
        
        cout << "square: " << endl;
        for (int p=n-1; p>=0; --p)
        {
            for (int q=0; q<n; ++q)
                cout << square[p][q] << " ";
            cout << endl;
        }
        */

        double R1 = R - t;
        double x1, x2, x3, x4, x5;
        double y1, y2, y3, y4, y5;
        double allsss = 0;
        double angle = 0;
        double sss = 0;
        for (int p=0; p<n-1; ++p)
        {
            for (int q=p+1; q<n; ++q)
            {
                if (square[p][q] == 1)
                {
                    x1 = cx[p*2][q*2];
                    y1 = cy[p*2][q*2];
                    x2 = x1;
                    y2 = sqrt(R1*R1 - x1*x1);
                    x3 = sqrt(R1*R1 - y1*y1);
                    y3 = y1;
                    angle = asin(y2/R1) - asin(y1/R1);
                    sss = 0.5*angle*R1*R1 + 0.5*x2*y2 - 0.5*x3*y3 - x1*(y2-y1);
                    allsss += sss;
                }
                else if (square[p][q] == 2)
                {
                    x1 = cx[p*2+1][q*2];
                    y1 = cy[p*2+1][q*2];
                    x2 = cx[p*2][q*2];
                    y2 = cy[p*2][q*2];
                    x3 = sqrt(R1*R1 - y1*y1);
                    y3 = y1;
                    x4 = sqrt(R1*R1 - y2*y2);
                    y4 = y2;
                    angle = asin(y1/R1) - asin(y2/R1);
                    sss = 0.5*angle*R1*R1 + 0.5*x3*y3 - 0.5*x4*y4 - x1*(y1-y2);
                    allsss += sss;
                }
                else if (square[p][q] == 3)
                {
                    x1 = cx[p*2+1][q*2];
                    y1 = cy[p*2+1][q*2];
                    x2 = cx[p*2][q*2];
                    y2 = cy[p*2][q*2];
                    x3 = sqrt(R1*R1 - y1*y1);
                    y3 = y1;
                    x4 = cx[p*2][q*2+1];
                    y4 = cy[p*2][q*2+1];
                    x5 = x4;
                    y5 = sqrt(R1*R1 - x4*x4);
                    angle = asin(y3/R1) - asin(y5/R1);
                    sss = 0.5*angle*R1*R1 + 0.5*x5*y5 + 0.5*x3*y3 - x4*y4 - x1*(y1-y2);
                    allsss += sss;

                }
                else if (square[p][q] == 4)
                {
                    allsss += (g * g);
                }
            }
        }
        
        allsss *= 8;

        double partsss = 0;
        for (int p=0; p<n; ++p)
        {
            for (int q=p; q<p+1; ++q)
            {
                if (square[p][q] == 1)
                {
                    x1 = cx[p*2][q*2];
                    y1 = cy[p*2][q*2];
                    x2 = x1;
                    y2 = sqrt(R1*R1 - x1*x1);
                    x3 = sqrt(R1*R1 - y1*y1);
                    y3 = y1;
                    angle = asin(y2/R1) - asin(y1/R1);
                    sss = 0.5*angle*R1*R1 + 0.5*x2*y2 - 0.5*x3*y3 - x1*(y2-y1);
                    partsss += sss;
                }
                else if (square[p][q] == 2)
                {
                    x1 = cx[p*2+1][q*2];
                    y1 = cy[p*2+1][q*2];
                    x2 = cx[p*2][q*2];
                    y2 = cy[p*2][q*2];
                    x3 = sqrt(R1*R1 - y1*y1);
                    y3 = y1;
                    x4 = sqrt(R1*R1 - y2*y2);
                    y4 = y2;
                    angle = asin(y1/R1) - asin(y2/R1);
                    sss = 0.5*angle*R1*R1 + 0.5*x3*y3 - 0.5*x4*y4 - x1*(y1-y2);
                    partsss += sss;
                }
                else if (square[p][q] == 3)
                {
                    x1 = cx[p*2+1][q*2];
                    y1 = cy[p*2+1][q*2];
                    x2 = cx[p*2][q*2];
                    y2 = cy[p*2][q*2];
                    x3 = sqrt(R1*R1 - y1*y1);
                    y3 = y1;
                    x4 = cx[p*2][q*2+1];
                    y4 = cy[p*2][q*2+1];
                    x5 = x4;
                    y5 = sqrt(R1*R1 - x4*x4);
                    angle = asin(y3/R1) - asin(y5/R1);
                    sss = 0.5*angle*R1*R1 + 0.5*x5*y5 + 0.5*x3*y3 - x4*y4 - x1*(y1-y2);
                    partsss += sss;

                }
                else if (square[p][q] == 4)
                {
                    partsss += (g * g);
                }
            }
        }

        allsss = allsss + partsss * 4;
        
        //cout << allsss << endl;
        //cout << PI * R * R << endl;
        
        result = 1 - allsss / (PI * R * R);

        cout << "Case #" << i+1 << ": " << result << endl;
    }
}
