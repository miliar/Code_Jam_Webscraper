#include <iostream>
#include <string> 
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {

	ifstream infile;
	ofstream out;

	infile.open (argv[1], ifstream::in);
	out.open (argv[2], ifstream::out);

	//infile.open ("A-small-attempt0.in", ifstream::in);
	//out.open ("A-small.out", ifstream::out);

	int T, C, D, N;
	vector<string> comb, delt;
	string elist;

	infile>>T;
	
	for (int t=0; t<T; t++) {		
		char comb_map[26][26];
		char delt_map[26][26];

		for (int i = 0; i<26; i++)
			for (int j = 0; j<26; j++) {
				comb_map[i][j] = '-';
				delt_map[i][j] = '-';
			}

		string str;	

		infile>>C;
		for (int i = 0; i<C; i++) {
			infile>>str;
			comb.push_back(str);
			int x, y;
			x = str[0]-'A';
			y = str[1]-'A';
			comb_map[x][y] = str[2];
			comb_map[y][x] = str[2];
		}

		infile>>D;
		for (int i = 0; i<D; i++) {
			infile>>str;
			delt.push_back(str);
			int x, y;
			x = str[0]-'A';
			y = str[1]-'A';
			delt_map[x][y] = str[2];
			delt_map[y][x] = str[2];
		}

		infile>>N;
		infile>>elist;

		for (int n = 1; n<elist.length(); n++) {
			char c = comb_map[elist[n]-'A'][elist[n-1]-'A'];
			if (c != '-') {
				elist[n-1] = c;
				elist.erase(n, 1);
				n--;
			} 

			for (int i = 0; i<n; i++) {
				c = delt_map[elist[n]-'A'][elist[i]-'A'];
				if (c != '-') {
					elist.erase(0, n+1);
					n = 0;
					break;
				} 
			}

		}

		cout<<"Case #"<<t+1<<": [";
		int l = elist.length();
		for (int i = 0; i<l-1; i++) {
			cout<<elist[i]<<", ";
		}
		if (l>0) cout<<elist[l-1];
		cout<<"]"<<endl;

		out<<"Case #"<<t+1<<": [";
		for (int i = 0; i<l-1; i++) {
			out<<elist[i]<<", ";
		}
		if (l>0) out<<elist[l-1];
		out<<"]"<<endl;

	}


	infile.close();
	out.close();

    return 0;
}

