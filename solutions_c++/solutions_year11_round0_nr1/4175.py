#include <iostream>
#include <fstream>

const int MAX_T = 100;
const int MAX_N = 100;

using namespace std;

int main(int argc, char** argv)
{
    int T = 0; // Test cases
    int N = 0; // Steps in ith case

    int *buttons_O = new int[MAX_N];
    int *buttons_B = new int[MAX_N];

    fstream input("A-large.in");
    ofstream output;
    output.open("A-large.out", ios_base::out);


    char* seq;
    int seq_it = 0;
    input >> T;
    for (int i=0; i<T; i++) {
        input >> N;

        seq = new char[N];
        seq_it = 0;

        int num_O = 0, num_B = 0;
        int buttons_O_it = 0, buttons_B_it = 0;
        for (int j=0; j<N; j++) {
            char c;
            int k;
            input >> c;
            input >> k;

            if (c == 'B') {
                buttons_B[buttons_B_it++] = k;
                num_B++;
            }
            if (c == 'O') {
                buttons_O[buttons_O_it++] = k;
                num_O++;
            }
            seq[seq_it++] = c;
        }

        for (int j=num_B; j<MAX_N; j++) {
            buttons_B[j] = -1;
        }
        for (int j=num_O; j<MAX_N; j++) {
            buttons_O[j] = -1;
        }
        buttons_O_it = 1;
        buttons_B_it = 1;

        int elapsed = 0;
        int pressed_O = 0, pressed_B = 0;

        seq_it = 0;
        do {
            bool pressed = false;
            elapsed++;
            if (buttons_B_it == buttons_B[pressed_B]) {
                if (seq[seq_it] == 'B') {
                    pressed_B++;
                    pressed = true;
                }
            } else {
                if (buttons_B[pressed_B] != -1) {
                    if (buttons_B[pressed_B] > buttons_B_it) {
                        buttons_B_it++;
                    } else if (buttons_B[pressed_B] < buttons_B_it) {
                        buttons_B_it--;
                    }
                }
            }
            if (buttons_O_it == buttons_O[pressed_O]) {
                if (seq[seq_it] == 'O') {
                    pressed_O++;
                    pressed = true;
                }
            } else {
                if (buttons_O[pressed_O] != -1) {
                    if (buttons_O[pressed_O] > buttons_O_it) {
                        buttons_O_it++;
                    } else if (buttons_O[pressed_O] < buttons_O_it) {
                        buttons_O_it--;
                    }
                }
            }
            if (pressed == true) {
                seq_it++;
            }
        } while(pressed_B + pressed_O < N);

//        cout << "Case #" << i+1 << ": " << elapsed << endl;
        output << "Case #" << i+1 << ": " << elapsed << endl;
        delete [] seq;
    }
    output.close();
    input.close();

    return 0;
}
