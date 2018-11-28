#include <iostream>
#include <vector>
#include <limits>
#include <iterator>
using namespace std;

int get_min_prod(vector<int> &v1, vector<int> &v2) {
    if (v1.size() == 1) {
	return v1[0] * v2[0];
    }
    else {
	int min_prod(numeric_limits<int>::max());
	for (size_t i = 0 ; i < v1.size() ; ++i) {
	    vector<int> v1c = v1;
	    vector<int> v2c = v2;
	    v1c.erase(v1c.begin());
	    v2c.erase(v2c.begin() + i);

	    int this_prod = v1[0] * v2[i] + get_min_prod(v1c, v2c);

	    if (this_prod < min_prod) {
		min_prod = this_prod;
	    }
	}

	return min_prod;
    }
}

int main(int argc, char *argv[])
{
    int num_cases;

    cin >> num_cases;

    for (int cse = 0 ; cse < num_cases ; ++cse) {
	int n;

	cin >> n;

	vector<int> v1;
	vector<int> v2;

	for (int i = 0 ; i < n ; ++i) {
	    int m;
	    cin >> m;

	    v1.push_back(m);
	}

	for (int i = 0 ; i < n ; ++i) {
	    int m;
	    cin >> m;

	    
	    v2.push_back(m);
	}

	int min_scalar = get_min_prod(v1, v2);

	cout << "Case #" << (cse + 1) << ": " << min_scalar << endl;
    }

    return 0;
}
