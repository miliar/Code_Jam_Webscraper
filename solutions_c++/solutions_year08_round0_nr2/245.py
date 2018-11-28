/* kanekoB.cc
 */
#include <iostream>
#include <string>
#include <cassert>
#include <deque>
#include <algorithm>
using namespace std;
int T, Turn, NA, NB;
int depa[100], depb[100], arra[100], arrb[100];
int parse(const string& t)
{
    assert(t[2] == ':');
    return ((t[0]-'0')*10+t[1]-'0')*60+(t[3]-'0')*10+t[4]-'0';
}
int count(int ND, const int *dep, int NA, const int *arr)
{
    typedef deque<int> queue_t;
    queue_t Q;
    for (int i=0; i<NA; ++i) Q.push_back(arr[i]+Turn);
    int sum = 0;
    for (int i=0; i<ND; ++i) {
	if (! Q.empty() && Q[0] <= dep[i]) {
	    Q.pop_front();
	    continue;
	}
	++sum;
    }
    return sum;
}
int main()
{
    cin >> T;
    for (int t=0; t<T; ++t) {
	cin >> Turn >> NA >> NB;
	string dep, arr;
	for (int i=0; i<NA; ++i) {
	    cin >> dep >> arr;
	    depa[i] = parse(dep);
	    arrb[i] = parse(arr);
	}
	for (int i=0; i<NB; ++i) {
	    cin >> dep >> arr;
	    depb[i] = parse(dep);
	    arra[i] = parse(arr);
	}
	sort(depa, depa+NA);
	sort(arrb, arrb+NA);
	sort(depb, depb+NB);
	sort(arra, arra+NB);
	cout << "Case #" << t+1 << ": "
	     << count(NA, depa, NB, arra)
	     << " " << count(NB, depb, NA, arrb) << endl;
    }
}
