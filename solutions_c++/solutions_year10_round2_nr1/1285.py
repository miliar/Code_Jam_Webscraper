#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


int main () {
    ifstream ifs( "../../A-large.in.txt" );
	std::ofstream ofs( "../../A-large.out.txt",  std::ios::trunc );
	
	int T = 0;
	
	ifs >> T;
	
	for (int i = 1; i <= T ; i++) {
		int N;
		int M;
		
		
		int result = 0;
		
		ifs >> N >> M;
		
		string* ex;
		ex = new string[N];
		string* mk;
		mk = new string[M];
		for (int j = 0; j < N; j++) {
			ifs >> ex[j];
			ex[j] = ex[j].substr(1);
			//cerr << ex[j] <<endl;
		}
		for (int j = 0; j < M; j++) {
			ifs >> mk[j];
			mk[j] = mk[j].substr(1);
			//cerr << mk[j] << endl;
		}
		
		vector<string> dir;
		for (int j = 0; j < N; j++) {
			int at = 0;
			string tmp = ex[j];
			int tmpat = 0;
			while (at != -1) {
				at = tmp.find('/');
				if(at != -1){
					tmpat += at;
					dir.push_back(ex[j].substr(0, tmpat));
					cerr << dir[dir.size()-1] << endl;
					tmp = tmp.substr(at+1);
					tmpat ++;
				}
			}
			dir.push_back(ex[j]);
			cerr << dir[dir.size()-1] << endl;
		}
		
		for (int j = 0; j < M; j++) {
			int tmpat = 0;
			string tmp = mk[j];
			bool fin = false;
			while (!fin) {
			
			
				
			
			int at = tmp.find('/');
			string path;
			if(at != -1){
				tmpat += at;
				path = mk[j].substr(0,tmpat);
				tmp = tmp.substr(at + 1);
				tmpat++;
			}else {
				path = mk[j];
				fin = true;
			}
			bool already = false;
			for (int k = 0; k < dir.size() ; k++) {
	
					if(dir[k] == path){
						already = true;
					}
				
			}
			if(!already){
				result++;
				dir.push_back(path);
			}
			
				
				
			
				
			}
		}
		
		

		ofs << "Case #" << i << ": " << result << std::endl;
		cerr << N << ',' << M << "Case #" << i << ": " << result << std::endl;
	}
	
	return 0;
}