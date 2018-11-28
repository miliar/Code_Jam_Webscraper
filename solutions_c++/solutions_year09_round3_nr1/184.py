#include <cstdio>
#include <map>
#include <vector>
#define MAX 70

using namespace std;

int t, ct;
char str[MAX];
map<char, int> m;
vector<int> num;
long long int final;

void goconvert(int base)
{
	final=0;
	if(base<2) base=2;
	long long int value=1;
	for(int i=num.size()-1; i>=0; i--, value*=(long long int)base)
		final+=(long long int)num[i]*value;
	printf("Case #%d: %lld\n", ct+1, final);
}

void goassign()
{
	num.clear();
	m.clear();
	m[str[0]]=1;
	num.push_back(1);
	int c=0;
	for(int i=1; str[i]; i++)
	{
		if(m.find(str[i])!=m.end())
			num.push_back(m[str[i]]);
		else
		{
			m[str[i]]=c;
			num.push_back(c);
			if(c==0) c=2;
			else c++;
		}
	}
	goconvert(c);	
}

int main()
{
	scanf("%d", &t);
	for(ct=0; ct<t; ct++)
	{
		scanf("%s", str);
		goassign();
	}
	return 0;
}