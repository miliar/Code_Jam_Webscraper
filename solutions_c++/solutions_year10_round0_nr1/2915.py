// Funny.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(char** argv)
{
	ifstream in("A-large.in");
	ofstream output("A-large.out");

	int T, N, K;
	in >> T;
	for(int t = 0; t < T; t++)
	{
		in >> N >> K;

		bool res = true;
		for(int i = 0; i < N; i++)
		{
			if(K % 2 == 0)
			{
				res = false;
				break;
			}
			K /= 2;
		}
		if(res)
			output << "Case #" << t + 1 << ": " << "ON" << endl;
		else
			output << "Case #" << t + 1 << ": " << "OFF" << endl;


	}
	return 0;
}
