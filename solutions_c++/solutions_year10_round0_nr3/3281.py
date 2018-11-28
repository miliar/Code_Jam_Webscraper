#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;


int main()
{

	ifstream ifile("C-small-attempt2.in");
	ofstream ofile("C-small-attempt2.in-out.txt");
	//ifstream ifile("test.txt");
	//ofstream ofile("test-out.txt");
	
	int times;//小于50个案例

	long r;//一天跑这些圈
	long n;//组数
	long k; //最大限乘
	long i,j;//一共n组。
	long f[11];
	long t[11];
	long h[11];//从f[1]记到f[n],h[n]记录重量
	long score=0;
	
	ifile>>times;
	
	for (i=0;i<times;i++)
	{
		//n devices,and k knock times 
		ifile>>r>>k>>n;
		//读入每组数据,每组有多少个
		long sum =0;
		for (j=1;j<=n;j++)
		{
			ifile>>f[j];
			sum+=f[j];
		}
		if (sum<=k)
		{
			ofile<<"Case #" <<i+1<<": "; 
			
			ofile<<sum*r<<endl;
		}
		else
		{
			//初始化辅助数据
			for (j=1;j<=n;j++)
			{
				//f[n]记录取几个，h[n]记录从n开始要拿几个
				if (j==1)
				{
					t[j]=1; //从j组一直拿到t[j]组
					h[j]=f[j];
					while(h[j]+f[(t[j])%n+1]<=k)
					{
						t[j]=(t[j])%n+1;
						h[j] = h[j]+f[t[j]];
					}
				}
				else
				{
					if (t[j-1]<j)
					{
						t[j]=j;
						h[j]=f[j];
					}
					else
					{
						t[j]=t[j-1];
						h[j]=h[j-1]-f[j-1];
					}
					while (h[j]+f[t[j]%n+1]<=k)
					{
						t[j]=(t[j])%n+1;
						h[j] = h[j]+f[t[j]];
					}
				}
				
			}
			
			score =0;
			long cur =1;
			for (j=1;j<=r;j++)//一共这么多圈
			{
				score += h[cur];
				cur = t[cur]%n+1;
			}
			
			
			ofile<<"Case #" <<i+1<<": "; 
			
			ofile<<score<<endl;

		}
	
			
	}
	return 0;
	
}


