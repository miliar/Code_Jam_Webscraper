/*
TASK: Rope Intranet
LANG: C++
*/

#include <iostream>
#include <map>

using namespace std;

int main(){
	int t,tt,n,i,a,b,cnt;
	map<int,int> m;
	map<int,int>::iterator it,it2,it3;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&n);
		m.clear();
		cnt=0;
		for(i=0;i<n;i++){
			scanf("%d %d",&a,&b);
			if(a<=b)
				m[a]=b-a;
			else
				m[b]=a-b;
		}
		/*for(it=m.begin();it!=m.end();it++)
		{
			printf("%d %d\n",(*it).first, (*it).second);
		}*/
		for(it=m.begin();it!=m.end();it++){
			//printf("0");
			it3=it;
			for(it2=++it3;it2!=m.end();it2++){
				//printf(":%d %d %d %d\n",(*it).first, (*it).second, (*it2).first, (*it2).second);
				if((*it).first + (*it).second < (*it2).first)
					break;
				//printf("t");
				if((*it2).second < (*it).second){
					//printf("+cnt\n");
					cnt++;
				}
				//system("pause");
			}
		}
		printf("Case #%d: %d\n",tt,cnt);
	}
	return 0;
}
