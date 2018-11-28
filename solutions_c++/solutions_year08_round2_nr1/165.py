#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main()
{
	int T;
	cin >> T;
	for (int caso=1;caso<=T;caso++)
	{
		ll n,A,B,C,D,x0,y0,M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		vector <ll> ver (9,0);
		ver[(x0%3)*3+y0%3]++;
		for (int i=1;i<n;i++)
		{
			x0=(A*x0+B)%M;
			y0=(C*y0+D)%M;
			ver[(x0%3)*3+(y0%3)]++;
		}
		/*for (int i=0;i<9;i++)
			cout << "i:" << i << " " << ver[i] << endl; */
		ll resp=0;
		/*if (ver[0]>2)
			resp+=ver[0]*(ver[0]-1)*(ver[0]-2)/6;
		resp+=ver[0]*ver[1]*ver[2];
		resp+=ver[0]*ver[3]*ver[6];
		resp+=ver[0]*ver[4]*ver[8];
		if (ver[1]>2)
			resp+=ver[1]*(ver[1]-1)*(ver[1]-2)/6;
		resp+=ver[1]*ver[3]*ver[8];
		resp+=ver[1]*ver[4]*ver[7];
		resp+=*/
		for (int i=0;i<9;i++)
		{
			for (int j=0;j<9;j++)
			{
				for (int k=0;k<9;k++)
				{
					if ((i%3+j%3+k%3)%3==0 and (i/3+j/3+k/3)%3==0)
					{
						if (i==j and j==k)
						{
							if (ver[i]>2)
								resp+=ver[i]*(ver[i]-1)*(ver[i]-2);
						}
						else
						{
							if (i==j)
								if (ver[i]>1)
									resp+=ver[i]*(ver[i]-1)*ver[k];
							if (j==k)
								if (ver[j]>1)
									resp+=ver[j]*(ver[j]-1)*ver[i];
							if (i==k)
								if (ver[i]>1)
									resp+=ver[i]*(ver[i]-1)*ver[j];
						}
						if (i!=j and i!=k and j!=k)
							resp+=ver[i]*ver[j]*ver[k];
					}
				}
			}
		}
		cout << "Case #" << caso << ": " << resp/6 << endl;
	}
}
