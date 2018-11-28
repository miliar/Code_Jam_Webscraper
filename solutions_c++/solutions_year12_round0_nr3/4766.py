#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int a, b;
	int T;
	cin >> T;
	set< pair<int,int> > s;
	for (int i = 0; i < T; i++)
	{
		
		cin >> a >> b;
		
		s.clear();
		for (int j = a; j <= b; j++)
		{
			int temp = j;
			vector<int> v_temp;
			while(temp!=0)
			{
				v_temp.push_back(temp % 10);
				temp = temp /10;
			}
			reverse(v_temp.begin(), v_temp.end());
			for (int l = 0; l < v_temp.size(); l++)
			{
				rotate(v_temp.begin(), v_temp.end()-1,v_temp.end());
				if(v_temp[0] != 0)
				{
					int x, y;
					int to_add = 0;
					for(int x =0; x<v_temp.size(); ++x)
					{
						
						to_add *= 10;
						to_add += v_temp[x];
						//~ cout << to_add << endl;
					}
					x = min(to_add, j);
					y = max(to_add, j);
					if (to_add != j && to_add <= b && to_add >= a)
					{
						//~ cout << "added "<< x << " "<< y <<endl;
						//~ cout << to_add << endl;
						s.insert(make_pair(x,y));
					}
					
				}
			}
			
		}
		cout << "Case #" << i+1 << ": " << s.size() << endl;
	}
	return 0;
}
