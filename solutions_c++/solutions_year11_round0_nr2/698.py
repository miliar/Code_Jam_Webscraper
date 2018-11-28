#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>

using namespace std;

const char *input_file = "B-large-0.in";
const char *output_file = "B-large-0.out";

typedef map<pair<char, char>, char> CompMap;
typedef map<char, set<char> > OppMap;

pair<char, char> pairUp(char a, char b) {
    return make_pair(min(a, b), max(a, b));
}

void insertComposition(CompMap &comp, char a, char b, char c) {
    comp.insert(make_pair(pairUp(a, b), c));
}

void insertOpposition(OppMap &oppMap, char a, char b) {
    oppMap[a].insert(b);
    oppMap[b].insert(a);
}

void compose(vector<char> &list, CompMap &comp) {
    if (list.size() < 2)
	return;

    char a = list[list.size() - 1];
    char b = list[list.size() - 2];

    if (comp.count(pairUp(a, b)) > 0) {
	list.pop_back();
	list.pop_back();
	list.push_back(comp[pairUp(a, b)]);
    }
}

void oppose(vector<char> &list, const OppMap &oppMap) {
    if (list.size() < 1 || oppMap.count(list.back()) == 0)
	return;
    const set<char> &opp = oppMap.find(list.back())->second;
    for (int i = 0; i < list.size() - 1; ++i)
	if (opp.count(list[i]) > 0) {
	    list.clear();
	    break;
	}
}

CompMap readCompositions(istream &in) {
    int c;
    CompMap comp;

    in >> c;
    for (int i = 0; i < c; ++i) {
	string s;
	in >> s;
	insertComposition(comp, s[0], s[1], s[2]);
    }

    return comp;
}

OppMap readOppositions(istream &in) {
    int d;
    OppMap oppMap;

    in >> d;
    for (int i = 0; i < d; ++i) {
	string s;
	in >> s;
	insertOpposition(oppMap, s[0], s[1]);
    }

    return oppMap;
}

void writeList(const vector<char> &list, ostream &out) {
    out << "[";
    for (int i = 0; i < list.size(); ++i)
	out << list[i] << (i + 1 == list.size() ? "" : ", ");
    out << "]" << endl;
}

void solveCase(int case_num, istream &in, ostream &out) {
    CompMap compMap(readCompositions(in));
    OppMap oppMap(readOppositions(in));

    int n;
    string input;
    vector<char> list;
    
    in >> n >> input;
    for (int i = 0; i < n; ++i) {
	list.push_back(input[i]);
	compose(list, compMap);
	oppose(list, oppMap);
    }

    out << "Case #" << case_num << ": ";
    writeList(list, out);
}

int main() {
    ifstream in(input_file);
    ofstream out(output_file);

    int t;
    in >> t;
    for (int i = 1; i <= t; ++i)
	solveCase(i, in, out);

    in.close();
    out.close();

    return EXIT_SUCCESS;
}

