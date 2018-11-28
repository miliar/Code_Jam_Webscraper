#include <iostream>
#include <string>
#include <fstream>
using namespace std;

bool judge(int a, int b)
{
	if(a == 0 || b == 0)
		return true;
	if(a == b)
		return false;
	if(a < b)
		return judge(b, a);

	if(judge(b, a%b) == false)
		return true;
	else if((a % b) + b < a)
	{
		return true;
	}

	return false;
}

int main() {
	ifstream ifs("input.txt");
	ofstream ofs("output.txt");

	int T;
	ifs >> T;
	for(int i = 1; i <= T; ++i)
	{
		int A1, A2, B1, B2;
		ifs >> A1 >> A2 >> B1 >> B2;
		int count = 0;
		for(int I1 = A1; I1 <= A2; ++I1)
			for(int I2 = B1; I2 <= B2; ++I2)
			{
				if(judge(I1, I2))
					++count;
			}
		ofs << "Case #" << i << ": " << count << endl;
	}
	
	ifs.close();
	ofs.close();
	
	return 0;
}