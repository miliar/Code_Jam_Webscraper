#include<iostream>
using namespace std;

char datain[60][60];

int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		int R,C;
		cin>>R>>C;
		for(int j=0;j<R;++j)
		{
			cin>>datain[j];
		}
		int totalSharp=0;
		for(int j=0;j<R;++j)
		{
			for(int t=0;t<C;++t)
			{
				if(datain[j][t]=='#')
				{
					++totalSharp;
				}
			}
		}
		int totalChange=0;
		if(totalSharp%4==0)
		{
			for(int row=0;row<R-1;++row)
			{
				for(int col=0;col<C-1;++col)
				{
					if(datain[row][col]=='#')
					{
						if(datain[row][col+1]=='#'&&datain[row+1][col]=='#'&&datain[row+1][col+1]=='#')
						{
							++totalChange;
							datain[row][col]='/';
							datain[row][col+1]='\\';
							datain[row+1][col]='\\';
							datain[row+1][col+1]='/';
						}
					}
				}
			}
			if(totalChange==totalSharp/4)
			{
				printf("Case #%d:\n",i);
				for(int row=0;row<R;++row)
				{
					cout<<datain[row]<<endl;
				}
			}
			else
			{
				printf("Case #%d:\nImpossible\n",i);
			}
		}
		else
		{
			printf("Case #%d:\nImpossible\n",i);
		}

	}
	return 0;
}