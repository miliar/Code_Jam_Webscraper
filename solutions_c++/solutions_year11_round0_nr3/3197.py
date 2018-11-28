#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

//bool t[1000001];

int main()
{
	int tt,n;
	int tmp;
	cin >> tt;
	
	for (int test=1;test<=tt;test++)
	{
		vector<int> list;
		//memset(t,0,sizeof(t));
		//t[0]=1;
		cin >> n;
		long long sum=0,xorsum=0;
		for (int i=0;i<n;i++)
		{
			cin >> tmp;
			list.push_back(tmp);
			sum+=tmp;
			xorsum^=tmp;
			//t[tmp]=1;
		}
		if (xorsum!=0) 
		{
			cout << "Case #" << test << ": NO\n";
			continue;
		}

		sort(list.begin(),list.end());
		int ans = sum - list[0];
		cout << "Case #" << test << ": " <<ans << endl;


	}


	//system("pause");
	return 0;
}