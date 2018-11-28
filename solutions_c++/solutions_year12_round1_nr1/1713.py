#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream fin("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.in");
	ofstream fout("C:\\Users\\ting\\Documents\\Visual Studio 2008\\Projects\\Google2012\\Debug\\file.out");

	int cases;

	fin >> cases;

	int counter = 1;
	while(counter <= cases)
	{
		int a, b;
		double prob;
		
		fin >> a >> b;

		int i = 0;
		double *probTable = new double[a];
		while(i < a)
		{
			fin >> prob;
			probTable[i] = prob;
		//	cout << "probTable[" << i << "] = " << prob << endl;
			i++;
		}

		// calc all correct prob: multiply all together
		double allCorrect = probTable[0];
		i = 1;
		while(i < a)
		{
			allCorrect = allCorrect * probTable[i];
			i++;
		//	cout << "all correct prob = " << allCorrect << endl;
		}

		// case 1: keep typing
		int keystrokes = b - a + 1;
		double expected, temp;
		expected = keystrokes * allCorrect;
		expected += (1 - allCorrect) * (b - a + 1 + b + 1);

		// case 3: press enter right away
		temp = b + 2;
		if(temp < expected)
			expected = temp;

		// case 2: backspace once
		for(i = 1; i < a; i++)
		{
			// success case
			keystrokes = i + i + b - a + 1;
			int keystrokes2 = keystrokes + b + 1;
			allCorrect = allCorrect / probTable[a - i];
			temp = keystrokes * allCorrect + keystrokes2 * (1 - allCorrect);
			if(temp < expected)
				expected = temp;
		}

		//fout << "Case #" << counter << ": " << expected << endl;
		cout.setf(std::ios::fixed);
		cout.precision(6);
		cout << "Case #" << counter << ": " << expected << endl;

		fout.setf(std::ios.fixed);
		fout.precision(6);
		fout << "Case #" << counter << ": " << expected << endl;
		counter++;
	}

	return 0;
}