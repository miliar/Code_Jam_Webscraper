#include <iostream>
#include <vector>
#include <map>

using namespace std;

map<int, double> owp;

double get_owp(vector<vector<int> > &v, int index, int N) {
    double total = 0.0;
    int mennyi = 0;

    for(int i = 0; i < N; i++) {
	if(i == index)
	    continue;
	if(v.at(index).at(i) != -1) {
	    double won = 0.0;
	    double played = 0.0;
	    for(int j = 0; j < N; j++) {
		if(j == index)
		    continue;

		if(v.at(i).at(j) == 1) {
		    played += 1.0;
		    won += 1.0;
		} else if(v.at(i).at(j) == 0)
		    played += 1.0;
	    }
	    total += won/played;
	    mennyi++;
	}
    }
    owp[index] = total/mennyi;
//    cout << "owp[" << index << "]: " << owp[index] << endl;
    return owp[index];
}


double get_oowp(vector<vector<int> > &v, int index, int N) {
    double owps = 0.0;
    int mennyi = 0;

    for(int i = 0; i < N; i++) {
	if(i == index)
	    continue;
	if(v.at(index).at(i) != -1) {
	    owps += owp[i];
	    mennyi++;
	}
    }
    return owps / mennyi;
}


int main() {
    int T;
    cout.precision(12);

    cin >> T;
    for(int t = 0; t < T; t++) {
	int N;
	cin >> N;

	vector<vector<int> > data;
	vector<vector<double> > data2;

	for(int i = 0; i < N; i++) {
	    vector<int> v;
	    vector<double> v2;

	    double played = 0.0;
	    double won = 0.0;

	    for(int j = 0; j < N; j++) {
		char c;
		cin >> c;
		if(c == '1') {
		    v.push_back(1);
		    played += 1.0;
		    won += 1.0;
		}
		else if(c == '0') {
		    played += 1.0;
		    v.push_back(0);
		}
		else if(c == '.')
		    v.push_back(-1);
	    }
	    v2.push_back(won / played); // WP
	    data.push_back(v);
	    data2.push_back(v2);
	}
	cout << "Case #" << t + 1 << ":" << endl;
	for(int i = 0; i < N; i++)
	    get_owp(data, i, N);
	for(int i = 0; i < N; i++) {
	    double wp = data2.at(i).at(0);
	    double _owp = owp[i];
	    double oowp = get_oowp(data, i, N);
//	    cout << "wp: " << wp << ", owp: " << _owp << ", oowp: " << oowp << endl;
	    cout << 0.25*wp + 0.5*_owp + 0.25*oowp << endl;
	}
    }
}
