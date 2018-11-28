#include<iostream>
#include<string>
#include<map>
using namespace std;
#define height 1001
#define length 101
int s,q,n,ans,a[length];
bool m[height][length];
//char site[length][101],query[height][101];
map<string,int> hash;
string site[length],query[height];

void f()
{
	
	int start,i,j,best,totel;
	for(start=1; ;start=start+a[best])
	{
		if(start>q)  return;
		else ans++;
		totel=0;
		memset(a,0,sizeof(a));
		for(i=1;i<=s;i++)
		{
			for(j=start;j<=q;j++)
			{
				if(m[j][i]==false)  a[i]++;
				else break;
			}
			if(a[i]>totel)
			{
				totel=a[i];
				best=i;
			}
		}
	}
}
		
		
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int i,j,cases;
	cin>>n;
	for(cases=1;cases<=n;cases++)
	{
		memset(m,false,sizeof(m));
		cin>>s;
		getchar();
		for(i=1;i<=s;i++)
		{
			getline(cin,site[i]);
			hash[site[i]]=i;
		}
		cin>>q;
		getchar();
		for(i=1;i<=q;i++)
		{
			getline(cin,query[i]);
			m[i][ hash[query[i]] ]=true;
		}
		ans=0;
		f();
		cout<<"Case "<<"#"<<cases<<": ";
		if(ans>0) 
			cout<<ans-1<<endl;
		else
			cout<<0<<endl;
	}
	system("pause");
	return 0;
}



