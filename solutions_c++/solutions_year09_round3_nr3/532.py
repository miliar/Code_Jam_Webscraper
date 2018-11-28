#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(int argc, char *argv[])
{
	FILE* ifp = freopen("C-small-attempt0.in","r",stdin);
	//FILE* ifp = freopen("C.in","r",stdin);
	FILE* ofp = freopen("C-small-attempt0.out","w",stdout);
	int N,Q,P,res,res_t;
	bool flag[10001];
	cin>>N;
	for(int i=0;i<N;++i)
	{
		cin>>P>>Q;
		vector<int> arr(Q);
		for(int j=0;j<Q;++j)
		{
			cin>>arr[j];
		}
		
		res = -1;
		do
		{
			memset(flag,0,sizeof(flag));
			res_t = 0;
			for(int j=0;j<arr.size();++j)
			{
				flag[arr[j]] = true;
				for(int k=arr[j]-1;k>=1;--k)
				{
					if(flag[k])
						break;
					++res_t;
				}
				for(int k=arr[j]+1;k<=P;++k)
				{
					if(flag[k])
						break;
					++res_t;
				}
			}
			if(res == -1)res = res_t;
			else
				res <?= res_t;
		}while(next_permutation(arr.begin(),arr.end()));
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}
