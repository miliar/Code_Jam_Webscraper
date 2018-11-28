#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;

int line=0, testCases;

int main()
{
	scanf("%d",&testCases);
	for (line; line<testCases;line++)
	{
		vector<int> t;
		vector<double> average;
		int N, S, p, total=0;
		scanf("%d ",&N);
		scanf("%d ",&S);
		scanf("%d ",&p);		

		int temp;
		for(int i=0; i<N; i++)
		{
			scanf("%d", &temp);
			t.push_back(temp);
			average.push_back(0);
		}
		sort (t.begin(),t.end());
		for(int i=0; i<N; i++)
		{
			if(p==0)
			{
				total = N;
				break;
			}
			else if(t[i]!= 0 && t[i]+4 >= 3*p && S>0)
			{
				total++;
				S--;
			}
			else if(t[i]!= 0 && t[i]+2 >= 3*p)
			{
				total++;
			}
		}
		cout << "Case #" << line+1 << ": " << total << endl;
	}
	return 0;
}
