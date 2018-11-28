#include <iostream>

using namespace std;

typedef struct btn_instruction_t {
    int pos;
    int label; // Convention: 0 is orange, 1 is blue
} BTN_INSTRUCTION;

int main()
{
    int t, n;
    BTN_INSTRUCTION btn_instr[101];
    int next_btn_idx[2],
        cur_pos[2],
        cur_btn_idx;
    int elapsed;
    char label;
    bool button_pushed;

    cin >> t;
    for (int c = 1; c <= t; c++) {
        // init vars
        cur_pos[0] = cur_pos[1] = 1;
        next_btn_idx[0] = next_btn_idx[1] = -1;
        cur_btn_idx = 0;

        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> label >> btn_instr[i].pos;
            btn_instr[i].label = (label == 'O' ? 0 : 1);
            if (next_btn_idx[btn_instr[i].label] == -1) {
                next_btn_idx[btn_instr[i].label] = i;
            }
        }

        for (elapsed = 0; cur_btn_idx < n; elapsed++) {
            button_pushed = false;
            for (int r = 0; r <= 1; r++) {
                if (cur_btn_idx < n && cur_btn_idx == next_btn_idx[r]
                    && cur_pos[r] == btn_instr[cur_btn_idx].pos) {
                    // push button and update next
                    button_pushed = true;
                    for (int i = cur_btn_idx + 1; i < n; i++) {
                        if (btn_instr[i].label == r) {
                            next_btn_idx[r] = i;
                            break;
                        }
                    }
                } else if (cur_pos[r] < btn_instr[next_btn_idx[r]].pos) {
                    ++cur_pos[r];
                } else if (cur_pos[r] > btn_instr[next_btn_idx[r]].pos) {
                    --cur_pos[r];
                }
            }
            if (button_pushed) {
                cur_btn_idx++;
            }
        }
        cout << "Case #" << c << ": " << elapsed << endl;
    }
}
