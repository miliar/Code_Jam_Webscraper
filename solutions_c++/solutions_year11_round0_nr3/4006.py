#include<iostream>
using namespace std;
int candy[15];
bool used[15];
int T;
int n;
int total;
int totalNum;
int res;

int max(const int & a, const int & b,const int & c)
{
	int tmp;
	tmp=a>b?a:b;
	tmp=tmp>c?tmp:c;
	return tmp;
}
void dfs(int pos,int cur)
{
	//if(pos>n) return;
	if(pos==n)
	{
		if( (cur) && (cur == (total^cur)) )
		{
			int num=0;
			for(int i=0;i<n;i++)
				if(used[i])
					num+=candy[i];
			res=max(num,totalNum-num,res);
		}
		return;
	}
		
	//use candy[pos]
	used[pos]=1;
	dfs(pos+1,cur^candy[pos]);
	

	//don't use candy[pos]
	used[pos]=0;
	dfs(pos+1,cur);
}
int main()
{
	freopen("small","r",stdin);		
	freopen("smalloutput","w",stdout);
	
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n;
		total=totalNum=0;
		res=0;
		memset(used,0,sizeof(used));
		for(int i=0;i<n;i++)
		{
			cin>>candy[i];
			total ^= candy[i];
			totalNum += candy[i];
		}
		cout<<"Case #"<<t<<": ";
		dfs(0,0);
		if(res)
			cout<<res<<endl;
		else
			cout<<"NO"<<endl;
	}
}