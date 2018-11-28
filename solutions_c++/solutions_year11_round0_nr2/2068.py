#include <iostream>
using namespace std;

int combine[26][26];
bool opposed[26][26];

void init() {
    for(int i = 0; i < 26; i++) {
        for(int j = 0; j < 26; j++) {
            combine[i][j] = -1;
            opposed[i][j] = false;
        }
    }
}

void read_combine() {
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        char elem_x, elem_y, elem_z;
        cin >> elem_x >> elem_y >> elem_z;

        int x = elem_x - 'A', y = elem_y - 'A', z = elem_z - 'A';
        combine[x][y] = combine[y][x] = z;
    }
}

void read_opposed() {
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        char elem_x, elem_y;
        cin >> elem_x >> elem_y;

        int x = elem_x - 'A', y = elem_y - 'A';
        opposed[x][y] = opposed[y][x] = true;
    }
}

int main() {
    int cases;
    cin >> cases;
    for(int c = 1; c <= cases; c++) {
        init();
        read_combine();
        read_opposed();

        int list[100];
        int list_len = 0;

        int n;
        cin >> n;
        for(int i = 0; i < n; i++) {
            char elem_next;
            cin >> elem_next;
            int next = elem_next - 'A';

            if(list_len == 0) {
                list[list_len++] = next;
            } else {
                int& top = list[list_len - 1];

                if(combine[top][next] != -1) {
                    top = combine[top][next];
                } else {
                    for(int j = 0; j < list_len; j++) {
                        if(opposed[list[j]][next]) {
                            list_len = 0;
                            break;
                        }
                    }

                    if(list_len > 0) {
                        list[list_len++] = next;
                    }
                }
            }
        }

        cout << "Case #" << c << ": " << "[";
        for(int i = 0; i < list_len; i++) {
            cout << (char) (list[i] + 'A');
            if(i < list_len - 1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    return 0;
}
