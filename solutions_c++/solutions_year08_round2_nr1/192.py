#include <map>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
void trim(string &s) {
     s = s.erase(s.find_last_not_of("\r\n") + 1);
     s = s.erase(0, s.find_first_not_of("\r\n"));
}
string readline() {
    string line;
    getline(cin, line); trim(line);
    return line;
}
void read1(int &a) {
    string l = readline();
    sscanf(l.c_str(), "%d", &a);
}
void read2(int &a, int &b) {
    string l = readline();
    sscanf(l.c_str(), "%d %d", &a, &b);
}
void _case(int i) {
    int n;
    long long int A, B, C, D, x0, y0, M;
    long long int X, Y;
    long long int q[3][3];
    for (int x = 0; x < 3; x++) 
        for (int y = 0; y < 3; y++) q[x][y] = 0;

    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    X = x0; Y = y0;
    q[X%3][Y%3]++;
    for (int x = 1; x < n; x++) {
        X = (A * X + B) % M;
	Y = (C * Y + D) % M;
        q[X%3][Y%3]++;
    }
    long long int qq = 0;
    for (int x = 0; x < 3; x++) {
        qq += q[x][0] * q[x][1] * q[x][2];
    }
    for (int x = 0; x < 3; x++) {
        qq += q[0][x] * q[1][x] * q[2][x];
    }
    for (int x = 0; x < 3; x++) {
        for (int y = 0; y < 3; y++) {
            qq += (q[x][y] * (q[x][y] - 1) * (q[x][y] - 2)) / 6;
        }
    }
    qq += q[0][0] * q[1][1] * q[2][2] +
	  q[0][0] * q[1][2] * q[2][1] +
	  q[0][1] * q[1][0] * q[2][2] +
	  q[0][1] * q[1][2] * q[2][0] +
	  q[0][2] * q[1][0] * q[2][1] +
	  q[0][2] * q[1][1] * q[2][0];
    cout << "Case #" << i << ": " << qq << endl;
}
int main() {
    int n, i = 1;
    cin >> n;
    while (n--) _case(i++);
    return 0;
}

