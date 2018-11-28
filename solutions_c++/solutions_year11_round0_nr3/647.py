#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
  int T;
	cin >> T;
	int case_num = 1;
	while(T>0)
	{
	  int N; 
		cin >> N;
		vector<int> c(N);
		for(int i=0;i<N;i++)  cin >> c[i];
		sort(c.begin(), c.end());
		vector<int> v = c;
		
		bool ok = true;
		while(ok && v[N-1] != 0)
		{
		  int sum = 0;
			for(int i=0;i<N;i++) {sum += (v[i] % 2); v[i] /= 2;}
			if( (sum % 2) != 0) ok = false;	
		}
		if(ok)
		{
		  long long total = 0;
			for(int i=1; i<N;i++) total += c[i];
			cout << "Case #" << case_num << ": " << total << endl;
		}
		else cout << "Case #" << case_num << ": NO" << endl;
	
	  T--; case_num++;
	}
 
  return 0;
}
