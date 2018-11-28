#include <iostream>
using namespace std;

int main()
{
	int h,w,t,T,R,r,c;
	int i,j;
	cin>>T;
	for (t=1; t<=T; t++)
	{
		cin>>h>>w>>R;
		int a[100][100];
		int i,j;
		int r,c;
		for (i=0; i<h; i++)
			for (j=0; j<w; j++)
				a[i][j]=0;
		for (i=0; i<R; i++)
		{
			cin>>r>>c;
			a[r-1][c-1]=-1;
		}
		a[0][0]=1;
		for (i=0; i<h; i++)
			for (j=0; j<w; j++)
				if (a[i][j]==0)
		{
			if (i-1>=0 && j-2>=0 && a[i-1][j-2]>=0)
				a[i][j]+=a[i-1][j-2];
			if (i-2>=0 && j-1>=0 && a[i-2][j-1]>=0)
				a[i][j]+=a[i-2][j-1];
			a[i][j]%=10007;
		}
		cout<<"Case #"<<t<<": "<<a[h-1][w-1]<<endl;
	}
	return 0;
}
