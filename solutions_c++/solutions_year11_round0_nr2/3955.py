#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <set>

using namespace std;

typedef pair<char,char> pcc_t;
typedef map<pcc_t,char> tcc_t;
typedef set<pcc_t> scc_t;

int main(int argc, char *argv[])
{
	int T; cin >> T;
	for( int t = 0 ; t < T ; t++ ) {
		tcc_t combine;
		scc_t opposed;

		int C; cin >> C;
		for( int c = 0 ; c < C ; c++ ) {
			string com = ""; 
			cin >> com;
			combine[make_pair<char,char>(com[0],com[1])] = com[2];
			combine[make_pair<char,char>(com[1],com[0])] = com[2];
			//cout << "Com : " << com << endl; 
		}

		int D; cin >> D;
		for( int d = 0 ; d < D ; d++ ) {
			string opp = "";
			cin >> opp;
			opposed.insert(make_pair<char,char>(opp[0],opp[1]));
			opposed.insert(make_pair<char,char>(opp[1],opp[0]));
			//cout << "Opp : " << opp << endl;
		}

		int N; cin >> N;
		string str = "";
		string EL = "";
		cin >> str;	
		//cout << "Str : " << str << endl;
		if( N > 0 ) EL += str[0];
		for( int i = 1 ; i < N ; i++ ) {

			pcc_t p = make_pair<char,char>(EL[EL.length()-1],str[i]);
			if( combine.find(p) != combine.end() ) { 
				EL[EL.length()-1] = combine[p];
				continue;
			}


			int l = EL.length();
			bool flag = false;
			for( int j = 0 ; j < l ; j++ ) {
				pcc_t p2 = make_pair<char,char>(EL[j],str[i]);
				if( opposed.find(p2) != opposed.end() ) {
					EL = "";
					flag = true;
					break;
				}
			}

			if(flag) continue;
		    EL += str[i];
			
			//cout << i << " : " << str[i] << " ==> " << EL << endl; 
		
		}	

		cout << "Case #" << t+1 << ": [";
		int K = EL.length();
		for( int i = 0 ; i < K-1 ; i++ )  cout << EL[i] << ", ";
		if( K > 0) cout << EL[K-1];
		cout << "]" << endl;

	}



   return 0;
}
