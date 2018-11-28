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
int k, minimal;
string line;
int perm[20], used[20];
void permu(int s) {
    if (s == k) {
        int value = 0;
        string line2 = line;
	for (int x = 0; x < line.size(); x++) {
	    line2[x] = line[perm[x%k] + (x - x%k)];
	    if (x && line2[x] != line2[x-1]) value++;
	}
	minimal = min(minimal, value + 1);
	return;
    }
    for (int x = 0; x < k; x++) {
        if (!used[x]) {
	    used[x] = 1;
	    perm[s] = x;
	    permu(s+1);
	    used[x] = 0;
	}
    }
}
void _case(int i) {
    read1(k);
    line = readline();
    for (int x = 0; x < 20; x++) used[x] = 0;
    minimal = line.size() + 10;
    permu(0);
    cout << "Case #" << i << ": " << minimal << endl;
}
int main() {
    int n, i = 1;
    read1(n);
    while (n--) _case(i++);
    return 0;
}

