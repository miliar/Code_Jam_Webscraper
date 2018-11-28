#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using std::string;
using std::cout;
using std::cin;
using std::cerr;
using std::vector;

int main()
{
	int tc_count;
	cin >> tc_count;
	for(int tc_index=1; tc_index <= tc_count; tc_index++)
	{
		bool ok = false;
		int n, pd, pg;
		cin >> n >> pd >>pg;

		int start = 1;

/*		
		start = n -100;
		if(start < 0)
			start = 1;
*/
		for(int i =start; i<=n; i++) 
		{
			double x = i * pd / 100.0;
			long l = x;
			if(fabs(l-x) < 1e-9)
				ok = true;
		}

		if(ok)
		{
			if( (pg == 0) || (pg == 100))
				ok = (pg == pd);
		}

		cout << "Case #" << tc_index <<  ": " 
		<< (ok? "Possible": "Broken")
		<< "\n";
	}
	return 0;
}
