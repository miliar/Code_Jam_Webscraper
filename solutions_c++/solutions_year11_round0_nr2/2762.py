#include <cstdio>
#include <string>
#include <set>
#include <map>

using namespace std;

string solve()
{
	int count;
	string c;
	string tmp;
	char tmpc,tmps[200];
	map<string,char> change;
	set<string> del;
	scanf("%d",&count);
	for(int i=0;i<count;i++)
	{
		scanf("%s",tmps);
		c=string(tmps);
		tmp=c.substr(0,2);
		change[tmp]=c[2];
		tmpc=tmp[0];
		tmp[0]=tmp[1];
		tmp[1]=tmpc;
		change[tmp]=c[2];
	}
	scanf("%d",&count);
	for(int i=0;i<count;i++)
	{
		scanf("%s",tmps);
		c=string(tmps);
		del.insert(c);
		tmpc=c[0];
		c[0]=c[1];
		c[1]=tmpc;
		del.insert(c);
	}
	scanf("%d",&count);
	scanf("%s",tmps);
	c=string(tmps);
	string magic,scan;
	for(int i=0;i<count;i++)
	{
		if(magic.length()>0)
		{
			scan.erase(scan.begin(),scan.end());
			scan+=c[i];
			scan+=magic[magic.length()-1];
			if(change.find(scan)!=change.end())
			{
				magic.erase(magic.length()-1);
				magic+=change[scan];
			}else{
				scan.erase(1);
				magic+=c[i];
				for(size_t k=0;k<magic.length()-1;k++)
				{
					scan+=magic[k];
					if(del.find(scan)!=del.end())
					{
						magic.erase(0,magic.length());
						break;
					}
					scan.erase(1);
				}
			}
		}else{
			magic+=c[i];
		}
	}
	int pos=0;
	while(pos+1<magic.length())
	{
		pos++;
		magic.insert(pos,", ");
		pos+=2;
	}
	return magic;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		printf("Case #%d: [%s]\n",i+1,solve().c_str());
	}
	return 0;
}
