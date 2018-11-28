#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int main()
{
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	int n;
	dat >> n;
	for(int t=0;t<n;t++)
	{
		int mas[257]={0};
		char num[257]={0};
		dat >> num;
		int kol=0,i,j,m=strlen(num);
		for(i=0;i<m;i++)
		{
			if (mas[num[i]]==0)
			{
				kol++;
				mas[num[i]]=1;
			}
		}
		int curl=0;
		int ans[257]={0};
		int arr[257]={0};
		bool used[257]={0};
		arr[num[0]]=1;
		used[num[0]]=true;
		ans[0]=1;
		for(i=1;i<m;i++)
		{
			if (used[num[i]])
			{
				ans[i]=arr[num[i]];
			}
			else
			{
				ans[i]=curl;
				arr[num[i]]=curl;
				used[num[i]]=true;
				if (curl==0) curl++;
				curl++;
			}
		}
//		for(i=0;i<m;i++)
//			sol << ans[i] << "	";
//		sol << endl;
		long long ans1=0,curs=1;
		if (kol==1) kol=2;
		for(i=m-1;i>=0;i--)
		{
			ans1+=curs*ans[i];
			curs*=kol;
		}
		sol << "Case #" << t+1 << ": " << ans1 << endl;
	}
	return 0;
}