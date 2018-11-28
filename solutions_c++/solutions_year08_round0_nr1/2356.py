#include <cstdio>
#include <string>
#include <map>
#include <utility>
#include <set>


using namespace std;


int n,nt;
int s,q;

char temp[500];

map<string,int> mp;
string str;
set<string> v;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);


	scanf("%d",&n);

	int res;
	int i;

	int count;
	for(nt=1;nt<=n;nt++){
		res=0;

		scanf("%d\n",&s);
		mp.clear();
		for(i=0;i<s;i++){
			gets(temp);
			mp.insert(make_pair(temp,1));
		}

		scanf("%d\n",&q);

		count=1;
		v.clear();
		for(i=0;i<q;i++){
			gets(temp);
			str=string(temp);
			if(mp[str])
				v.insert(str);
			if(v.size()==s){
				++res;
				v.clear();
				v.insert(str);
			}

		}

		printf("Case #%d: %d\n",nt,res);
	}


	return 0;
}