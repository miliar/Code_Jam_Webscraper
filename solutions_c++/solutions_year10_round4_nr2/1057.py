#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;
int M[2000];
bool have(int f,int t)
{
	for(int i=f;i<=t;i++)
		if(M[i]>0)
			return true;
	return false;
}
void did(int f,int t)
{
	for(int i=f;i<=t;i++)
		if(M[i]>0)
			M[i]--;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	int p;	
	int tt[11][1100];
	for(int t=1;t<=T;t++)
	{
		cin>>p;
		int xx=pow(2.0,p);
		for(int i=1;i<=xx;i++)
		{
			cin>>M[i];
			M[i]=p-M[i];
		}
		for(int i=1;i<=p;i++)
		{
			for(int j=1;j<=(int)pow(2.0,p-i);j++)
			{
				cin>>tt[i][j];
			}
		}
		int ans=0;
		for(int i=p;i>0;i--)
		{
			int len=pow(2.0,i);
			
			int start=1;
			for(int j=1;j<=pow(2.0,p-i);j++)
			{
				if(have(start,start+len-1))
				{
					did(start,start+len-1);
					ans++;
				}
				start+=len;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}