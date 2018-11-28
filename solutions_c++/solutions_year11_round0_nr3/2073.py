#include <iostream> 
#include <cmath> 
#include <string> 
#include <cstring> 
#include <set> 
#include <map> 
#include <vector> 
#include <cstdio> 
using namespace std; 

int main(int argc, char *argv[]) 
{ 
 freopen("A.txt","r",stdin);
freopen("AOUT.txt","w",stdout);
	int tstCs = 1;
	int T = 0;
	cin >> T;
	while (T--)
	{
		int N;
		cin >> N;
		int t = 0, sum = 0, mn = INT_MAX;
		int c;
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &c);
			t ^= c;
			sum += c;
			mn <?= c;
		}
		bool can = false;
		int ret = 0;
		if (t == 0) 
		{
			can = true;
			ret = sum - mn;
		}
		if (can)
			cout << "Case #" << tstCs++ << ": " << ret << endl;
		else 
				cout << "Case #" << tstCs++ << ": NO" << endl;
		
	}
    return 0; 
}

