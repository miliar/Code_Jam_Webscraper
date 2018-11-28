#include <iostream>
#include <map>
#include <string>
using namespace std;


int main()
{
	freopen("A-large.out","w",stdout);
	freopen("A-large.in","r",stdin);

	int flag[120], pc;
	map<string,int> mymap;
	int T,K,i,s,q,ans;
	char  temp[110];
	int x;


	scanf("%d",&T);
	for(K=1;K<=T;K++){
		scanf("%d\n",&s);
		mymap.clear();

		for(i=0;i<s;i++){
			gets(temp);
			mymap[temp]=i;
		}
		scanf("%d\n",&q);


		pc=0;
		ans=0;
		memset(flag,0,sizeof(flag));

		for(i=0;i<q;i++){
			gets(temp);
		
			if (mymap.find(temp)!=mymap.end()){
				x=mymap[temp];
				if (flag[x]==0){
					flag[x]=1;
					pc++;
					if (pc==s){
						ans++;
						memset(flag,0,sizeof(flag));
						flag[x]=1;
						pc=1;
					}
				}
			}
		}
		printf("Case #%d: %d\n",K,ans);

	}
	return 0;
}
