#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for(int c = 1; c <= cases; c++) {
        int o_pos = 1, b_pos = 1;
        int o_time = 0, b_time = 0;
        
        int data_count;
        cin >> data_count;

        for(int i = 0; i < data_count; i++) {
            char color;
            int pos;
            cin >> color >> pos;

            switch(color) {
                case 'O':
                    o_time += abs(pos - o_pos); // move
                    o_pos = pos;
                    if(o_time < b_time) o_time = b_time; // wait
                    o_time++; // push
                    break;
                case 'B':
                    b_time += abs(pos - b_pos); // move
                    b_pos = pos;
                    if(b_time < o_time) b_time = o_time; // wait
                    b_time++; // push
                    break;
            }
        }

        int result = max(o_time, b_time);
        cout << "Case #" << c << ": " << result << endl;
    }
    return 0;
}
