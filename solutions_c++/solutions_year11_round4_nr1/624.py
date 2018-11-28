#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct WalkWay {
    int b, e, w;
    WalkWay(int b, int e, int w) : b(b), e(e), w(w) { }
    bool operator<(const WalkWay& other) const {
        return b < other.b;
    }
};

struct Interval {
    int length, speed;
    Interval(int length, int speed) : length(length), speed(speed) { }
    bool operator<(const Interval& other) const {
        if (speed != other.speed)
            return speed < other.speed;
        return length > other.length;
    }
};

double solve()
{
    vector<WalkWay> walkways;
    int X, S, R, t, N;
    cin >> X >> S >> R >> t >> N;
    for (int i = 0; i < N; i++) {
        int B, E, w;
        cin >> B >> E >> w;
        walkways.push_back(WalkWay(B, E, w));
    }
    sort(walkways.begin(), walkways.end());
    vector<Interval> intervals;
    int x = 0;
    for (int i = 0; i < N; i++) {
        if (x < walkways[i].b)
            intervals.push_back(Interval(walkways[i].b - x, S));
        intervals.push_back(Interval(walkways[i].e - walkways[i].b,
                    walkways[i].w + S));
        x = walkways[i].e;
    }
    if (x < X)
        intervals.push_back(Interval(X - x, S));
    sort(intervals.begin(), intervals.end());
    /*
    cout << endl << "Here are the intervals: " << endl;
    for (int i = 0; i < intervals.size(); i++)
        cout << "length: " << intervals[i].length
             << " speed: " << intervals[i].speed << endl;
    */ 

    double runningLeft = t;
    double timeSpent = 0;
    double extraSpeed = R - S;
    for (int i = 0; i < intervals.size(); i++) {
        double length = intervals[i].length;
        double speed = intervals[i].speed;
        double newSpeed = speed + extraSpeed;
        if (runningLeft * newSpeed > length) {
            runningLeft -= length / newSpeed;
            timeSpent += length / newSpeed;
        } else {
            timeSpent += runningLeft + (length - runningLeft * newSpeed) / speed;
            runningLeft = 0.0;
        }
        // cout << "timespent = " << timeSpent << endl;
    }

    return timeSpent;
}

int main()
{
    int T;
    cin >> T;
    cout.precision(10);
    cout.setf(ios::fixed,ios::floatfield);
    for (int t = 1; t <= T; t++) {
        double answer = solve();
        cout << "Case #" << t << ": " << answer << endl;
    }
}
