#include <iostream>
#include <string>
#include <vector> 
using namespace std;
int main()
{
	string a,b;
	int nc;
	cin>>nc;
	int caseno = 1;
	b = "welcome to code jam";
	vector<int> arr[100];
	int n[550][50];
	int MOD = 1000;
	while(nc--)
	{
		char buff[100000];
		cin.getline(buff,50000);
		if(strcmp(buff,"")==0)
		{
			nc++;
			continue;
		}
		a = buff;
		//printf("for |%s|\n",a.c_str());
		memset(n,0,sizeof(n));
		for(int c1 = 0; c1<100; c1++)
			arr[c1].clear();
		for(int c1 = 0; c1< b.length(); c1++)
		{
			for(int c2 = 0; c2<a.length(); c2++)
			{
				if(a[c2] == b[c1])
					arr[c1].push_back(c2);
			}
		}
		
		for(int c1 = 0; c1<b.length(); c1++)
		{
			int curr = 0;
			for(int c2 = 0; c2<a.length(); c2++)
			{
				int v1=0;
				int v2 = 0;
				//n(i,j) = n(i-1,j-1) + n(i-1,j)
				if(b[c1]==a[c2])
				{
					//printf("hi %d %d\n",c1,c2);
					if(c1 ==0 && c2==0)
					{
						n[0][0] = 1;
						continue;
					}
					if(c2-1>=0 && c1-1>=0)
					{
						v1 = n[c2-1][c1-1];
					}
					else if(c2-1>=0)
					{
						v1 = 1;
					}
					if(c2-1>=0)
					{
						v2 = n[c2-1][c1];
					}
					n[c2][c1] = (v1 + v2)%MOD;
				}
				else
				{
					n[c2][c1] = n[c2-1][c1];
				}
			}
		}
		printf("Case #%d: %04d\n",caseno,n[a.length()-1][b.length()-1]);
		caseno++;
	}
	return 0;
}