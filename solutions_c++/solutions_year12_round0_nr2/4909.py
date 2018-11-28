#include <fstream>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	
	fin.open("B-large.in");
	fout.open("output.txt");
	
	int currS;
	int remS;
	int T;
	int N;
	int S;
	int P;
	
	int ans;
	
	int A, B, C;
	int sum;
	
	fin >> T;
	for(int c=1;c<=T;c++){
		ans=0;
		fin >> N >> S >> P;
		for(int i=0;i<N;i++){
			fin >> sum;
			switch (sum%3){
				case 0:
					if(sum/3>=P)
						ans++;
					else if(S&&sum)
						if((sum/3)+1>=P){
							S--;
							ans++;
						}
					break;
				case 1:
					if((sum/3)+1>=P)
						ans++;
					break;
				case 2:
					if((sum/3)+1>=P)
						ans++;
					else if(S)
						if((sum/3)+2>=P){
							ans++;
							S--;
						}
					break;
			}
		}
		fout << "Case #" << c << ": " << ans << endl;
	}
	
	return 0;
}

