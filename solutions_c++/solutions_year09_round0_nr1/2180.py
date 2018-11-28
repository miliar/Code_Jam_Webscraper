#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <stack>
#include <queue>
#include <complex>
#include <set>
#include <list>
#include <iomanip>



using namespace std;
#define FOR(i,n) for(int i=0;i<(int)n;++i)
#define FORI(p, x) for (int i = p; i < (int)(x); ++i)
#define FORJ(p, x) for (int j = p; j < (int)(x); ++j)
#define FORK(p, x) for (int k = p; k < (int)(x); ++k)



// BEGIN CUT HERE
int main() {
//	ifstream cin("in.txt");
//	ifstream cin("A-small-attempt0.in");
	ifstream cin("A-large.in");
	ofstream cout("out.txt");
	
	int L,D,N;
	cin>>L>>D>>N;
	vector<string> str;
	string s;
	FORI(0,D){
		cin>>s;
		str.push_back(s);
	}

	FORI(0,N){
		cin>>s;
		int cnt=0;
		FORJ(0,D){
			int len=0;
			FORK(0,s.size()){
				bool flg=false;
				if(s[k]=='('){
					k++;
					while(s[k]!=')'){
						if(s[k]==str[j][len]){
							flg=true;
							while(s[k]!=')')
								k++;
							break;
						}
						else
							k++;
					}
					if(flg){
						len++;
						continue;
					}
					else
						break;
				}
				else{
					if(s[k]==str[j][len]){
						len++;
						continue;
					}
					else
						break;
				}

			}
			if(len==L)
				cnt++;
		}
		cout << "Case #" << i+1 <<": " << cnt << endl;
	}


	
		
	
	return 0;
}

