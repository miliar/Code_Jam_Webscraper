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
void solveit(int D, vector<int> &i) {
    int pos = 0;
    vector<int> perfect(D, 0);
    for (int x = 0; x < perfect.size(); x++) perfect[x] = 0;
    for (int x = 1; x <= D; x++) {
        int zz = x;
	while (perfect[pos] || zz) {
	    if (perfect[pos] == 0) {
	        if (--zz == 0) break;
	    }
	    pos++; pos %= D;
	}
	while (perfect[pos]) { pos++; pos %= D; }
	perfect[pos++] = x;
	pos %= D;
    }
    for (int x = 0; x < i.size(); x++) i[x] = perfect[i[x] - 1];
}
void _case(int i) {
    int D, ask, temp;
    vector<int> ind;
    cin >> D >> ask;
    for (int x = 0; x < ask; x++) {
        cin >> temp;
	ind.push_back(temp);
    }
    solveit(D, ind);
    cout << "Case #" << i << ":";
    for (int x = 0; x < ind.size(); x++) {
        cout << " " << ind[x];
    }
    cout << endl;
}
int main() {
    int n, i = 1;
    cin >> n;
    while (n--) _case(i++);
    return 0;
}

