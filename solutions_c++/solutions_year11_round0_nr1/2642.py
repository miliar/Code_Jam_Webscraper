
#include <iostream>
#include <vector>

// 3
// 4 O 2 B 1 B 2 O 4
// 3 O 5 O 8 B 100
// 2 B 2 B 1

using namespace std;
typedef std::vector<int> VI;
typedef std::vector<char> VC;

void
do_test(int test_num, VC &robots, VI &buttons)
{
    int ns = robots.size();
    
    int op = 1;  // orange pos
    int odp = 0; // orange desired pos
    int os = 0; // orange step
    
    int bp = 1;  // blue pos
    int bdp = 0; // blue desired pos
    int bs = 0;  // blue step

    int s = 0; // current step

    int t = 0; // timer

    int i = 0;

    // Set initial desired position
    for (i = 0; i < ns; ++i) {
        if (odp == 0 && robots[i] == 'O') {
            odp = buttons[i];
            os = i;
        }
        if (bdp == 0 && robots[i] == 'B') {
            bdp = buttons[i];
            bs = i;
        }
        if (odp != 0 && bdp != 0) break;
    }

    while (odp != 0 || bdp != 0) {
        bool step = false;
        if (odp == 0) {
            // nothing
        } else if (op < odp) {
            ++op;
        } else if (op > odp) {
            --op;
        } else if (s == os) {
            step = true;
            os++;
            bool done = true;
            for (i = os; i < ns; ++i) {
                if (robots[i] == 'O') {
                    odp = buttons[i];
                    os = i;
                    done = false;
                    break;
                }
            }
            if (done) {
                odp = 0;
            }
                    
        }

        if (bdp == 0) {
            // nothing
        } else if (bp < bdp) {
            ++bp;
        } else if (bp > bdp) {
            --bp;
        } else if (s == bs) {
            step = true;
            bs++;
            bool done = true;
            for (i = bs; i < ns; ++i) {
                if (robots[i] == 'B') {
                    bdp = buttons[i];
                    bs = i;
                    done = false;
                    break;
                }
            }
            if (done) {
                bdp = 0;
            }
        }
        if (step) s++;
        t++;
    }

    cout << "Case #" << test_num << ": " << t << endl;
}

int
main(int argc, char **argv)
{
    int num_tests = 0;

    cin >> num_tests;

    for (int i = 1; i <= num_tests; ++i) {
        int num_buttons = 0;
        char r = 0;
        int p = 0;
        VC robots;
        VI buttons;
        
        cin >> num_buttons;
        for (int j = 0; j < num_buttons; j++) {
            cin >> r;
            cin >> p;
            robots.push_back(r);
            buttons.push_back(p);
            // cout << r << " " << p << " ";
        }
        // cout << endl;

        do_test(i, robots, buttons);

    }
}
    
