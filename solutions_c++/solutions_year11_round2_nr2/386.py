#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <algorithm>

#include <cmath>

using namespace std;

struct cluster {
    double center;
    double radius;
    double time;
};

int main() {
    ifstream in("B.in");
    ofstream out("B.out");

    int tests;
    in >> tests;
    for (int t = 1; t <= tests; ++t) {
        int result = 0;

        int clusts, dist;
        in >> clusts >> dist;

        vector<pair<double, double> > setup;
        for (int i = 0; i < clusts; ++i) {
            double pos, vend;
            in >> pos >> vend;

            setup.push_back(make_pair(pos, vend));
        }
        sort(setup.begin(), setup.end());

        cluster cum;
        cum.center = setup[0].first;
        cum.radius = (double)dist * (setup[0].second - 1) / 2.0;
        cum.time   = cum.radius;
        cum.radius += (double)dist / 2.0;

        for (int i = 1; i < setup.size(); ++i) {
            cluster c;
            c.center = setup[i].first;
            c.radius = (double)dist * (setup[i].second - 1) / 2.0;
            c.time   = c.radius;
            c.radius += (double)dist / 2.0;

            if (cum.center > c.center) {
                cluster tmp = c;
                c = cum;
                cum = tmp;
            }

            double overlap = (cum.center + cum.radius) - (c.center - c.radius);
            if (overlap > 0) {
                double timediff = abs(cum.time - c.time);
                if (timediff > overlap) {
                    if (cum.time < c.time) {
                        cum.time   += overlap;
                        cum.center -= overlap;
                    } else {
                        c.time   += overlap;
                        c.center += overlap;
                    }
                } else {
                    double leftover = overlap - timediff;
                    if (cum.time < c.time) {
                        cum.time   += timediff;
                        cum.center -= timediff;
                    } else {
                        c.time   += timediff;
                        c.center += timediff;
                    }
                    cum.time   += leftover / 2.0;
                    cum.center -= leftover / 2.0;
                    c.time     += leftover / 2.0;
                    c.center   += leftover / 2.0;
                }

                cum.time   = max(cum.time, c.time);
                cum.center = ((cum.center - cum.radius) + (c.center + c.radius)) / 2.0;
                cum.radius = cum.radius + c.radius;
            } else {
                double gap      = -overlap;
                double timediff = abs(cum.time - c.time);
                if (timediff > gap) {
                    if (cum.time < c.time) {
                        cum.time   += gap;
                        cum.center += gap;
                    } else {
                        c.time   += gap;
                        c.center -= gap;
                    }
                } else {
                    if (cum.time < c.time) {
                        cum.time   += timediff;
                        cum.center += timediff;
                    } else {
                        c.time   += timediff;
                        c.center -= timediff;
                    }
                }

                cum.time   = max(cum.time, c.time);
                cum.center = ((cum.center - cum.radius) + (c.center + c.radius)) / 2.0;
                cum.radius = cum.radius + c.radius;
                if (timediff < gap) {
                    cum.radius += (gap - timediff) / 2.0;
                }
            }
        }

        out.precision(12);
        out << "Case #" << t << ": " << cum.time << endl;
    }
    return 0;
}

