#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int divide(int p,int si)
{
	int t = si / 3;
	if ( si % 3 == 0){
		if (t >= p)
			return 1;
		else if (t + 1 >= p && t-1 >= 0)
			return 2;
	}else if (si % 3 == 1){
		if (t + 1 >= p)
			return 1;
	}else{
		if (t + 1 >= p)
			return 1;
		else if (t+2 >= p)
			return 2;
	}
	return 0;
}

int main()
{
	freopen("B-large.in" ,"r",stdin);
	freopen("B-large.out" ,"w" ,stdout);

	int T ,N ,S ,p;
	vector<int> si;
	cin >> T ;
	for (int t = 0 ;t < T ;++t){
		cin >> N >> S  >> p;
		int res ;
		int res1 = 0 ,res2 = 0;
		for (int i = 0 ;i < N ;++i){
			int si;
			cin >> si;
			if (divide(p ,si) == 1)
				res1 += 1;
			else if(divide(p ,si) == 2)
				res2 += 1;
		}
		res = res1 + min(res2 ,S);
		cout << "Case #" << t+1 << ": " << res << endl; 
	}
}
