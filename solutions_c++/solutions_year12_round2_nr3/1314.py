#include <iostream>
#include <map>
#include <set>

using namespace std;

ostream& operator<<(ostream& os, set<int> i)
{
	if (i.size()==0) cout<<"NULL";
	for (set<int>::iterator it=i.begin(); it!=i.end(); ++it) os<<*it<<" ";
	os<<endl;
	return os;
}

void sum(int N, int num[])
{
	int C = 1 << 20;
	map<int, set<int> > mnum;
	int count = 0;
	for(int i = 0; i < C; i++)
		{
			set<int> temp;
			int sum = 0;
			for(int j = 0; j < N; j++)
				{
					if(i >> j & 1) 
						{
							temp.insert(num[j]);
							sum += num[j];
						}
				}
			if(mnum.find(sum) != mnum.end()) 
				{
					set<int> set1 = mnum[sum];
					cout << set1 << temp;
					break;
				}
			else 
				{
					count++;
					mnum[sum] = temp;
				}
		}
	if(count == C) cout << "Impossible" << endl;
}

int main()
{
	int T;
	cin >> T;
	
	for(int i = 0; i < T; i++)
		{
			int N;
			cin >> N;
			
			int num[N];
			for(int j = 0; j < N; j++)
				cin >> num[j];
			cout << "Case #" << i+1 << ":" << endl;
			sum(N, num);
		}
	
	return 0;
}
