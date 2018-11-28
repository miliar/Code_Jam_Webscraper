#include <fstream>
using namespace std;

ifstream fin("c:\\pro\\A-large.in");
ofstream fou("c:\\pro\\output1_l.txt");


int main()
{
	unsigned int T , N , K, tmp;
	fin >> T;
	for (unsigned int i=1; i<=T; i++){
		fou << "Case #" << i << ": ";
		fin >> N >> K;
		K=K % (1<<N);
		tmp = (1<<N)-1;
		if (K==tmp) {
			fou << "ON" << endl;
		}else{
			fou << "OFF" << endl;
		}
	}
	
	return 0;
}