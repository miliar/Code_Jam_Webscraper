
#include <iostream>
#include <vector>


using namespace std;
typedef std::vector<int> VI;
typedef std::vector<char> VC;

double
winpct(int team, int ignore, vector<vector<char> > &rec) {
    int n = rec.size();
    int ngames = 0;
    int nwon = 0;
    for (int i = 0; i < n; ++i) {
        if (i == team) {
            continue;
        } else if (i == ignore) {
            continue;
        } else if (rec[team][i] == '.') {
            continue;
        } else {
            ++ngames;
            if (rec[team][i] == '1') ++nwon;
        }
    }
    
    return (static_cast<double>(nwon) / static_cast<double>(ngames));
}

double
wp(int team, vector<vector<char> > &rec) {
    return winpct(team, -1, rec);
}

double
owp(int team, vector<vector<char> > &rec) {
    int n = rec.size();
    int nopp = 0;
    double val = 0.0;
    for (int i = 0; i < n; i++) {
        if (i == team) continue;
        if (rec[team][i] == '.') continue;
        nopp++;
        val += winpct(i, team, rec);
    }
            
    return val / nopp;
}

double
oowp(int team, vector<vector<char> > &rec) {
    int n = rec.size();
    int nopp = 0;
    double val = 0.0;
    for (int i = 0; i < n; i++) {
        if (i == team) continue;
        if (rec[team][i] == '.') continue;
        nopp++;
        val += owp(i, rec);
    }
    return val / nopp;
}

double
rpi(int team, vector<vector<char> > &rec) {
    double v1 = 0.25 * wp(team, rec);
    double v2 = 0.50 * owp(team, rec);
    double v3 = 0.25 * oowp(team, rec);
    return v1 + v2 + v3;
}

void
do_test(int test_num, vector<vector<char> > &rec)
{
    cout << "Case #" << test_num << ": " << endl;
    for (int i = 0; i < rec.size(); i++) {
        // cout << "wp " << i << " " << wp(i, rec) << endl;
        printf("%.12f\n", rpi(i, rec));
    }
}

int
main(int argc, char **argv)
{
    int num_tests = 0;

    cin >> num_tests;

    for (int i = 1; i <= num_tests; ++i) {
        int n;
        cin >> n;

        vector<vector<char> > rec(n);
        
        for (int a = 0; a < n; ++a)
            rec[a] = vector<char>(n);
        
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                char c;
                cin >> c;
                rec[j][k] = c;
            }
        }
            
        do_test(i, rec);
    }
}
    
