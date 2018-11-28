#include <iostream>
#include <fstream>

using namespace std;
int main () {
    ifstream ifs( "/Users/seki/Desktop/cpps/GoogleCodeJam2010/Qualification1/A-large.in.txt" );
	std::ofstream ofs( "/Users/seki/Desktop/cpps/GoogleCodeJam2010/Qualification1/A-large.out.txt",  std::ios::trunc );

	int sampleNum = 0;
	
	ifs >> sampleNum;
	
	for (int i = 1; i <= sampleNum ; i++) {
		int N = 0;
		long int K = 0;
		
		ifs >> N >> K;
		
		bool light = 1;
		for (int j = 0; j < N; j++) {
			light = light && (K%2);
			K = K/2;
		}

		string result = "ON";
		if(!light) result = "OFF";
		ofs << "Case #" << i << ": " << result << std::endl;	
	}
	
	return 0;
}