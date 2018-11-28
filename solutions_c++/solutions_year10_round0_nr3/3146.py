#include <iostream>
#include <fstream>

using namespace std;


int main () {
    ifstream ifs( "/Users/seki/Desktop/cpps/GoogleCodeJam2010/Qualification3/C-small-attempt0.in.txt" );
	std::ofstream ofs( "/Users/seki/Desktop/cpps/GoogleCodeJam2010/Qualification3/C-small-attempt0.out.txt",  std::ios::trunc );
	
	int sampleNum = 0;
	
	ifs >> sampleNum;
	
	for (int i = 1; i <= sampleNum ; i++) {
		long int R = 0;
		long int k = 0;
		int N = 0;
		
		ifs >> R >> k >> N;
		long int *g;
		g = new long int[N];
		for (int j = 0; j < N; j++) {
			ifs >> g[j];
			
		}
		
		long int result = 0;
		for (long int j = 0; j < R; j++) {
			//ride
			long int riding = 0;
			long int l;
			for (l = 0;l < N;l++) {
				if(riding+g[l] > k){
					break;
				}else{
					riding += g[l];
				}
			}
		
			l--;
			long int *tmp;
			tmp = new long int[N];
			memcpy(tmp, g, N*8);
			
			for (int m = l+1; m < N; m++) {
				g[m-l-1] = tmp[m];
			}
			for (int m = 0; m <= l; m++) {
				g[m+N-l-1] = tmp[m];
			}
			
			delete [] tmp;
			
			result+=riding;
		}
		
		
		
		ofs << "Case #" << i << ": " << result << std::endl;	
	}
	
	return 0;
}