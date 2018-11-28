#include <iostream>
#include <set>
#include <vector>
using namespace std;
typedef pair<int, int> PII;
int go(multiset<int> s1, vector<int> s2)
{
	for (int i=0; i<s2.size(); ++i) {
		set<int>::iterator it1=s1.lower_bound(s2[i]);
		if (it1!=s1.end()) s1.erase(it1);
	}
	return s1.size();
}
int main()
{
	int t, na, nb, slp;
	PII a[100], b[100];
	int h1, h2, m1, m2;
	scanf("%d", &t);
	for (int icase=1; icase<=t; ++icase) {
		scanf("%d%d%d", &slp, &na, &nb);
		for (int i=0; i<na; ++i) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a[i]=PII(h1*60+m1, h2*60+m2);
		}
		for (int i=0; i<nb; ++i) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			b[i]=PII(h1*60+m1, h2*60+m2);
		}
		printf("Case #%d:", icase);
		multiset<int> s1;
		vector<int> s2;
		for (int i=0; i<na; ++i) s1.insert(a[i].first);
		for (int i=0; i<nb; ++i) s2.push_back(b[i].second+slp);
		sort(s2.begin(), s2.end());
		printf(" %d", go(s1, s2));
		s1.clear(); s2.clear();
		for (int i=0; i<nb; ++i) s1.insert(b[i].first);
		for (int i=0; i<na; ++i) s2.push_back(a[i].second+slp);
		sort(s2.begin(), s2.end());
		printf(" %d", go(s1, s2));
		printf("\n");
	}
}
