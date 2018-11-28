#include "iostream"
#include "cstdio"
#include "vector"
#include "algorithm"
using namespace std;
vector <int> a;
int main()
{
	int T,N;
	int i,j;
	int tmp,nMax;
	int sum,nSum;
	freopen("test.txt","r",stdin);
	freopen("C-large.out","w",stdout);
	cin>>T;
	for(int caseID = 1; caseID <= T; caseID++)
	{
		nMax = 0;
		sum = 0;
		nSum = 0;
		a.clear();
		cin>>N;
		for(i = 0; i < N; i++)
		{
			cin>>tmp;
			a.push_back(tmp);
			sum = sum^tmp;
			nSum += tmp;
		}
		sort(a.begin(),a.end());
		if(sum == 0)
			nMax = nSum - a.front();
		else
			nMax = 0;
		cout<<"Case #"<<caseID<<": ";
		if(nMax == 0)
			cout<<"NO";
		else
			cout<<nMax;
		if(caseID != T)
			cout<<endl;
	}
	return 0;
}