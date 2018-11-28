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
void readTimes(int &a, int &b) {
    string l = readline();
    int h0, m0, h1, m1;
    sscanf(l.c_str(), "%d:%d %d:%d", &h0, &m0, &h1, &m1);
    a = h0 * 60 + m0;
    b = h1 * 60 + m1;
}
void recEraser(vector< pair<int, int> > &tai, vector< pair<int, int> > &tbi, int from, int side) {
    int tmp = -1;
    if (!side) {
       for (int x = 0; x < tbi.size(); x++) {
           if (tbi[x].first >= from) {
	       tmp = tbi[x].second;
	       tbi.erase(tbi.begin() + x);
	       break;
	   }
       }
       if (tmp > 0)
           recEraser(tai, tbi, tmp, !side);
    } else {
       for (int x = 0; x < tai.size(); x++) {
           if (tai[x].first >= from) {
	       tmp = tai[x].second;
	       tai.erase(tai.begin() + x);
               break;
           }
       }
       if (tmp > 0) 
           recEraser(tai, tbi, tmp, !side);
    }
}
pair<int, int> scase(vector< pair<int, int> > &tai, vector< pair<int, int> > &tbi) {
    pair<int, int> res;
    res.first = res.second = 0;
    sort(tai.begin(), tai.end());
    sort(tbi.begin(), tbi.end());
    while (tai.size() && tbi.size()) {
        if (tai[0].first < tbi[0].first) {
	    int tmp = tai[0].second;
	    tai.erase(tai.begin());
	    recEraser(tai, tbi, tmp, 0);
	    res.first ++;
	} else {
	    int tmp = tbi[0].second;
	    tbi.erase(tbi.begin());
	    recEraser(tai, tbi, tmp, 1);
	    res.second ++;
	}
    }
    res.first += (int)tai.size();
    res.second += (int)tbi.size();
    return res;
}
void _case(int i) {
    vector< pair<int, int> > tai, tbi;
    cout << "Case #" << i << ": ";
    int turn, ta, tb, hs, he;
    read1(turn); read2(ta, tb);
    for (int x = 0; x < ta; x++) {
        readTimes(hs, he); he += turn;
	tai.push_back(make_pair(hs, he));
    }
    for (int x = 0; x < tb; x++) {
        readTimes(hs, he); he += turn;
	tbi.push_back(make_pair(hs, he));
    }
    pair<int, int> r = scase(tai, tbi);
    cout << r.first << " " << r.second << endl;
}
int main() {
    int n, i = 1;
    read1(n);
    while (n--) _case(i++);
    return 0;
}

