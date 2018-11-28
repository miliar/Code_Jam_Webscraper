#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
using namespace std;

ifstream fin("in");
ofstream fout("out");

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		map< pair<char,char> , char > combinations;
		map< pair<char,char> , int > opposed;
		vector<char> list;
		int C,D,N;
		fin>>C;
		for(int i=0; i<C; i++) {
			char a,b,c; fin>>a>>b>>c;
			combinations[make_pair(a,b)]=c;
			combinations[make_pair(b,a)]=c;
		}
		fin>>D;
		for(int i=0; i<D; i++) {
			char a,b; fin>>a>>b;
			opposed[make_pair(a,b)]=1;
			opposed[make_pair(b,a)]=1;
		}
		fin>>N;
		for(int i=0; i<N; i++) {
			char element; fin>>element;
			int n = (int)list.size();
			if(n>=1) {
				char last = list[n-1];
				pair<char,char> p = make_pair(element,last);
				if(combinations.count(p)>0)
					list[n-1] = combinations[p];
				else {
					bool b=true;
					for(int j=n-1; j>=0; j--) {
						char el = list[j];
						p = make_pair(element, el);
						if(opposed.count(p)>0) {
							list.clear();
							b=false;
							break;
						}
					}
					if(b)
						list.push_back(element);
				}
			}
			else
				list.push_back(element);
		}

		fout << "Case #" << t << ": [";
		int n = (int)list.size();
		for(int i=0; i<n; i++) {
			fout << list[i];
			if(i<n-1)
				fout << ", ";
		}
		fout << "]" << endl;
	}

	return 0;
}


