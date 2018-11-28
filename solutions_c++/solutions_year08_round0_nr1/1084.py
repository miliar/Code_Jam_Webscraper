#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef vector<string>::iterator VSI;
typedef map<string, bool>::iterator MSBI;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	map<string, bool> EN;
	vector<string> QR;

	int bool_count, ans;
	bool one_find;
	int N, S, Q;
	string s;

	in >> N;
	getline(in, s);

	for (int i=0; i<N; i++){
		in >> S;
		getline(in, s);

		ans = 0;
		EN.clear();
		QR.clear();
		bool_count = S;

		for (int j=0; j<S; j++){
			getline(in, s);
			EN[s] = false;
		}

		in >> Q;
		getline(in, s);

		for (int j=0; j<Q; j++){
			getline(in, s);
			QR.push_back(s);
		}

		//SOLVATION
		one_find=false;
		for (VSI j=QR.begin(); j!=QR.end(); j++){
			if (bool_count == 0){
				ans++;
				for (MSBI k=EN.begin(); k!=EN.end(); k++) k->second = false;
				bool_count = S;
			} else 
				if (bool_count == 1){
					if (!one_find){
						for (MSBI k=EN.begin(); k!=EN.end(); k++) 
							if (k->second == false) {s=k->first; break;}
						one_find = true;
					}
					if (*j == s){
						ans++;
						for (MSBI k=EN.begin(); k!=EN.end(); k++) k->second = false;
						bool_count = S;
						one_find = false;
					}
				}

			if (EN[*j] == false) bool_count--;
			EN[*j]=true;
		}
	
		out << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}