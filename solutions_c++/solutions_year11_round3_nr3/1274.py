#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>

using namespace std;

long int lcm(long int a,long int b, long int MIN, long int MAX, long int cond)
{
	long int res = -1;
	cout << a << " " << b << " " << MIN << " " << MAX << endl;
    for(long int n= MIN; n < MAX; n++) {
		if(max(n, a) % min(n, a) == 0 && max(n, b) % min(n, b) == 0 && max(n, cond) % min(n, cond) == 0) {
			res = n;
			break;
		}
    }
	return res;
}

int main (int argc, char * const argv[]) {
	
	ifstream input(argv[1], ifstream::in);
	
	int testsNb;
	input >> testsNb;
	
	ofstream outfile(argv[2]);
	
	cout << "Testing " << testsNb << " cases..." << endl;
	
	int cases = 0;
	while (cases < testsNb) {
		long int N, L, H;
		input >> N;
		input >> L;
		input >> H;
		int local_count = 0;
		vector<long int> freqs;
		while (local_count < N) {
			int current;
			input >> current;
			freqs.push_back(current);
			local_count++;
		}
		cases++;
		
		//Compute
		sort(freqs.begin(), freqs.end());
		long int val = -1;
		for (long int j = max((long int)1, L); j <= H; j++) {
			bool stop = false;
			for (int i = 0; i < freqs.size() && !stop; i++) {
				if (max(j, freqs[i]) % min(j, freqs[i]) != 0) {
					stop = true;
				}
			}
			if (stop == false) {
				val = j;
				break;
			}
		}
		/*for (int i = 0; i < freqs.size() - 1 && !impossible; i++) {
			val = lcm(freqs[i+1], freqs[i], max(val, (long int)L), H, val);
			cout << val << endl;
			if (val == -1 || val > H) {
				impossible = true;
				break;
			}
		}*/
		outfile << "Case #" << cases << ": ";
		if (val == -1)
			outfile << "NO" << endl;
		else 
			outfile << val << endl;
	}
	
	input.close();
	outfile.close();
    return 0;
	
}