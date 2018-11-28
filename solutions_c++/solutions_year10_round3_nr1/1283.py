#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int, int> my_pair;
bool sort_pred(const my_pair& left, const my_pair& right)
{
return left.first < right.first;
}
int main()
{
	int tc,cases=1;
	int N;
	cin >> tc;
	while(cases <= tc)
	{
		int intersect=0;
		cin >> N;
		vector<pair<int,int>> A(N);
		for(int i=0;i<N;i++) cin >> A[i].first >> A[i].second;
		sort(A.begin(), A.end(), sort_pred);
		for(int i=0;i<N;i++)
			for(int j=i;j<N;j++)
				if(A[i].second>A[j].second) intersect++;
		cout <<"Case #" << cases<< ": " << intersect <<endl;
		cases++;
	}
	
	return 0;
}