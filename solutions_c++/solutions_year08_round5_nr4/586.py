#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<queue>
#include<map>
#include<set>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
#define Pi acos(-1.0)
#define Eps (1e-9)
#define pb push_back
#define mp make_pair
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define sqr(a) ((a)*(a))
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
int arr[105][105];
int main()
{
	freopen("F.in","r",stdin);
	freopen("F.out","w",stdout);
	int T,ind=0;
	cin>>T;

	while(T)
	{
		T--;
		ind++;
		int W,H,N;
		cin>>H>>W>>N;
		memset(arr,0,sizeof(arr));
		int i;
		for(i=0;i<N;i++)
		{
			int r,c;
			cin>>r>>c;
			arr[r][c]=-1;
		}
		arr[1][1]=1;
		for(i=1;i<=H;i++)
			for(int j=1;j<=W;j++)
			{
				if(i==j && i==1)continue;
				if(arr[i][j]==-1)continue;
				if(i>1 && j>2 && arr[i-1][j-2]!=-1)arr[i][j]+=arr[i-1][j-2];
				if(j>1 && i>2 && arr[i-2][j-1]!=-1)arr[i][j]+=arr[i-2][j-1];
				arr[i][j]%=10007;
			}
		cout<<"Case #"<<ind<<": "<<arr[H][W]<<endl;
	}
	return 0;
}

