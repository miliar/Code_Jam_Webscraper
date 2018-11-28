#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <sstream>
#include <cstdio>

#pragma comment(linker, "/STACK:16777216")
using namespace std;


bool p[20000];

char* chb(int num, int base)
{
	char* ret = new char[50];
	int i = 0;
	do
	{
		ret[i++] = '0' + num%base;
		num/=base;
	}while (num);
	ret[i] = '\0';
	for(int j = 0; j < i/2; ++j)
		swap(ret[j],ret[i-j-1]);
	return ret;
}


int ok(int num, int base)
{
	if(num<20000)
	{
		if(num == 1)
			return true;
		if(p[num])
			return false;
		p[num] = true;
	}
	char* n = chb(num,base);
	num = 0;
	for(int i = 0; i < strlen(n); ++i)
		num += (n[i]-'0')*(n[i]-'0');
	return ok(num,base);
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("A-small-output.out","w",stdout);
	int t,k;
	int ans;
	char tox[100];
	cin>>t;
	int base[4];
	int i,j;
	for(k = 1; k <= t; k++)
	{
		gets(tox);
		//cin.getline(tox,100);
		if(strcmp(tox,"\n")==0 || strcmp(tox,"")==0)
		{
			k--;
			continue;
		}
		stringstream kardal(tox);
		i = 0;
		while(kardal>>base[i])
			i++;
		for(ans = 2; ;++ans)
		{
			for(j = 0; j < i; ++j)
			{
				memset(p,false,sizeof(p));
				if(!ok(ans,base[j]))
					break;
			}
			if(j == i)
				break;
//			cerr<<ans<<endl;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}

