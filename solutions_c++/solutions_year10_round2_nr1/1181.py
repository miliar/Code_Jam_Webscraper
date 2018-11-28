#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
struct dir{
string name;
vector<dir>son;
};
dir root;
void display(dir a){
cout<<a.name<<endl;
for(int i=0;i<a.son.size();i++)
display(a.son[i]);
}
int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	int N,M;
	char path[101];
	char dirname[101];
	dir* previous;
	dir tmp;
	int len;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		root.son.clear();
		scanf("%d%d\n",&N,&M);
		for(int t=0;t<N;t++)
		{
			scanf("%s",path);
			len=0;
			previous=&root;
			for(int i=1;i<=strlen(path);i++)
			{
				if(path[i]=='/'||path[i]=='\0'){
					dirname[len]='\0';
					len=0;
					int j;
					for(j=0;j<previous->son.size();j++)
					{
						if(dirname==previous->son[j].name){
						break;
						}
					}
					if(j==previous->son.size()){
						tmp.name=dirname;
						tmp.son.clear();
					previous->son.push_back(tmp);
					}
					previous=&(previous->son[j]);
				}
				else{
				dirname[len++]=path[i];
				}
			}
		}
//display(root);
		int ans=0;
		for(int t=0;t<M;t++)
		{
			scanf("%s",path);
			len=0;
			previous=&root;
			for(int i=1;i<=strlen(path);i++)
			{
				if(path[i]=='/'||path[i]=='\0'){
					dirname[len]='\0';
					len=0;
					int j;
					for(j=0;j<previous->son.size();j++)
					{
						if(dirname==previous->son[j].name){
						break;
						}
					}
					if(j==previous->son.size()){
						tmp.name=dirname;
						tmp.son.clear();
					previous->son.push_back(tmp);
					ans++;
					}
					previous=&(previous->son[j]);
				}
				else{
				dirname[len++]=path[i];
				}
			}
		}
			printf("%d\n",ans);
		fflush(stdout);
	}
	return 0;
}
