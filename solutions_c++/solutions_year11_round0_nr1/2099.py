#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int t;
	inf >> t;
	for (int i = 1; i <= t; i++) {
		int n;
		inf >> n;
		int pos[2] = {1,1}, prevTime[2] = {0,0}, time = 0;
				
		for (int j = 0; j < n; j++) {
			char c;
			inf >> c;
			int a;
			inf >> a;
			int index;
			if (c == 'O')
				index = 0;
			else if (c == 'B')
				index = 1;
			else cout << "WTF in test " << i << endl;
			
			int r = abs(a-pos[index]);
			time += time - prevTime[index] - r > 0 ? 0 : abs(time - prevTime[index] - r);
			time++;
			pos[index] = a;
			prevTime[index] = time;
			
		}
		cout << time << endl;
		outf << "Case #" << i << ": " << time << endl;
	}
	outf.close();
	inf.close();
	return 0;
}