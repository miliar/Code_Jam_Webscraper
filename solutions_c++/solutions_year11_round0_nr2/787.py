#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <list>
#include <set>

using namespace std;

typedef map<int, char> comb;
typedef map<int, char>::const_iterator cit;
typedef set<int> pairs;

int key(int a,int b) {
    return 256*a+b;
}

void invoke (char base, list<char> &el, const comb &form, const pairs &opp) {
    //el.push_back(base);
    if (!el.empty()) {
	cit ci = form.find(key(el.back(),base));
	if (ci != form.end()) {
	    el.pop_back();
	    invoke(ci->second,el,form,opp);
	    return;
	}

	for (list<char>::iterator li = el.begin(); li != el.end(); ++li) {
	    if (opp.count(key(*li,base)) > 0) {
		el.clear();
		return;
	    }
	}
    }
    el.push_back(base);
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int C, D, N;
	comb form;
	cin >> C;
	for (int i = 0; i<C; ++i) {
	    string s;
	    cin >> s;
	    form.insert(make_pair(key(s[0],s[1]),s[2]));
	    form.insert(make_pair(key(s[1],s[0]),s[2]));
	}

	pairs opposed;
	cin >> D;
	for (int i = 0; i<D; ++i) {
	    string s;
	    cin >> s;
	    opposed.insert(key(s[0],s[1]));
	    opposed.insert(key(s[1],s[0]));
	}

	string s;
	cin >> N >> s;
	list<char> el;
	for (int i = 0; i<N; ++i) 
	    invoke(s[i],el,form,opposed);

	cout<<"Case #"<<c<<": [";
	bool f = true;
	for (list<char>::iterator li = el.begin(); li != el.end(); ++li) {
	    if (!f) cout<<", ";
	    cout<<*li;
	    f = false;
	}
	cout<<"]"<<endl;
    }

    return 0;
}
