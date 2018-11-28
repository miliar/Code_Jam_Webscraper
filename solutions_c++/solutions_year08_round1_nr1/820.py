#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

template<typename T1, typename T2> T1 cast(const T2 &v) 
{ 
	T1 ret; 
	stringstream s; 
	s << v; 
	s.seekg(O); 
	s >> ret; 
	return ret; 
} 

int main()
{
	int T, size, data;
	int a, b;
	int rst;

	vector <int> data1, data2;

	scanf("%d", &T);

	for(int i=1; i<=T; ++i)
	{
		data1.clear();
		data2.clear();
		rst = 0;

		scanf("%d", &size);

		int idx;
		
		for(idx=0; idx < size; ++idx)
		{
			scanf("%d", &data);
			data1.push_back(data);
		}

		for(idx=0; idx <size; ++idx)
		{
			scanf("%d", &data);
			data2.push_back(data);
		}

		sort(data1.begin(), data1.end());
		sort(data2.begin(), data2.end());

		for( a =0, b = data2.size()-1; a < data1.size(); ++a, --b)
			rst += (data1[a] * data2[b]);

		cout << "Case #" << i << ": " << rst << endl;

	}
	return 0;
}
