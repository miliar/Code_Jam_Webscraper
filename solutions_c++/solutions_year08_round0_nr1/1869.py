#include<iostream>
#include<map>
#include<string>
using namespace std;
main()
{
      int t,cas;
      cin>>t;
      map<string,int> nameno;
      cas=1;
      while(t--)
      {
       int n;
       cin>>n;
//       cout<<n;
       int i;
       string a;
       nameno.clear();
       int flags[101];
       memset(&flags,0,sizeof(flags));
       
       for(i=0;i<=n;i++)
       {
        fflush(stdin);
        getline(cin,a,'\n');
        //cout<<a<<endl;
	if(i==0)
	continue;
        nameno.insert(pair<string,int> (a,i));
       }
       int q;
       cin>>q;
       int cnt=0,ans=0;
       
       for(i=0;i<=q;i++)
       {
        fflush(stdin);
	getline(cin,a,'\n');
        //cout<<a;
	if(i==0)
	continue;
	int now=nameno.find(a)->second;
        //cout<<now<<endl;
        if(flags[now]==0)
        {
         cnt++;
         flags[now]=1;
        }
        if(cnt==n)
        {
         ans++;
         memset(&flags,0,sizeof(flags));
         flags[now]=1;
         cnt=1;
        }
       }
       cout<<"Case #"<<cas<<": "<<ans<<endl;
       cas++;
      }
}
