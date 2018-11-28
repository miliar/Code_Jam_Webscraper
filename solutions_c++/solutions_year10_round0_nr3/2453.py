#include<iostream>
#include<fstream>
using namespace std;
ofstream outfile("res.txt", ios::out);
int T,R,K,N;
struct node
{
	int edpos;
	__int64 money;
}f[1005];
int gi[1005];

int main()
{
	while(cin>>T)
	{
		int count;
		for(count = 1; count <= T; count++)
		{
			cin>>R>>K>>N;
			int i;
			for(i = 0; i < N; i++)
			{
				cin>>gi[i];
				f[i].edpos = -1;
				f[i].money = 0;
			}
			int stpos = 0;
			__int64 res = 0;
			for(i = 0; i < R; i++)
			{
				if(f[stpos].edpos != -1)
				{	
					res += f[stpos].money;
					stpos = f[stpos].edpos;
				}
				else
				{
					int num = 0;
					int j;
					for(j = 0; j < N; j++)
					{
						num += gi[(stpos+j)%N];
						if(num > K)
						{
							num -= gi[(stpos+j)%N];
							j--;
							break;
						}
					}
					f[stpos].edpos = (stpos+j+1)%N;
					f[stpos].money = num;
					res += num;
					stpos = (stpos+j+1)%N;
				}
			}
			//cout<<"Case #"<<count<<": ";
			outfile<<"Case #"<<count<<": ";
			char str[65];
			_i64toa(res, str, 10);
			//cout<<str<<endl;
			outfile<<str<<endl;
		}
	}
	return 0;
	
}




/*
ofstream outfile("res.txt", ios::out);
int T,N,K;

int main()
{
	while(cin>>T)
	{
		int count;
		for(count = 1; count <= T; count++)
		{
			cin>>N>>K;
			__int64 cir = (1 << N);	
			outfile<<"Case #"<<count<<": ";
			if((K+1) % cir == 0)
				outfile<<"ON"<<endl;
			else
				outfile<<"OFF"<<endl;
		}
	}
	outfile.close();
	return 0;
}
*/