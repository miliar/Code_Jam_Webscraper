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
int isprime(long long int a) {
    if (a%2 == 0) return a == 2;
    if (a < 3) return 0;
    for (long long int i = 3; i * i <= a; i += 2) if (a%i == 0) return 0;
    return 1;
}
void _case(int i) {
    map<long long int, long long int> xxx;
    map<long long int, long long int> groups;
    long long int A, B, P;
    cin >> A >> B >> P;
    long long int cant = B - A + 1;
    for (int x = A, z = 0; x <= B; x++, z++) groups[x] = -1;

    for (long long int x = P; x < B-A+1; x++) {
        for (long long int y = A; y <= B; y++) {
	    if (isprime(x) && y % x == 0) {
	        if (groups[y] == -1) {
		    groups[y] = x;
		} else {
		    long long int temp = groups[y];
		    for (long long int z = A; z <= B; z++) {
		        if (groups[z] == temp) {
			    groups[z] = x;
			}
		    }
		}
	    }
	}
    }
    for (long long int z = A; z <= B; z++) {
        if (groups[z] > -1) {
            xxx[groups[z]]++;
	}
    }
    for (typeof(xxx.begin()) x = xxx.begin(); x != xxx.end(); x++) {
        if (x->second-- > 1) cant -= x->second;
    }
    cout << "Case #" << i << ": " << cant << endl;
}
int main() {
    int n, i = 1;
    cin >> n;
    while (n--) _case(i++);
    return 0;
}

