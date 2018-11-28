#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out1.txt", "w", stdout);
	int T;
	cin>>T;

	int N, S, p;
	int t[200];

	for(int ca = 1; ca <= T; ca++)
	{
		cout<<"Case #"<<ca<<": ";
		
		
		cin>>N>>S>>p;
		for(int i = 0; i < N; i++) cin>>t[i];
		sort(t, t + N);
		//for(int i = 0; i < N; i++) cout<<t[i]<<" ";
		int result = 0;
		for(int i = 0; i < N; i++)
		{ 
			if((p > 0) && (t[i] - 3 * p + 2 >= 0) ||
		       (p == 0))
			{
				result++;
				continue;
			}
			if((p > 1) && (t[i] - 3 * p + 4 >= 0 && S > 0))
			{
				result++;
				S--;
			}
		}
		cout<<result<<endl;
	}
	
	fclose(stdout);
	return 0;
}
