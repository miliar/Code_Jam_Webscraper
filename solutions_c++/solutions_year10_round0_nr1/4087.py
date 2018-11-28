#include <fstream>
using namespace std;

ifstream fin("A.in");
ofstream fout("A.out");

int main() {
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int N,R;
		fin>>N>>R;
		bool on=true;
		for(int i=0; i<N; i++) {
			if((R & (1<<i)) == 0) {
				on=false;
				break;
			}
		}
		if(on)
			fout<<"Case #"<<t<<": "<<"ON"<<endl;
		else
			fout<<"Case #"<<t<<": "<<"OFF"<<endl;
	}
	return 0;
}
