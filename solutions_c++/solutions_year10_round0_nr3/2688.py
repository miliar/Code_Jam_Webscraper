#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <set>
using namespace std;

int main(int argc, char **argv)
{
	ifstream ifstr("C:\\Documents and Settings\\login\\Desktop\\small.in");
	int nC;
	ifstr >> nC;
	ofstream ofstr("small.out");
	for (int i = 0; i < nC; i++)
	{
		int R, k, N;

		ifstr >> R >> k >> N;
		int *iArr = new int[N];
		for (int j = 0; j < N; j++)
			ifstr >> iArr[j];

		int tot = 0;
		int count = 0;
		for (int j = 0; j < R; j++)
		{
			int sum = 0;
			cout << "Round : " << j << endl;
			
			int start = count;
			while(sum+iArr[count] <= k)
			{
				
				
				tot+=iArr[count];
				cout << iArr[count];

				sum += iArr[count];
				count++;
				if (count == N)
					count=0;
				if (count == start)
					break;
			}
			cout << endl;
		}
		ofstr << "Case #" << i+1 << ": " << tot << endl;
	}
	return 0;
}
