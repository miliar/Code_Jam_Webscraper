#include <iostream>
#include <string>
using namespace std;
string st[103];
int qur[1003];
bool mk[103];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	string temp;
    int n,s,q,i,j,k,ans,d;
	cin>>n;
	//cout<<n<<endl;
	for(k=1;k<=n;k++)
	{
		ans=0;
		cin>>s;
		//cout<<s<<endl;
		getchar();
		for(i=1;i<=s;i++)getline(cin,st[i]);//cout<<st[i]<<endl;}
		cin>>q;
		//cout<<q<<endl;
		getchar();
		for(i=1;i<=q;i++)
		{
			getline(cin,temp);
			//cout<<temp<<endl;
			for(j=1;j<=s;j++)
				if(st[j]==temp)qur[i]=j;
		}
		d=1;
	    for(j=1;j<=s;j++)mk[j]=0;
		for(i=1;i<=q;i++)
		{
			mk[qur[i]]=1;
			for(j=1;j<=s;j++){
				if(mk[j])continue;else break;}
		    if(j==s+1)
			{
				i--;
			    for(j=1;j<=s;j++)mk[j]=0;
				ans++;
			}
		}
		cout<<"Case #"<<k<<":"<<" "<<ans<<endl;
	}
        return 0;
}