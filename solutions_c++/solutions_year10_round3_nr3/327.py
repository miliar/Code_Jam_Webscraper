#include <iostream>
using namespace std;

char map[64][64];
int T,N,M;
char str[64];
int val[256];
bool used[64][64];
int sizes[64];

bool test(int x,int y,int sz)
{
	if(x+sz>M+1 || y+sz>N+1) return false;
	for(int i=x;i<x+sz;i++)
	{
		for(int j=y;j<y+sz;j++)
		{
			if(used[i][j] || (i+1<x+sz && map[i][j]==map[i+1][j]) || (j+1<y+sz && map[i][j]==map[i][j+1]) ) return false;	
		}	
	}	
	return true;
}

void use(int x,int y,int sz)
{
	for(int i=x;i<x+sz;i++)
	{
		for(int j=y;j<y+sz;j++)
		{
			used[i][j]=1;
		}	
	}	
}
int main()
{
	val['1']=1;
	val['2']=2;
	val['3']=3;
	val['4']=4;
	val['5']=5;
	val['6']=6;
	val['7']=7;
	val['8']=8;
	val['9']=9;
	val['A']=10;
	val['B']=11;
	val['C']=12;
	val['D']=13;
	val['E']=14;
	val['F']=15;
	
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>M>>N;
		memset(map,0,sizeof(map));
		memset(str,0,sizeof(str));
		memset(used,0,sizeof(used));
		memset(sizes,0,sizeof(sizes));
		for(int i=1;i<=M;i++)
		{
		//	cout<<i<<endl;
			memset(str,0,sizeof(str));
			cin>>str;
			int cnt=0;
			for(int j=0;str[j]!=0;j++)
			{
				int t = val[str[j]];
			//	cout<<t<<"-";
				map[i][++cnt] = ((t&(1<<3))	>>3);
				map[i][++cnt] = ((t&(1<<2))	>>2);
				map[i][++cnt] = ((t&(1<<1))	>>1);
				map[i][++cnt] = (t&1);
			}	
		}
		
		bool found = 0;
		do
		{
			found = false;
			pair<int,int> pos;
			int maxsz=0;
			for(int i=1;i<=M;i++)
			{
				for(int j=1;j<=N;j++)
				{
					int sz=1;
				 
						while(test(i,j,sz))
						{
								if(sz>maxsz)
								{
									pos=make_pair(i,j);
									maxsz=sz;	
								}
								sz++;
						}
			 
				}
			}	
			
			if(maxsz!=0)
			{
			//	cout<<pos.first<<" "<<pos.second<<" "<<maxsz<<endl;
				 found=true;
				 sizes[maxsz]++;
				 use(pos.first,pos.second,maxsz);
			}
		
			
		}
		while(found);
		
		int cnt=0;
		for(int i=1;i<64;i++)
			if(sizes[i]) cnt++;
		cout<<"Case #"<<t<<": "<<cnt<<endl;
		for(int i=64;i>0;i--)
			if(sizes[i]) cout<<i<<" "<<sizes[i]<<endl;
		
	}
	
}
