#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;


int main()
{
	//const char* iFileName = "A-small-attempt2.in";
	const char* iFileName = "A-large.in";
	const char* oFileName = "out1.txt";

	ifstream iFile(iFileName);
	ofstream oFile(oFileName);
	int N;
	iFile >> N;
	for(int caseNum=1; caseNum<=N; ++caseNum)
	{
		unsigned int n, k;
		iFile >> n >> k;
		const string on("ON");
		const string off("OFF");
		string ans;
		int t = (1<<n);
		for(int j=1; ; ++j)
		{
			if(k == t-1)
			{
				ans = on;
				break;
			}
			if(k < t-1)
			{
				ans = off;
				break;
			}
			t += (1<<n);
		}
		oFile << "Case #" << caseNum << ": " << ans << endl;
	}
	return 0;
}