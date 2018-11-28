#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
int readInt(ifstream& fin){
	stringstream ss;
	string temp;
	int n=-1;
	getline(fin, temp); 
	ss << temp;
	ss >> n;
	return n;
}

int main() {

	int T;
	long long ans, t_ans; 
	int p, k, l;
	
	p=k=l=0;
	T=0;
	ans=t_ans=0; 
	p=k=l=0;
	int t;
	
	vector<int> v;

	ifstream fin("1.in");
	ofstream fout("1.out");

	T = readInt(fin);
	t=0;
	
	for(int i=0; i<T; i++){
		ans=0;
		v.clear();
		fin >> p >> k >>l;
		for (int j=0; j<l; j++) {
			fin >> t;
			v.push_back(t);
		}
		
		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
	
		vector<int>::iterator iter = v.begin();
		for(int a=0; a<p && iter!=v.end(); a++) {
			for(int b=0; b<k && iter!=v.end(); b++) {
				ans+=*(iter++)*(a+1);
			}
		}

		fout << "Case #" << i + 1 << ": " << ans <<endl;
		cout << "Case #" << i + 1 << ": " << ans <<endl;
	}

	return 0;
}
