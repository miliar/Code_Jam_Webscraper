#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
    int coden, t;
    cin >> t;
    // define vars
    int x; // length of the corridor
    // 1 <= x <= 1e6
    int s; // walking speed
    int r; // running speed
    int time; // maximum time you can run, in seconds
    // 1 <= x <= 1e6
    int begin, end, wspeed;
    const int mostfast = 1000;
    double totaltime;

    int i;
    int n;
    // number of walkways
    vector <int> speed;
    vector <int> length;
    vector <bool> run;
    int halfrunind;
    double halfruntime;

    for (coden = 1; coden <= t; coden++)
    {
        speed.clear();
        length.clear();
        run.clear();
        cin >> x >> s >> r >> time >> n;

        int sum = 0;
        for (i = 0; i < n; i++) {
            cin >> begin >> end >> wspeed;
            length.push_back(end - begin);
            speed.push_back(wspeed);
            run.push_back(false);
            sum += end - begin;
        }
        speed.push_back(0);
        length.push_back(x-sum);
        run.push_back(false);
        //assert(speed.size() == length.size());
        assert(speed.size() == n + 1);
        n = speed.size();

        double acctimeleft = time;

        // acc the slowest piece
        // and find the halfrun piece
        // set $halfruntime and $halfrunind
        halfrunind = -1;
        halfruntime = 0;
        while (acctimeleft > 0) {
            int minspeed = mostfast;
            int minspeedind = -1;
            for (i = 0; i < n; i++) {
                if (!run[i] && speed[i] < minspeed) {
                    // i has not been acc
                    // and speed[i] is smallest by now
                    // then: 
                    // pick i
                    minspeed = speed[i];
                    minspeedind = i;
                }
            }
            if (minspeedind == -1) {
                // all has been acc
                break;
            }
            // acc #minspeedind
            i = minspeedind;
            double acctime = double(length[i]) / (speed[i] + r);
            if (acctime < acctimeleft) { // sometime left
                acctimeleft -= acctime;
                run[i] = true;
                continue;
            } else {
                halfruntime = acctimeleft;
                halfrunind = i;
                break;
            }
        }

        totaltime = 0;
        for (i = 0; i < n; i++) {
            if (i == halfrunind) {
                // run halfruntime
                double halfrunlength = halfruntime * (r + speed[i]);
                totaltime += halfruntime + double(length[i] - halfrunlength) / (s + speed[i]);
                //cerr << "#" << i << ": " << "speed(" << speed[i] << "), length(" << length[i] << "), run(" << halfruntime << ")" << endl;
            } else if (run[i]) {
                totaltime += double(length[i]) / (r + speed[i]);
                //cerr << "#" << i << ": " << "speed(" << speed[i] << "), length(" << length[i] << "), run(true)" << endl;
            } else {
                totaltime += double(length[i]) / (s + speed[i]);
                //cerr << "#" << i << ": " << "speed(" << speed[i] << "), length(" << length[i] << "), run(false)" << endl;
            }
            // cerr << "totaltime = " << totaltime << endl;
        }
        // output result
        cout << "Case #" << coden << ": " << setprecision(12) << totaltime << endl;
    }
    return 0;
}

