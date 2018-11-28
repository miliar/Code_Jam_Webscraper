#include <fstream>
#include <vector>
using namespace std;


bool next_flags(bool flags[], int n);


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T, t, N, S, p;
	int input, i, mngb, mngp, mngpm, nt;
	vector<int> tests;
	bool flags[100];
	
	fin >> T;
	
	for (t = 1; t <= T; t++) {
		fin >> N >> S >> p;
		
		tests.clear();
		mngb = mngpm = 0;
		
		for (i = 0; i < N; i++) {
			fin >> input;
			
			if (input % 3 == 1 || input < 2 || input > 28) {
				if ((input + 2) / 3 >= p)
					mngb++;
			}
			else
				tests.push_back(input);
		}
		
		nt = tests.size();
		
		if (S >= nt) {
			mngpm = 0;
			
			for (i = 0; i < nt; i++)
				if ((tests[i] + 4) / 3 >= p)
					mngpm++;
		}
		else {
			for (i = nt-1; i >= nt-S; i--)
				flags[i] = true;
			
			for (; i >= 0; i--)
				flags[i] = false;
			
			do {
				mngp = 0;
				
				for (i = 0; i < nt; i++)
					if ((flags[i] ? tests[i] + 4 : tests[i] + 2) / 3 >= p)
						mngp++;
				
				if (mngp > mngpm)
					mngpm = mngp;
			} while (next_flags(flags, nt));
		}
		
		fout << "Case #" << t << ": " << mngb + mngpm << endl;
	}
	
	fin.close();
	fout.close();
	
	return 0;
}


bool next_flags(bool flags[], int n)
{
	int i, j, k = n-1;
	
	for (i = n-1; i > 0; i--)
		if (flags[i] && !flags[i-1])
			break;
	
	if (i == 0)
		return false;
	
	flags[i-1] = true;
	flags[i--] = false;
	
	for (j = n-1; j > i; j--)
		if (!flags[j])
			break;
	
	for (; j > i; j--)
		if (flags[j]) {
			flags[k--] = true;
			flags[j] = false;
		}
	
	return true;
}
