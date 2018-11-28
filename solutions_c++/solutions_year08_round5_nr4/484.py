#include <iostream>
#include <algorithm>
using namespace std;

const int MOD = 10007;

const int MX = 150;
long long xcnt[MX][MX];
bool bEvil[MX][MX];

int main()
{
	int n;
	cin>>n;
	for(int t=1;t<=n;++t)
	{
		int H,W,R;
		cin>>H>>W>>R;
		memset(bEvil,0,sizeof bEvil);
		memset(xcnt,0,sizeof xcnt);
		for(int i=0;i<R;++i){
			int r,c;
			cin>>r>>c;
			bEvil[r][c] = true;
		}

		xcnt[1][1] = 1;
		for(int i=1;i<=H;++i){
			for(int j=1;j<=W;++j){
				if(bEvil[i][j])
					continue;
				xcnt[i][j] %= MOD;
				int nr = i+1,
					nc = j+2;
				if( nr<=H && nc <= W)
					xcnt[nr][nc] += xcnt[i][j];
				nr = i+2;
				nc = j+1;
				if( nr<=H && nc <= W)
					xcnt[nr][nc] += xcnt[i][j];
			}
		}
		cout<<"Case #"<<t<<": ";
		cout<<xcnt[H][W]<<endl;
	}
}

