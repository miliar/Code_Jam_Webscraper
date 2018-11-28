// Helloworld : Console application project sample.

#include <iostream>
#include <fstream>

#include <string>
#include <vector>
using namespace std;


int main()
{
	ifstream fin ("A-large.in");
	ofstream fout ("out.txt");
	int t, i, n;
	int a, b, j, s;
	int count;
	vector <int> r;
	vector <int> l;
	fin >> t;
	for (i = 0; i < t; i++){
		fin >> n;
		r.clear();
		l.clear();
		count=0;
		fout << "Case #" << i + 1 << ": ";
		for(j = 0; j < n; j++){
			fin >> a >> b;
			l.push_back(a);
			r.push_back(b);
			for(s = 0; s < l.size()-1; s++){
				if ((l[s] > a && r[s] < b) || (l[s] < a && r[s] > b)){
					count ++;
				}
			}
		}
		fout << count << endl;
	}
	
	return 0;
}
