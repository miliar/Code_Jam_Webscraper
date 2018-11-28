#include <stdio.h>
#include <set>
#include <string>
#include <vector>

using namespace std;

int L,D,N;
set<string> allowed;
string inp;
string cur[50];
int ans;
void go(int pos, string last)
{
	if (pos>=L)
	{
		ans++;
		return;
	}
	int i;
	for (i=0; i<cur[pos].length(); i++)
	{
		string nextlast=last;
		nextlast+=cur[pos][i];
		if (allowed.count(nextlast)==0)
			continue;
		go(pos+1,nextlast);
	}
}
char data[3000000];

int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.outx","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d %d %d", &L,&D,&N);
	int i,j;
	allowed.clear();
	for (i=0; i<D; i++)
	{
		scanf("%s", data);
		string d=data;
		string d2="";
		for (j=0; j<d.length(); j++)
		{
			d2+=d[j];
			allowed.insert(d2);
		}
	}
	for (i=0; i<N; i++)
	{
		scanf("%s",data);
		inp=data;
		int pos=0;
		for (j=0; j<L; j++)
		{
			if (inp[pos]=='(')
			{
				int until=inp.find(")",pos);
				string xx=inp.substr(pos+1,until-(pos+1));
				cur[j]=xx;
				pos=until+1;
			}
			else
			{
				string xx="";
				xx+=inp[pos];
				cur[j]=xx;
				pos++;
			}
		}
		ans=0;
		go(0,"");
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
