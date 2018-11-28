#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define D(x)

using namespace std;

template<typename T>
ostream& operator <<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) os << ", ";
        os << v[i];
    }
    os << "]";
    return os;
}

int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int X, S, R, t, N;
        cin >> X >> S >> R >> t >> N;
        int ds = R-S;

        int Xleft = X;
        vector<pair<int, int> > lengths;
        for (int i = 0; i < N; i++) {
            int Bi, Ei, wi;
            cin >> Bi >> Ei >> wi;
            lengths.push_back(make_pair(wi, Ei-Bi));
            Xleft -= (Ei-Bi);
        }
        lengths.push_back(make_pair(0, Xleft));

        sort(lengths.begin(), lengths.end());
        double tleft = t, ttaken = 0;
        for (int i = 0; i < lengths.size(); i++) {
            int speed = lengths[i].first;
            int length = lengths[i].second;
            D(cerr << "speed=" << speed << " length=" << length << endl);

            double trunning = length / (double) (speed+R);
            trunning = min(trunning, tleft);
            if (trunning > 0) {
                ttaken += trunning;
                tleft -= trunning;
                double lengthused = trunning * (speed+R);
                double twalking = (length-lengthused) / (double) (speed+S);
                D(cerr << "  " << trunning << " (" << lengthused << ") running" << endl);
                ttaken += twalking;
            } else {

                double twalking = length / (double) (speed+S);
                D(cerr << "  " << twalking << " walking" << endl);
                ttaken+=twalking;
            }
        }


        cout.precision(10);
        cout << "Case #" << testCase << ": " << ttaken << endl;
    }
}

