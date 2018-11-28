#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

class StringTokenizer{
public:
	static vector <string> tokenize(string &in,string seps){
		string token;
		vector <string> ret;
		for(size_t i=0;i<in.size();i++){
			if(seps.find(in.substr(i,1)) == string::npos){
				token = token +in.substr(i,1);
				if((i==in.size()-1)&&(token.size()!=0))
					ret.push_back(token);
			}
			else{
				if(token.size()>0){
					ret.push_back(token);
					token = "";
				}
			}
		}
		return ret;
	}
};

int commonPrefixLength(vector <string> &vs1, vector<string> &vs2){
	int n = 0;
	for(int i=0;(i<vs1.size())&&(i<vs2.size());i++){
		if (vs1[i]==vs2[i]) n++;
		else break;
	}
	return n;
}

int main(){
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("A-large.out");
	int T;
	fin >> T;
	for(int i=0;i<T;i++){
		int N, M;
		fin >> N >> M;
		string s;
		getline(fin,s);
		vector < vector <string> > oldpaths;
		vector < vector  <string> > newpaths;
		for(int j=0;j<N;j++){
			getline(fin,s);
			vector <string> vs = StringTokenizer::tokenize(s,"/");
			oldpaths.push_back(vs);
		}
		for(int j=0;j<M;j++){
			getline(fin,s);
			vector <string> vs = StringTokenizer::tokenize(s,"/");
			newpaths.push_back(vs);
		}
		int ans = 0;
		for(int j=0;j<M;j++){
			int mx =0;
			for(int k=0;k<oldpaths.size();k++){
				int qq = commonPrefixLength(newpaths[j],oldpaths[k]);
				mx = max(mx,qq);
			}
			ans+= newpaths[j].size()-mx;
			oldpaths.push_back(newpaths[j]);
		}
		fout << "Case #" << i + 1 << ": " << ans << endl;
		

	}
	return 0;
}