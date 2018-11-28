#include <iostream>
using namespace std;

int main()
{
  int T; cin >> T;
	int caseNum = 1;
	
	while(T > 0)
	{
		int N,S,p;
		cin >> N >> S >> p;
		int ans = 0;
		int possible_reverse = 0;
		
		int t;
		for(int i=0;i<N;i++) 
		{
			cin >> t;
			if(t >= 3*p - 2) 
				{ans++;}
			else
			{
				if((p != 1) && (t >= 3*p - 4) && (S > 0)) {ans++; S--;}
			}
		}
		
		cout << "Case #" << caseNum << ": " << ans << endl;
		caseNum++;
		T--;
	}

  return 0;
}
