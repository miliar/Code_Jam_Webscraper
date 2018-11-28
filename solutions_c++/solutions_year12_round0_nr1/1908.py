#include <cstdio>
using namespace std;
#include <iostream>
#include <map>
#include <cmath>

//By chyx111
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define forI(it,v) for(__typeof__((v).begin()) it = (v).begin(); it != (v).end(); ++it)

template<class S, class T> ostream& operator<<(ostream& os, pair<S, T> p){
	return os << "(" << p.first << ", " << p.second << ")";
};
char *encoded = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char *decoded = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char strtmp[1024];
int main() {
	map<char, char> to_ori;
	for(int i = 0; encoded[i]; ++i){
		to_ori[encoded[i]] = decoded[i];
	}
	//forI(it, to_ori){
	//	cout << *it << endl;
	//}
	to_ori['q'] = 'z';
	to_ori['z'] = 'q';

	int ca;
	scanf("%d", &ca);
		gets(strtmp);
	Rep(ica, ca){
		gets(strtmp);
		for(int i = 0; strtmp[i]; ++i){
			strtmp[i] = to_ori[strtmp[i]];
		}
		printf("Case #%d: %s\n", ica + 1, strtmp);
	}
	return 0;
}

