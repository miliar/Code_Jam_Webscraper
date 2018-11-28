#include <map>
#include <string>
#include <iostream>
using namespace std;
map <string,int> x;
string ch;
int boo[105];
int main()
{
	char cha;
	int tot,kase,res,i,k,s,q;
	cin>>tot;
	for(kase=1;kase<=tot;kase++)
	{
		printf("Case #%d: ",kase);
		res=0;
		scanf("%d",&s);
		while(cha=getchar())
			if(cha=='\n')
				break;
		x.clear();
		for(i=1;i<=s;i++)
		{
			boo[i]=0;
			getline(cin,ch);
			x[ch]=i;
		}
		k=0;
		scanf("%d",&q);
		while(cha=getchar())
			if(cha=='\n')
				break;
		for(i=1;i<=q;i++)
		{
			getline(cin,ch);
			if(boo[x[ch]]==res)
			{
				boo[x[ch]]++;
				k++;
				if(k==s)
				{
					res++;
					k=1;
					boo[x[ch]]++;
				}
			}
		}
		printf("%d\n",res);
	}
	return 0;
}