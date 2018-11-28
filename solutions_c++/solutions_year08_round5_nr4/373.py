#include <iostream>
#include <vector>

#define mod 10007

using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int caso=1;caso<=N;caso++)
	{
		int H,W,R;
		cin >> H >> W >> R;
		vector <vector <bool> > tr (H,vector <bool> (W,false));
		vector <vector <int> > din (H, vector <int> (W,0));
		din[H-1][W-1]=1;
		for (int i=0;i<R;i++)
		{
			int r,c;
			cin >> r >> c;
			r--;c--;
			tr[r][c]=true;
		}
		for (int i=H-1;i>=0;i--)
		{
			for (int j=W-1;j>=0;j--)
			{
				if (not tr[i][j])
				{
					int a=i+2;
					int b=j+1;
					if (a<H and b<W)
					{
						din[i][j]+=din[a][b];
					}
					a=i+1;
					b=j+2;
					if (a<H and b<W)
					{
						din[i][j]+=din[a][b];
					}
					din[i][j]%=mod;
				}
			}
		}
		cout << "Case #" << caso << ": " << din[0][0] << endl;
	}
}
