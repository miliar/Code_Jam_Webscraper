#include<iostream>

#include<fstream>


using namespace std;

ifstream in("C.in");
ofstream out("C.out");

bool m[500][500];
int main()
{
	int T;
	in>>T;

	int R;
	int x1,x2,y1,y2;
	
	
	for(int c=0;c<T;c++)
	{
		memset(m,false,sizeof(m));
		in>>R;
		for(int i=0;i<R;i++)
		{
			in>>x1>>y1>>x2>>y2;
			for(int a=x1;a<=x2;a++)
				for(int b=y1;b<=y2;b++)
				{
					m[a][b] = true;
				}
		}

		int res = 0;

		int remain = 0;

		for(int i=0;i<200;i++)
			for(int j=0;j<200;j++)
			{
				if(m[i][j])
					remain++;

			}
		while(remain)
		{
			res++;
			for(int i=110;i>0;i--)
				for(int j=110;j>0;j--)
				{
					if(!m[i][j] && m[i-1][j] && m[i][j-1])
					{
						m[i][j] = true;
						remain++;
					}
					if(m[i][j] && !m[i-1][j] && !m[i][j-1])
					{
						m[i][j] = false;
						remain--;
					}

				}
		}
	


		out<<"Case #"<<c+1<<": "<<res<<"\n";
	}
		
	return 0;
}