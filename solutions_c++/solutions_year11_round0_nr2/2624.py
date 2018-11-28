#include <iostream>
#include <string>
using namespace std;

int A,T,len,ch;
string s,buf,ret;
int g[505][505],h[505][505];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	cin>>T;
	for (int Te=1;Te<=T;++Te)
	{
		cin>>A;
		ret.clear();
		memset(g,0,sizeof(g));
		memset(h,0,sizeof(h));
		for (int i=0;i<A;++i)
		{
			cin>>buf;
			g[buf[0]][buf[1]]=g[buf[1]][buf[0]]=buf[2];
		}
		cin>>A;
		for (int i=0;i<A;++i)
		{
			cin>>buf;
			h[buf[0]][buf[1]]=h[buf[1]][buf[0]]=-1;
		}
		cin>>len>>s;
		for (int i=0;i<len;++i)
		{
			ret+=s[i];
			if (ret.size()<2)	continue;
			ch=g[ret[ret.size()-1]][ret[ret.size()-2]];
			if (ch>0)	ret.erase(ret.size()-2,2),ret+=(char)ch;
			for (int i=0;i<ret.size()-1;++i)
			if (h[ret[i]][ret[ret.size()-1]]<0)	{ret.clear();break;}
		}
		cout<<"Case #"<<Te<<": [";
		for (int i=0;i<ret.size();++i)
		{
			if (i)	cout<<", ";
			cout<<ret[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}
