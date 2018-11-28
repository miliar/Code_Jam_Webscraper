#include<iostream>
#include<fstream>
#include<string>
#include<map>
using namespace std;

bool flag[110];
string se[110];
string que[1105];
int num[1100];
int s,q;
int check(string a)
{
	int i;
	for(i=0;i<s;i++)
	{
		if(se[i]==a)return i;
	}
	return -1;
}

bool ok()
{
	int i;
	for(i=0;i<s;i++)
	{
		if(flag[i]==0)return 0;
	}
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("abcd","w",stdout);
	int test;
	cin>>test;
	int i1,i;
	int t;
	string temp;
	int k;
	int die;
	for(die=1;die<=test;die++)
	{
        cin>>s;
		getchar();
		for(i1=0;i1<s;i1++)
		{
			getline(cin,se[i1]);	
		}	
		cin>>q;
		getchar();
		k=0;
		for(i1=0;i1<q;i1++)
		{	
			getline(cin,temp);
			int tt=check(temp);
			if(tt!=-1)num[k++]=tt;
		}
		int ans=0;
		i=k-1;
		memset(flag,0,sizeof(flag));
		while(1)
		{
			if(i<0)break;
			flag[num[i]]=1;
			if(ok()&&i<k-1)
			{
				ans++;
				memset(flag,0,sizeof(flag));
				i++;
			}
			i--;
		}
		cout<<"Case #"<<die<<":"<<" "<<ans<<endl;
	}
	return 0;
}



			


