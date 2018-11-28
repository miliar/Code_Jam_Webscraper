#include <iostream>
#include <cstring>

using namespace std;

int A[128][128], B[128][128];

int main()
{
	int T,cn=1;
	cin >> T;
	while(T--)
	{
		int R;
		cin >> R;
		memset(A,0,sizeof(A));
		for(int i=0;i<R;i++)
		{
			int x1,y1,x2,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(int i=x1;i<=x2;i++) for(int j=y1;j<=y2;j++) A[i][j]=1;
		}
		int t=0, f=1;
		do
		{
			t++;
			f=0;
			memset(B,0,sizeof(B));
			for(int i=1;i<=100;i++) for(int j=1;j<=100;j++)
			{
				B[i][j]=A[i][j];
				if((A[i][j] && !A[i-1][j] && !A[i][j-1]) ||
					(!A[i][j] && A[i-1][j] && A[i][j-1])) B[i][j] = !A[i][j];
				if(B[i][j]) f=1;
			}
			memcpy(A,B,sizeof(A));
		} while(f);
		cout << "Case #" << cn << ": " << t << endl;
		cn++;
	}
	return 0;
}
