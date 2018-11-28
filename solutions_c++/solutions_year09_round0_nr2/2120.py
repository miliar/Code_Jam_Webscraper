#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <string>
#include <cassert>
#include <cstdio>

using namespace std;

struct LocationData {
public:
    LocationData(int el, int r, int c, char l) : elevation(el), row(r), col(c), label(l) { }
    int elevation;
    int row;
    int col;
    char label;
};

bool SortPredicate(const LocationData & d1, const LocationData & d2) {
    if (d1.elevation > d2.elevation) {
        return true;
    } else if (d1.elevation == d2.elevation) {
        if (d1.row < d2.row) {
            return true;
        } else if (d1.row == d2.row) {
            return (d1.col < d2.col);
        }
    }

    return false;
}

void do_testcase() {
    int height;
    cin >> height;
    assert(height >= 0);
    assert(height <= 100);
    int width;
    cin >> width;
    assert(width >= 0);
    assert(width <= 100);

    int data[100][100];
    char state[100][100];

    /* vector<LocationData> priority_queue;
    priority_queue.reserve(height * width); */

    for (int row = 0; row < height; row++) {
        for (int col = 0; col < width; col++) {
            int el;
            cin >> el;

        /*    LocationData myloc(el, row, col);
            priority_queue.push_back(myloc); */
            data [row] [col] = el;
            state [row] [col] = -1;
        }
    }
//     cout << "HERE";
/*
    char basins[10000];
    int basin = 0; */

    char offset = 0;

    for (int row = 0; row < height; row++) {
        for (int col = 0; col < width; col++) {
            int temp_el = data [row] [col]; 
            int temp_r = row;
            int temp_c = col;

            if (state [row] [col] != -1) {
                continue;
            }

            std::stack<int> backtrace;

            int final_r;
            int final_c;
            char final_offset = 0;

            do {
                int lowest_el;
                int lowest_dx;
                int lowest_dy;
                bool lowest_found = false;

                if (state [temp_r] [temp_c] != -1) {
                    final_offset = state [temp_r] [temp_c];
                    break;
                }

                // cout << "Around [" << temp_r << "," << temp_c << "]" << endl;

                for (int i = 0; i < 4; i++) {
                    int dx;
                    int dy;

                    // NORTH-SOUTH DIRECTIONS ARE REVERSED!!!
                    switch (i) {
                        case 0: // NORTH
                            dx = 0;
                            dy = -1;
                            break;
                        case 1: // WEST
                            dx = -1;
                            dy = 0;
                            break;
                        case 2: // EAST
                            dx = 1;
                            dy = 0;
                            break;
                        case 3: // SOUTH
                            dx = 0;
                            dy = 1;
                            break;
                    }

                    if (temp_r + dy < 0 || temp_r + dy >= height) {
                        continue;
                    }

                    if (temp_c + dx < 0 || temp_c + dx >= width) {
                        continue;
                    }

                    int alt_el = data [temp_r + dy] [temp_c + dx];
                    if (alt_el < temp_el && (!(lowest_found) || alt_el < lowest_el)) {
                       //  cout << "El: " << alt_el << " vs. " << temp_el << endl;
                       // cout << "Lowest El: " << lowest_el << endl;
                       //  cout << "Found? " << (lowest_found ? "true" : "false") << endl;

                        if (!(backtrace.empty())) {
                            int stack_top = backtrace.top();
                            int trial_pos = (temp_r + dy) * 100 + (temp_c + dx);

                            if (stack_top == trial_pos) {
                               // cout << "SKIPPING" << endl;
                                continue;
                            }
                        }
                   
                        lowest_found = true;
                        lowest_el = alt_el;
                        lowest_dx = dx;
                        lowest_dy = dy;
                        // cout << "DUMB";
                    }
                    // cout << "ELSE";
                }

                if (lowest_found) {
                    int current = temp_r * 100 + temp_c;
                    backtrace.push(current);

                    temp_el     = lowest_el;
                    temp_r    = temp_r + lowest_dy;
                    temp_c    = temp_c + lowest_dx;

                    // cout << "[" << temp_r << "," << temp_c << "]" << endl;

                    if (state [temp_r] [temp_c] != -1) {
                        final_r     = temp_r;
                        final_c     = temp_c;
                        final_offset    = state [temp_r] [temp_c];

                        break; 
                    }
                } else {
                    final_r     = temp_r;
                    final_c     = temp_c;

                    if (state [temp_r] [temp_c] == -1) {
                        final_offset    = offset;
                        offset++;
                        state [temp_r] [temp_c] = final_offset;

                        // cout << "Sink: [" << temp_r << "," << temp_c << "] = " << final_offset << endl;
                    } else {
                        final_offset = state [temp_r] [temp_c];
                        // cout << "Hit old path at [" << temp_r << "," << temp_c << "]" <<endl;
                    }
                    break;
                }
            } while (true);

            while (!(backtrace.empty())) {
                int pos = backtrace.top();
                backtrace.pop();

                int final_c = pos % 100;
                int final_r = (pos - final_c) / 100;
                // cout << "[" << final_r << "," << final_c << "] <- " << ('a' + final_offset) << endl;
                state [final_r] [final_c] = final_offset;
            }
        }
    }

    for (int row = 0; row < height; row++) {
        for (int col = 0; col < width; col++) {
            if (col > 0) {
                cout << " ";
            }

            putchar('a' + state[row] [col]);
        }

        cout << endl;
    }
}

int main(int argc, char **argv) {
    int test_cases;
    cin >> test_cases;

    for (int i = 0; i < test_cases; i++) {
        cout << "Case #" << (i + 1) << ":" << endl;
        do_testcase();
    }
}


