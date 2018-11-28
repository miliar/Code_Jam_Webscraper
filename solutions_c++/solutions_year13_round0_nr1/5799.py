#include  <iostream>
using namespace std;

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T;
	cin >> T;

	for (int k=1;k<=T;k++)
	{
		bool flag=true;
		int A[4][4]={-1};
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				char tmp;
				cin >> tmp;
                switch (tmp)
                {
                    case 'X':
                        A[i][j]=1;
                        break;
                    case 'O':
                        A[i][j]=10;
                        break;
                    case '.':
                        flag=false;
						A[i][j]=-1;
                        break;
                    case 'T':
                        A[i][j]=0;
                        
                        break;
                }

			}
		}
		int sum[10]={0};
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				sum[i]+=A[i][j];
			}
		}
		for (int i=0;i<4;i++)
		{
			for (int j=0;j<4;j++)
			{
				sum[i+4]+=A[j][i];
			}
		}
		for (int i=0;i<4;i++)
		{
			sum[8]+=A[i][i];
			sum[9]+=A[i][3-i];
		}
		cout << "Case #"<<k<<": ";
		bool flag1=true;
		for (int i=0;i<10;i++)
		{
			if (sum[i]==3 || sum[i]==4) {cout << "X won"<<endl;flag1=false;break;}
			if (sum[i]==30 || sum[i]==40) {cout << "O won"<<endl;flag1=false;break;}
		}
		if (flag1)
		{
			if (flag1) cout << "Draw"<<endl;
			else cout << "Game has not completed"<<endl;
		}
	}
	return 0;
}