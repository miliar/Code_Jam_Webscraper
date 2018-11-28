#include<cstdio>
#include<map>
#include<string>
#include<list>
using namespace std;

void trim(string &s)
{
	while(!s.empty() && isspace(s[0]))
		s.erase(0,1);
	while(!s.empty() && isspace(s[s.size()-1]))
		s.erase(s.size()-1,1);
}

int main()
{
	int Z;
	scanf("%d",&Z);
	for(int z=1;z<=Z;++z)
	{
		printf("Case #%d: ",z);
		int n;
		list<int> v[111];
		scanf("%d\n",&n);
		map<string,int> id;
		for(int i=0;i<n;++i)
		{
			char s[111];
			fgets(s,111,stdin);
			string ss(s);
			trim(ss);
			//printf("[%s]",ss.c_str());
			id[ss]=i;
		}
		int q;
		scanf("%d\n",&q);
		//printf("q=%d\n",q);
		for(int i=0;i<q;++i)
		{
			char s[111];
			fgets(s,111,stdin);
			string ss(s);
			trim(ss);
			//printf("(%s)",ss.c_str());
			int x=id[ss];
			//printf("x=%d i=%d\n",x,i);
			v[x].push_back(i);
		}
		for(int i=0;i<n;++i)
			v[i].push_back(q);
		int ile=0;
		for(;;++ile)
		{
			int mx=-1,idmx=-1;
			for(int i=0;i<n;++i)
				if(v[i].front()>mx)
				{
					mx=v[i].front();
					idmx=i;
				}
			//printf("mx=%d idmx=%d\n",mx,idmx);
			if(mx==q)
				break;
			for(int i=0;i<n;++i)
				while(v[i].front()<mx)
					v[i].pop_front();
		}
		printf("%d\n",ile);
	}
}
