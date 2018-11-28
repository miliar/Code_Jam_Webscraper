#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>


using namespace std;

int main()
{
	ifstream ifs("B-small-attempt2.in");
	ofstream ofs("B-small-attempt2.out");

	int t, n, m, p, i, j, k;
	vector<int> v1, v2;
	vector<int>::iterator it;
	bool solved;

	ifs >> t;
	ifs.ignore();
	for(i = 1; i <= t; i++){
		ifs >> n;
		ifs.ignore();

		v1.clear();
		while(n != 0){
			v1.push_back(n % 10);
			n /= 10;
		}

		solved = false;
		m = v1.at(0);
		for(j = 1; j < v1.size(); j++){
			if(m > v1.at(j)){
				v2.clear();
				v2.assign(v1.begin(), v1.begin() + j);
				sort(v2.begin(), v2.end());
				for(k = 0; k < j; k++){
					if(v2.at(k) > v1.at(j)){
						break;
					}
				}
				n = v2.at(k);
				for(k = 0; k < j; k++){
					if(v1.at(k) == n){
						break;
					}

				}
				swap(v1.at(j), v1.at(k));
				sort(v1.begin(), v1.begin() + j, greater<int>());
				solved = true;
				break;
			} else {
				m = v1.at(j);
			}
		}
		if(!solved){
			sort(v1.begin(), v1.end(), greater<int>());
			if(v1.at(v1.size() - 1) == 0){
				for(j = v1.size() - 2; j >= 0; j--){
					if(v1.at(j) != 0){
						swap(v1.at(j), v1.at(v1.size() - 1));
						break;
					}
				}
			}
			v1.insert(v1.end() - 1, 0);
		}
		ofs << "Case #" << i << ": ";
		for(j = v1.size() - 1; j >= 0; j--){
			ofs << v1.at(j);
		}
		ofs << endl;
	}

	return 0;
}