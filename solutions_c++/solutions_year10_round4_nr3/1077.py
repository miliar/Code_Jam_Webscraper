#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <map>
#include<set>
using namespace std;
int test,Test;
int main(){
	int i,j,x1,y1,x2,y2,x,y,k,count=0;
	scanf("%d",&Test);
	for (test=1;test<=Test;test++){
		printf("Case #%d: ",test);
		fprintf(stderr,"%d/%d\n",test,Test);
		scanf("%d",&k);
		set<pair<int,int> > s1;
		for (i=0;i<k;i++){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (x=x1;x<=x2;x++)
			for (y=y1;y<=y2;y++)
			s1.insert(make_pair(x,y));
		}
		for (j=0;!s1.empty();j++){
			//printf("%d:\n",j);
			set<pair<int,int> > s2;
			for (set<pair<int,int> >::iterator it=s1.begin();it!=s1.end();it++){
				x=it->first;
				y=it->second;
			//	printf("%d %d\n",x,y);
				//if ((s1.find(make_pair(x,y-1))!=s1.end())||(s1.find(make_pair(x-1,y))!=s1.end))
				if ((s1.find(make_pair(x,y-1))!=s1.end())||(s1.find(make_pair(x-1,y))!=s1.end()))
				s2.insert(make_pair(x,y));
				if (s1.find(make_pair(x-1,y+1))!=s1.end())
				s2.insert(make_pair(x,y+1));
			}
			swap(s1,s2);
		}
		printf("%d\n",j);
	}
  return 0;
}
