#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

double f, R, t, rs, g;

void getCenter(int nx, int ny, double& x, double& y) {
    x = rs + g / 2 + nx * (g + 2 * rs);
    y = rs + g / 2 + ny * (g + 2 * rs);
}

int main(int argc, char* argv[]) {
    string name = argv[1];
    string outName = name + ".out";
    ifstream in(name.c_str());
    ofstream out(outName.c_str());
    int n;
    in >> n;
    for (int i = 0; i < n ; i++) {
        in >> f >> R >> t >> rs >> g;
        double s1 = 3.141592653589793 * R * R / 4;
        R -= t;

        double effG = g - 2 * f;
        double rlim = R - g / sqrt(2.0);// - (f + effG / sqrt(2.0));
        double rlim2 = R + g / sqrt(2.0);
        
        int n = R / (g + 2 * rs) + 1; // 1 is reserved
        
        double x1, y1;
        double total = 0;

        if (0!=effG) {
            for (int y = 0; y < n; ++y) {
                for (int x = 0; x < n; ++x) {
                    getCenter(x, y, x1, y1);
                    int sum = 0;
                    
                    double reff = (R - f) * (R-f);
                    double maxX = x1 + effG / 2;
                    double maxY = y1 + effG / 2;
                    if (maxX * maxX + maxY * maxY < reff) {
                        total += 1.0;
                        continue;
                    }

                    double minY = y1 - effG / 2;
                    int count = 100000;
                    double dx = effG / count;
                    double x1 = maxX;
                    double s = 0;
                    for (int k = 0; k < count; ++k) {
                        double l = reff - x1 * x1;
                        if (l >= 0) {
                            double y = sqrt(l);
                            if (y > minY) {
                                y = std::min(y, maxY);
                                s += (y - minY);
                            }
                        }
                        x1 -=dx;

                    }
                    total += s * dx / (effG * effG);
                }
            }
        }
        
        
        total *= effG * effG;
        char buf[100];
        sprintf(buf, "%.8f", 1 - total / s1);
        cout << "Case #" << i + 1 << ": " << buf<<  endl;
    }
}

