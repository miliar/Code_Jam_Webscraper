#include<iostream>
#include<fstream>
using namespace std;

int n,c[1010];
bool flag;

int cmp(const void *a,const void *b)
{
	return *(int *)a-*(int *)b;
}

void dfs(int ste,int &res, int pat,int &cnt)
{
	if(flag) return ;
	if(ste<0)
	{
		if(res==pat&&res!=0)
		{
			flag=true;
			return ;
		}
		return ;
	}
	res=res^c[ste];
	cnt+=c[ste];
	dfs(ste-1,res,pat,cnt);
	if(flag) return ;
	res=res^c[ste];
	cnt-=c[ste];
	pat=pat^c[ste];
	dfs(ste-1,res,pat,cnt);
}

int main()
{
	int t,i,k=0,ans,test,cnt;
	ifstream cin("C-large.in");
	ofstream cout("C-large.out");
	cin>>t;
	while(t--)
	{
		cin>>n;
		test=0;
		flag=0;
		for(i=0;i<n;++i)
		{
			cin>>c[i];
			test=test^c[i];
		}
		if(test!=0)
		{
			cout<<"Case #"<<++k<<": NO"<<endl;
			continue;
		}
		qsort(c,n,sizeof(int),cmp);
		ans=0;
		cnt=0;
		dfs(n-1,ans,0,cnt);
		cout<<"Case #"<<++k<<": "<<cnt<<endl;
	}

    return 0;
}
