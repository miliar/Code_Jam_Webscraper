#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int pass;

struct pt {
    int sp;
    int nsp;
};

struct pt mx(int tot)
{
    pt r;
    if (tot == 0 || tot == 1) {
	r.sp = -1;
	r.nsp = tot;
	return r;
    }
    if (tot == 30 || tot == 29) {
	r.sp = -1;
	r.nsp = 10;
	return r;
    }

    switch (tot % 3) {
	case 0:
	    r.sp = tot / 3 + 1;
	    r.nsp = tot / 3;
	    break;
	case 1:
	    r.sp = r.nsp = tot / 3 + 1;
	    break;
	case 2:
	    r.sp = tot / 3 + 2;
	    r.nsp = tot / 3 + 1;
	    break;
    }

    return r;
}

bool cmp(const pt &a, const pt &b)
{
    if (a.sp >= pass && a.nsp < pass && !(b.sp >= pass && b.nsp < pass))
	return 1;
    if (a.sp >= pass && a.nsp >= pass && !(b.sp >= pass && b.nsp >= pass))
	return 1;
    if (a.nsp >= pass && b.nsp < pass)
	return 1;
    return b.nsp < a.nsp;
}

int main(void)
{
    vector<pt> v;
    int num, surp;
    int kiss, i, j;
    int input;
    int goog;
    for (cin >> kiss, i = 1; i <= kiss; ++i) {
	cin >> num >> surp >> pass;
	for (j = 0; j < num; ++j) {
	    cin >> input;
	    v.push_back(mx(input));
	}
	sort(v.begin(), v.end(), cmp);
	for (j = 0, goog = 0; j < v.size(); ++j) {
	    if (v[j].sp >= pass && surp > 0) {
		goog++;
		surp--;
	    } else if (v[j].nsp >= pass) {
		goog++;
	    }
	}
	cout << "Case #" << i << ": " << goog << endl;
	v.clear();
    }
    return 0;
}
