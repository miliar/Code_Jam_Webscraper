#include<iostream>
#include<map>
using namespace std;


int main() {

	map<char,char> m;
	m[' '] = ' ';
	m['a'] = 'y';
	m['o'] = 'k';
	m['z'] = 'q';
	m['q'] = 'z';
	
	string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string b = "our language is impossible to understand";
	for (int i=0;i<(int)a.size();i++) {
		if (!m.count(a[i]))
			m[a[i]] = b[i];
	}
	a = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	b = "there are twenty six factorial possibilities";
	for (int i=0;i<(int)a.size();i++) {
		if (!m.count(a[i]))
			m[a[i]] = b[i];
	}

	a = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	b = "so it is okay if you want to just give up";
	for (int i=0;i<(int)a.size();i++) {
		if (!m.count(a[i]))
			m[a[i]] = b[i];
	}

	int N;
	cin >> N;
	string s;
	string *r = new string[N];
	for (int i = 0; i < N; i++)
		r[i] = "";
	for (int i = 0; i < N; i++) {
		cin >> ws;
		getline(cin, s);
		for (int j=0;j<s.size();j++)
			r[i] = r[i]+ m[s[j]];
	}
	for (int i = 0; i < N; i++) 
		cout<<"Case #"<<i+1<<": "<<r[i]<<endl;

}


