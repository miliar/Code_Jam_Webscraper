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
    long long int N, M, A;
    cin >> N >> M >> A;
    long long int x1 = 0, y1 = 0, x2, y2, x3, y3;
    for (x2 = 0; x2 <= N; x2++) {
        for (y2 = 0; y2 <= M; y2++) {
	    for (x3 = 0; x3 <= N; x3++) {
	        for (y3 = 0; y3 <= M; y3++) {
                    long long int area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
                    if (area == A || area == -A) {
                        cout << "Case #" << i << ": " << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
			return;
		    }
		}
	    }
	}
    }
    cout << "Case #" << i << ": IMPOSSIBLE" << endl;
}
int main() {
    int n, i = 1;
    cin >> n;
    while (n--) _case(i++);
    return 0;
}

