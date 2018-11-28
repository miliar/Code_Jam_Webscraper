#include <iostream>
using namespace std;

struct level
{
	int time;
	int die;
	int index;
};

bool operator<(const level& a, const level& b)
{
	if(a.time*100 + b.time*(100-a.die) < b.time*100 + a.time*(100-b.die))
		return true;
	else if(a.time*100 + b.time*(100-a.die) > b.time*100 + a.time*(100-b.die))
		return false;
	return a.index < b.index;
}

level l[1000];

int main()
{
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		int N;
		cin >> N;
		for(int i=0;i<N;i++)
		{
			l[i].index = i;
			cin >> l[i].time;
		}
		for(int i=0;i<N;i++)
			cin >> l[i].die;
		cout << "Case #" << t << ":";
		sort(l,l+N);
		for(int i=0;i<N;i++)
			cout << " " << l[i].index;
		cout << endl;
	}
}
