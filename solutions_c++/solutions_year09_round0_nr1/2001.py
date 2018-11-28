#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int L,D,N;
	cin >> L >> D >> N;
	//clog << L << " " << D << " "<< N << endl;

	vector<string> dic(D);
	for(int i = 0; i < D; ++i){
		string t;
		cin >> t;
		dic[i] = t;
		// clog << t << endl;
	}
	for(int i = 0; i < N; ++i){
		string w;
		cin >> w;
		// clog << w << endl;
		bool multiple = false;
		int pos=0;
		vector<bool> ok(D,true);
		vector<bool> letter_ok(D,false);
		for(int j = 0; j < w.size(); j++){
			// clog << w[j] << " -- ";
			
			if(w[j]=='('){
				//	clog << endl;
				multiple = true;
				continue;
			}
			if(w[j]==')'){
				multiple = false;
				pos++;
				for(int k = 0; k < D; ++k){
					// clog << "("<<k<<","<<ok[k]<<","<<letter_ok[k]<<") ";
					ok[k] = ok[k] and letter_ok[k];
					letter_ok[k] = false;
				}
				// clog << endl;
				continue;
			}
			for(int k = 0; k<D ; ++k){
				if(!ok[k] or pos >= dic[k].size()){
					// clog << "("<< dic[k][pos] << "," << w[j] << "," << ok[k]<< ",1) ";
					continue;
				}
				if(!multiple){
					if(dic[k][pos]!=w[j]){
						ok[k] = false;
						// clog << "(" << dic[k][pos] << "," << w[j] << "," << ok[k] <<",2) ";
						continue;
					}
				}
				if(multiple and !letter_ok[k]){
					if(dic[k][pos]==w[j]){
						// clog << "(" << dic[k][pos] << "," << w[j] << "," << ok[k] << ",3) ";
						letter_ok[k]=true;
						continue;
					}
				}
				// clog << "(" << dic[k][pos] << "," << w[j] << "," << ok[k] << ",4) ";
			}
			// clog << pos << endl;
			if(!multiple)
				pos++;
		}
		cout << "Case #" << i+1 << ": " << count(ok.begin(),ok.end(),true) << endl;
	}

}
