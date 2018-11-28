#include <iostream>
#include <iomanip>
#include <set>
#include <vector>
#include <string>

using namespace std;

int process(vector<int> * vect);

int main(int argc, char * argv) {

	int linecount = 0;
	int tabsize = 0;

	cin >> linecount;

	for (int i = 0; i < linecount; i++) {
		cin >> tabsize;
		vector<int> full_vector;
		vector<int>::iterator it;
		
		for (int j = 0; j < tabsize; j++) {
			int r;
			cin >> r;
			full_vector.push_back(r);
		}

		int res = process(&full_vector);

/*
		for (it = full_vector.begin(); it != full_vector.end(); it++) {
			cout << *it << " - ";
		}
		cout << endl;
*/

		cout << "Case #" << i+1 << ": ";
		if (res == -1) {
			cout << "NO";
		} else {
			cout << res;
		}
		cout << endl;
	}

	return 0;
}

int add(int a, int b) {

//	cout << "add(" << a << "," << b << ") = ";

	int ret = 0;
	int k = 1;

	while(a != 0 || b != 0) {
//		cout << a % 2 << " " << b % 2 << endl;
		ret += k * (((a % 2) + (b % 2)) % 2);
		a /= 2;
		b /= 2;
		k *= 2;
	}	
//	cout << ret << endl;
	return ret;
}

int count(vector<int> * v1, vector<int> * v2) {

	if (v1->size() == 0 || v2->size() == 0) {
		return -1;
	}	

	int c1 = 0;
	int tc1 = 0;
	int c2 = 0;
	int tc2 = 0;

	for(vector<int>::iterator it = v1->begin(); it != v1->end(); it++) {
		c1 = add(c1, *it);
		tc1 = tc1 + *it;
	}

	for(vector<int>::iterator it = v2->begin(); it != v2->end(); it++) {
		c2 = add(c2, *it);
		tc2 = tc2 + *it;
	}

//	cout << "c1 : " << c1 << " c2 : " << c2 << " tc1 : " << tc1 << " tc2 : " << tc2 << endl;

	if (c1 == c2) {
		return max(tc1,tc2);
	} else {
		return -1;
	}
}	

int process_rec(vector<int> * v, vector<int> v1, vector<int> v2, int k) {

/*
	vector<int>::iterator it;

	cout << "v1 : ";
	for (it = v1.begin(); it != v1.end(); it++) {
		cout << *it << " - ";
	}
	cout << endl;

	cout << "v2 : ";
	for (it = v2.begin(); it != v2.end(); it++) {
		cout << *it << " - ";
	}
	cout << endl;
*/

	if (k == v->size()) {
		return count(&v1, &v2);
	} else {	
		int r = -1;
		v1.push_back(v->at(k));
		r = process_rec(v, v1, v2, k+1);
		v1.pop_back();
		v2.push_back(v->at(k));
		r = max(r, process_rec(v, v1, v2, k+1));
		
		return r;
	}
}	

int process(vector<int> * vect) {
	int ret = -1;

	vector<int> * v1 = new vector<int>;
	vector<int> * v2 = new vector<int>;

	ret = process_rec(vect, *v1, *v2, 0);

	return ret;
}

