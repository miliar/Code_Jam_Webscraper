
#include<iostream>
#include<string>
using namespace std;
int solve()
{
	int n,m,i,j,ans=0,num=0;
	string s[124],f;
	bool hash[124];
	memset(hash,false,sizeof(hash));
	cin>>n;getchar();
	for(int i=0;i<n;i++)
	{
		getline(cin,s[i]);
		//cout<<s[i]<<endl;
	}
	cin>>m;getchar();
	for(i=0;i<m;i++)
	{
		getline(cin,f);
		for(j=0;j<n&&f!=s[j];j++);
		if(f!=s[j])continue;
		if(!hash[j])
		{
			hash[j]=true;
			num++;
		}
		if(num==n)
		{
			ans++;
			
			memset(hash,false,sizeof(hash));
			num=1;hash[j]=true;
		}
		//cout<<f<<endl;
	}
	return ans;
}
int main()
{

	int cas;
	cin>>cas;
	for(int ca=1;ca<=cas;ca++)
		printf("Case #%d: %d\n",ca,solve());
}
