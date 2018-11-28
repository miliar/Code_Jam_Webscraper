#include <iostream>
#include <cmath>
using namespace std;

struct vine
{
	int len;
	int dist;
	int hold;
	bool reach;
};

vine v[60000];

int main()
{
	int T;
	cin >> T;
	for(int k=1;k<=T;k++)
	{
		int N;
		double D;
		cin >> N;
		for(int i=0;i<N;i++)
		{
			cin >> v[i].dist >> v[i].len;
			v[i].reach = false;
		}
		v[0].reach = true;
		v[0].hold = v[0].dist;
		cout << "Case #" << k << ": ";
		cin >> D;
		bool success = false;
		for(int i=0;i<N;i++)
		{
			if(!v[i].reach) continue;
			if(v[i].dist + v[i].hold>=D)
			{
				success = true;
				break;
			}
			for(int j=i+1;j<N;j++)
			{
				if(v[j].dist <= v[i].dist + v[i].hold)
				{
					if(!v[j].reach || v[j].hold < min(v[j].dist - v[i].dist,v[j].len))
						v[j].hold = min(v[j].dist - v[i].dist,v[j].len);
					v[j].reach = true;
				}
				else
					break;
			}
		}
		if(success)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
}
