#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <stack>
#include <cmath>

using namespace std;

#define MAX 30

void init(char a[MAX][MAX]) {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            a[i][j] = 'a';
        }
    }
}

void init(int a[MAX][MAX]) {
    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            a[i][j] = 0;
        }
    }
}

void init1d(int a[MAX]) {
    for (int i = 0; i < MAX; i++) {
        a[i] = 0;
    }
}

int check(stack<char> temp, char a) {
    char temp1;
    while (!temp.empty()) {
        temp1 = temp.top();
        if (temp1 == a) return 1;
        else temp.pop();
    }
    return 0;
}

void print(stack<char> &final){
    char here=final.top();
    final.pop();    
    if (final.empty()) {cout<<here;return;}
    print(final);
    cout<<", "<<here;
}

void myclear(stack<char> &a) {
    while (!a.empty()) {
        a.pop();
    }
    return;
}

int main() {
    int T, C, D, N;
    char invoke[MAX][MAX];
    int oppose[MAX][MAX];
    stack<char> result;
    int present[MAX];
    char last;
    char a, b, c, temp;
    bool cleared;
    cin>>T;
    for (int i = 0; i < T; i++) {
        init1d(present);
        cin >> C;
        init(invoke);
        for (int j = 0; j < C; j++) {
            cin >> a >> b >> c;
            invoke[a - 'A'][b - 'A'] = c;
            invoke[b - 'A'][a - 'A'] = c;
        }
        cin >> D;        
        init(oppose);
        for (int j = 0; j < D; j++) {
            cin >> a >> b;
            oppose[a - 'A'][b - 'A'] = 1;
            oppose[b - 'A'][a - 'A'] = 1;
        }
        cin>>N;
        for (int j = 0; j < N; j++) {
            cin >> a;            
            if (result.empty()) {
                result.push(a);
                present[a - 'A'] = 1;
            } else {
                last = result.top();
                if (invoke[last - 'A'][a - 'A'] != 'a') {
                    result.pop();
                    present[last - 'A'] = check(result, last);
                    result.push(invoke[last - 'A'][a - 'A']);
                } else {
                    for (int m = 0; m < MAX; m++) {
                        if (oppose[a - 'A'][m] == 1 && present[m] == 1) {
                            myclear(result);
                            init1d(present);
                            cleared = true;
                            break;
                        }
                        cleared = false;
                    }
                    if (!cleared) {
                        result.push(a);
                        present[a - 'A'] = 1;
                    }
                }
            }
        }
        cout << "Case #" << i + 1 << ": [";
        if (!result.empty()) print(result);
        cout<<"]"<<endl;
    }
    return 0;
}