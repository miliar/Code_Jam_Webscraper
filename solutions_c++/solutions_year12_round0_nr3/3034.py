#include <iostream>
#include <string.h>
#include <algorithm>
#include <string>
#include <map>
using namespace std;
int mm[105];
map <string,int> myhash;
int str2int(char *data)
{
	int len ,x;
	x = 0;
	len = strlen(data);
	for(int i=0;i<len ;i++)x = x*10 + data[i]-'0';
	return x;
}
void char2str(string &m,char*data)
{
	int len ;
	len = strlen(data);
	m.clear();
	for(int i=0;i<len;++i)
	{
		m.push_back(data[i]);
	}
}
int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	int a,b;
	int cnt;
	int len;
	int temp;
	int ans;
	string tstr;
	cnt = 0;
	char mm[30];
	char tchr[30];
	scanf("%d",&T);
	while(T--)
	{
		myhash.clear();
		++cnt;
		ans =0;
		scanf("%d%d",&a,&b);
		for(int i = a; i <=b ; ++i)
		{
			memset(mm,0,sizeof(mm));
			sprintf(mm,"%d",i);
			len = strlen(mm);
			for(int j =0; j< len -1 ; ++j)
			{
				mm[len+j]=mm[j];
				temp = str2int(mm+j+1);
				if(temp > i && temp >= a && temp <= b)
				{
					sprintf(tchr,"%d$%d\n",i,temp);
					char2str(tstr,tchr);
					if(myhash.find(tstr) == myhash.end())
					{
						myhash[tstr]=1;
						++ans;
					}
				}
			}
		}
		printf("Case #%d: %d\n",cnt,ans);
	}
}