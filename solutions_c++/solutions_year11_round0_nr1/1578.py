#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


void printints(vector<int> & v){
	for(int i = 0; i < v.size(); i++){
		cout << v[i] << " ";
	}
	cout << endl;
}
void printchars(vector<char> & v){
	for(int i = 0; i < v.size(); i++){
		cout << v[i] << " ";
	}
	cout << endl;
}

int main(){
	vector<int> b;
	vector<int> o;
	vector<char> seq;
	ifstream in("A-large.in");
	ofstream out("result.out");
	int T;
	in >> T;
	for(int i = 1; i <= T; i++){
		b.clear();
		o.clear();
		seq.clear();
		string line;
		int N;
		in >> N;
		for(int j = 0; j < N; j++){
			char c;
			int l;
			in >> c;
			seq.push_back(c);
			if(c=='O'){
				in >> l;
				o.push_back(l);
			}else if(c=='B'){
				in >> l;
				b.push_back(l);
			}
		}
		for(int j = b.size()-1; j >= 1; j--){
			int v = b[j]-b[j-1];
			b[j]=(v>=0?v:-v);
		}
		b[0]=b[0]-1;
		for(int j = o.size()-1; j >= 1; j--){
			int v = o[j]-o[j-1];
			o[j]=(v>=0?v:-v);
		}
		o[0]=o[0]-1;
		int counter = 0;
		int bind = 0;
		int oind = 0;
		int seqind = 0;

		while(seqind < seq.size()){
			if(seq[seqind]=='O'){
				if(o[oind]==0){
					oind++;
					seqind++;
				}else{
					o[oind]--;
				}
				if(bind < b.size() && b[bind] > 0){
					b[bind]--;
				}
			}else if(seq[seqind]=='B'){
				if(b[bind]==0){
					bind++;
					seqind++;
				}else{
					b[bind]--;
				}
				if(oind < o.size() && o[oind] > 0){
					o[oind]--;
				}
			}
			counter++;
		}
		out << "Case #" << i << ": " << counter << endl;
	}

	return 0;
}
