#include <iostream>
#include <iomanip>
#include <set>
#include <vector>
#include <string>

using namespace std;
vector<double> tF(100, -1);

double process(vector<int> * vect);
int realsize(vector<int> * vect);
set<vector<int> *> * find_independant_permutations(vector<int> * vect);
double F(int n);

int main(int argc, char * argv) {

/*
	for (int i = 1; i <= 12; i++) {
		cout << "F(" << i << ") = " << F(i) << endl;
	}	
*/
	int linecount = 0;
	int tabsize = 0;

	cin >> linecount;

	for (int i = 0; i < linecount; i++) {
		cin >> tabsize;
//		int tab[tabsize];
		vector<int> full_vector;
		vector<int>::iterator it;
		
		for (int j = 0; j < tabsize; j++) {
			int r;
			cin >> r;
			full_vector.push_back(r);
		}

		double proba = process(&full_vector);

/*		
		for (it = full_vector.begin(); it != full_vector.end(); it++) {
			cout << *it << " - ";
		}
		cout << endl;
*/
		cout << "Case #" << i+1 << ": " << setiosflags(ios::fixed) << setprecision(6) << proba << endl;
	}

	return 0;
}

void do_combination(vector<int> * vect, vector<int> * tmp, int ind, double * ret, int * useless_perms_count, int * total_count) {
//	cout << "Pouf" << endl;
	int i;
	if (ind >= (vect->size())) {
//		cout << "Blah" << endl;
		set<vector<int> *> * s = find_independant_permutations(tmp);
		if (s->size() == 1) {
			*useless_perms_count += 1;
//			cout << "U : " << *useless_perms_count << endl;
		} else {	
			*ret += 1 + process(new vector<int>(*tmp));
		}
		*total_count += 1;
		return;
	}
	for (i = 0; i < vect->size(); i++) {
//		cout << "Presque inside the boucle (" << i << ")" << endl;
		if (vect->at(i) >= 0) {
//			cout << "Inside the boucle pour de vrai ! (" << i << ")" << endl;
			int pt = vect->at(i);
			vect->at(i) = -1;
			tmp->at(ind) = pt;
			do_combination(vect, tmp, ind+1, ret, useless_perms_count, total_count);
			vect->at(i) = pt;
		}
	}	
//	cout << "Blih ! End of function reached !" << endl;
//	cout << "ind value : " << ind << endl;
}	

/* Return the average number of hits needed to sort an array containing a single permutation.
This is an intrinsec value. The hard part is to compute it.
*/
double F(int n) {
	return n;
	if (n == 1) {
		return 0;
	}	
	if (tF.at(n) != -1) {
		return tF.at(n);
	} else {
		int * useless_perms_count = new int(0);
		int * total_count = new int(0);
		double * r = new double(0);
		vector<int> * vect = new vector<int>(n);
		for (int i = 0; i < n; i++) {
			vect->at(i) = i+1;
		}	
		do_combination(vect, new vector<int>(vect->size(), -1), 0, r, useless_perms_count, total_count);
		cout << "F(" << n << ") -> U: " << *useless_perms_count << " T: " << *total_count << " r: " << *r << endl;
		if (*useless_perms_count != 0) {
			tF.at(n) = ( (*r / *useless_perms_count) + 1) / ( (*total_count/ *useless_perms_count) - 1);
		} else {
			tF.at(n) = (*r / *total_count);
		}	
		cout << " -> " << tF.at(n) << endl;
		return tF.at(n);
	}	
}

set<vector<int> *> * find_independant_permutations(vector<int> * vect) {
	set<int> processed_elts;
	set<vector<int> *> * ret = new set<vector<int> *>;

	for (int i = 0; i < vect->size(); i++) {
		if (vect->at(i) != -1 && processed_elts.find(i) == processed_elts.end()) {
			// We start a chain from this element which was never seen before.
			vector<int> * t = new vector<int>(vect->size(),-1);
//			cout << "Created new t. Start index : " << i << ", size : " << vect->size() << endl;
			ret->insert(t);

			//We copy the values from vect to t as we encounter them
			t->at(i) = vect->at(i);
			processed_elts.insert(i);
			for (int k = vect->at(i)-1; processed_elts.find(k) == processed_elts.end(); k = vect->at(k)-1) {
//				cout << "Access to " << k << endl;
				if (vect->at(k) == -1) {
//					cout << "Fail ! Access to a non-existent value. Chain is broken." << endl;
				}	
				t->at(k) = vect->at(k);
				processed_elts.insert(k);
			}

			// Then, we purge the vector for (-1) values
			// Note. No. Ignoring them instead makes us able to still find permutations.
			vector<int>::iterator it;
			/*
			for (it = t->begin(); it != t->end();) {
				if (*it == -1) {
					it = t->erase(it);
				} else {
					it++;
				}	
				
			}
*/
/*			// Some debug printing
			cout << "In the end, the vector contains : ";
			for (it = t->begin(); it != t->end(); it++) {
				cout << *it << ",";
			}
			cout << endl;
*/		}
	}

	return ret;
}	

int realsize(vector<int> * vect) {
	int ret = 0;
	for(vector<int>::iterator it = vect->begin(); it != vect->end(); it++) {
		if (*it != -1) {
			ret++;
		}
	}
	return ret;
}	

double process(vector<int> * vect) {

	if (realsize(vect) == 1) {
		return 0; // A 1-element array is already sorted
	}	

	set<vector<int> *> * subvects_set = find_independant_permutations(vect);

	if (subvects_set->size() == 1) {
		return F(realsize(vect));
	} else {
		int k = 0;
		set<vector<int> *>::iterator it;
		for (it = subvects_set->begin(); it != subvects_set->end(); it++) {
			k += process(*it);
		}
		return k;
	}	
}

