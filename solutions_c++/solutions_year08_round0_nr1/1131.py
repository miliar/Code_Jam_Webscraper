#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

int main(){
	int tt; scanf("%d",&tt);
	string tmp;

	for (int ti=1;ti<=tt;ti++){
		int S; scanf("%d",&S);
		getline(cin,tmp);
		map<string,int> Map;
		for (int i=1;i<=S;i++){
			getline(cin,tmp);
			Map[tmp] = i;
		}
		int Q; scanf("%d",&Q);
		getline(cin,tmp);
		int q[Q];
		for (int i=0;i<Q;i++){
			getline(cin,tmp);
			q[i] = Map[tmp];
		}
/*
		for (int i=0;i<Q;i++)printf("%d ",q[i]); 
		puts("");
*/
		//process
		int cnt=0,ans=0;
		bool b[Q+1]; memset(b,0,sizeof(b));
		for (int i=0;i<Q;i++){
			//printf("~ %d: %d %d\n",i,q[i],cnt);
			if (b[q[i]])continue;
			if (cnt==S-1){
				ans++; cnt=0;
				memset(b,0,sizeof(b));
			}
			cnt++;
			b[q[i]]=true;

		}
		printf("Case #%d: %d\n",ti, ans);


	}

	return 0;
}
