#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include<fstream>
#include <algorithm>

using namespace std;

ifstream in("B-large.in");

int main(void){
	freopen("B-large.out","wt",stdout);
	int cases, iC, iD, iN;
	string S;
    map<string, char> mC;
	map<string, char> ::const_iterator it;
	vector<string> vD;
	vector<string>::iterator itD;
	vector<char> vN;
	vector<char>::iterator itN;
	string result;

	getline(in,S);
	stringstream ss(S);
	ss >> cases;
	for(int i = 1; i <= cases; i++){
		getline(in,S);
		stringstream ss(S);
		vN.clear();
		mC.clear();
		vD.clear();
		result = "";

		ss >> iC;
		for(int j = 0; j < iC; j++){
			string c;
			ss >> c;
			string r;
			r  = c[0];
			r += c[1];
			mC.insert(pair<string, char>(r, c[2]));
			r  = c[1];
			r += c[0];
			mC.insert(pair<string, char>(r, c[2]));
		}

		ss >> iD;
		for(int k = 0; k < iD; k++){
			string d;
			ss >> d;
			vD.push_back(d);
		}

		ss >> iN;
			string cn;
			ss >> cn;
		for(int n = 0; n < iN; n++){
			if(vN.size() > 0){
				string f;
				f = cn[n];
				f+=vN.back();
				it = mC.find(f);

				if(it == mC.end()){
					vN.push_back(cn[n]);
					for(itD = vD.begin(); itD != vD.end(); ++itD){
						string sD = *itD;
						if(( find(vN.begin(), vN.end(), sD[0])!=vN.end() )&&( find(vN.begin(), vN.end(), sD[1])!=vN.end() )){
							vN.clear();
						}
						
					}
				}
				else
				{
					vN.pop_back();
					vN.push_back(it->second);
				}
			}
			else
				vN.push_back(cn[n]);

		}
		for(itN = vN.begin(); itN != vN.end(); ++itN){
			result += *itN;
			result += ", ";
		}
		if(result.size()>0)
		result.resize(result.size()-2, '|');
		cout <<	"Case #" << i << ": [" << result << "]" << endl;
	}
    return 0;
}
