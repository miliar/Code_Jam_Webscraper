#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <set>

int main(void)
{
	freopen("magicka.in","r",stdin);

	int tests;
	std::cin>>tests;
	for (int z=0; z<tests; z++)
	{
		std::map<char, std::map<char,char> > convert;
		std::map<char, std::map<char,bool> > oppose;

		int rules;
		std::cin>>rules;
		for (int i=0; i<rules; i++)
		{
			std::string r;
			std::cin>>r;
			convert[r[0]][r[1]]=
			convert[r[1]][r[0]]=r[2];
		}
		std::cin>>rules;
		for (int i=0; i<rules; i++)
		{
			std::string r;
			std::cin>>r;
			oppose[r[0]][r[1]]=
			oppose[r[1]][r[0]]=1;
		}

		int wl;
		std::cin>>wl;

		std::string invoke;
		std::cin>>invoke;

		int i,p;
		std::string val; val.resize(invoke.size());
		for (i=0,p=0; i<wl; i++)
		{
			val[p]=invoke[i];

			if (p>0 && convert.find(val[p-1])!=convert.end() && convert[val[p-1]].find(val[p])!=convert[val[p-1]].end())
			{
				char dst=convert[val[p-1]][val[p]];
				val[p-1]=dst;
				p--;
			}

			bool dead=0;
			for (int j=0; j<p; j++)
				if (oppose.find(val[j])!=oppose.end() && oppose[val[j]].find(val[p])!=oppose[val[j]].end() && oppose[val[j]][val[p]]==1)
				{
					p=0;
					dead=1;
					break;
				}
			if (!dead)
				p++;
		}
		val.resize(p);
		std::cout<<"Case #"<<z+1<<": [";
		for (int i=0; i<p-1; i++)
			std::cout<<val[i]<<", ";
		if (p)
			std::cout<<val[p-1];
			std::cout<<"]"<<std::endl;
	}
}
