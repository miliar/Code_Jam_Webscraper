#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for (int t = 0;t<T;t++)
	{
		cout<<"Case #"<<t+1<<": ";
		int N,S,p;
		cin>>N>>S>>p;
		int answer = 0;
		for (int j = 0;j<N;j++)
		{
			int score;
			cin>>score;
			if (score<3*p-4 or score<p) continue;
			if (score>=3*p-2)
			{
				answer++;
				continue;
			}
			if (S>0)
			{
				S--;
				answer++;
			}
		}
		cout<<answer<<endl;
	}
	return 0;
}
