#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<algorithm>
#include<fstream>
#include<sstream>
#include <cmath>

using namespace std;

string rotate(string i)
{
//	cout << "Rotating:  " << i;
	i += i[0];
	i = i.substr(1, i.size()-1);

	//cout << " to this: " << i << endl;

	return i;
}
int process3(string s)
{
	int out = 0;
	istringstream iss(s);
	int a, b;

	set<pair<string, string> > added_set;

	iss >> a >> b;

	for (int i=a; i < b; ++i) {
		stringstream oss;
		oss << i;
		string orig_i(oss.str());
		string rotated_str = orig_i;

		//cout << "starting with m : " << orig_i << endl;

		for (int j = 0; j < orig_i.size()-1; j++) {
			rotated_str = rotate(rotated_str);
			istringstream iss(rotated_str);
			//cout << "cur n: " << rotated_str << endl;

			if (rotated_str[0] == '0')
				continue;
			int cur_b = 0;
			iss >> cur_b;
			if((i < cur_b) && (cur_b <= b)) {
				pair<string, string> cur_pair(make_pair(orig_i, rotated_str));
				if (added_set.find(cur_pair) == added_set.end()) {
				
					//found a valid value
					out++;
					added_set.insert(cur_pair);
				} else {
					// already added
				}
			}

		} 

	}
	return out;
}

int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("input.txt");
	else
		is.open(argv[1]);

	string s;
	getline(is,s); 
	istringstream iss(s);
	iss >> tc;

	for(int i = 1; i <= tc; i++)
	{
		cout << "Case #" << i << ": ";
		getline(is,s); 
		cout << process3(s) << endl;
	}
	is.close();
	return 0;
}
