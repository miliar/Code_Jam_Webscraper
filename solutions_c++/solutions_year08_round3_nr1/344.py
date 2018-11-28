#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
#include <iterator>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cassert>
#include <string>
#include <ctime>
#include <cmath>

using namespace std;


#define FOR(x,b) for(int x=0;x<int(b);x++)
#define  PI 3.141592653589
#define  SI 0.707106781186548
#define F(x) ((x)*(x))




int main()
{
	ifstream file1("A-large.in");
	ofstream file2("A-large.out");
    int i,j;
	int P,K,L,N;
	file1>>N;
	vector<int> letter;

	
	for (i=1;i<=N;i++)
	{
		file1>>P>>K>>L;
		letter.resize(L);

		for (j=0;j<L;j++)
			file1>>letter[j];

		sort(letter.begin(),letter.end());

		long long int result=0;
		for (j=0;j<L;j++)
		{
			result+=(int(j/K)+1)*letter[L-j-1];
		}
	

		file2<<"Case #"<<i<<": "<<result<<endl;
		cout<<"Case #"<<i<<": "<<result<<endl;

	}

	file1.close();
	file2.close();


	return 0;
}