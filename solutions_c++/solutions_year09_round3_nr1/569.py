#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

long long pow(int a, int b){
	long long ret=1;
	while (b > 0){
		ret *= a;
		b--;
	}
	return ret;
}

unsigned long long convert(string i, int base){

	unsigned long long ret = 0;
	int len = i.size();
	for (int r = 0; r < len; r++){
		long long n = i[r];
		n *= pow(base, len-r-1);
		ret += n;
	}
	return ret;
};

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int N;
	map<char, int> m;
	cin >> N;
	for (int r = 0; r < N; r++){
		m.clear();
		string s;
		char a[62] = {0};
		cin >> a;
		int len = strlen(a);
		int c = 0;
		for (int p = 0; p < len; p++){
			map<char,int>::iterator iter;
			if ((iter = m.find(a[p])) == m.end()){
				if (c == 0)	m.insert(make_pair(a[p], 1)), s.push_back(1);
				else if (c == 1) m.insert(make_pair(a[p], 0)), s.push_back(0);
				else m.insert(make_pair(a[p], c)), s.push_back(c);
				c++;
			} else s.push_back(iter->second);
		}
		if (c == 1) c++;
		cout << "Case #" << r+1 << ": " << convert(s, c) << endl;
	}
};