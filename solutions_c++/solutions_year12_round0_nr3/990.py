#include <fstream>
#include <string>

using namespace std;
ifstream fin("input.in");
ofstream fout("output.out");


int main()
{
	int t;
	long a ,b;
	long added[10],cur;
	long long ans;
	long index[8];
	int *calculated;

	calculated=new int[2000005];
	fin>>t;
	index[0]=1;
	for (int i=1;i<8;i++) index[i]=index[i-1]*10;

	for (int i=1;i<=t;i++)
	{
		fin>>a>>b;
		long temp,ls,new_num,left,right;
	
		memset(&calculated[a],0,sizeof(int)*(b-a+1));
		ans=0;

		for (temp=a;temp<b;temp++)
		{
			if (calculated[temp]>0) continue;
			int len=0;
			ls=temp;
			while (ls>0)
			{
				ls/=10;
				len++;
			}

			cur=0;
		
		
			for (int j=1;j<len;j++)
			{
				left=temp/index[j];
				right=temp-left*index[j];
				new_num=right*index[len-j]+left;
				if (new_num>temp && new_num<=b)
				{
					if (cur==0)
					{
						added[cur++]=new_num;
						calculated[new_num]=1;
						//ans++;
					}
					else 
					{
						int k;
						for (k=0;k<cur;k++)
							if (added[k]==new_num) break;
						if (k>=cur)
						{
							added[cur++]=new_num;
							calculated[new_num]=1;
						  //  ans++;
						}
					}
				}

			}
			ans+=(cur+1)*cur/2;
		}

		fout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
