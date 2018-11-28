
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<string>
#include<string.h>
#include<cstring>
#include<stack>

#include<queue>
#include<cassert>

using namespace std;

#define LL long long int 
#define PII pair<int,int> 

char a[300][300],b[300][300];
vector<char> v;
int main(){
	int i,n,t,test,C,D,j;
	char x,y,z;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		scanf("%d",&C);
		for(i=1;i<=C;i++){
			scanf(" %c %c %c",&x,&y,&z);
			a[x][y]=a[y][x]=z;
		}
		scanf("%d",&D);
		for(i=1;i<=D;i++){
			scanf(" %c %c",&x,&y);
			b[x][y]=b[y][x]=1;
		}
		scanf("%d",&n);
		v.clear();
		for(i=1;i<=n;i++){
			scanf(" %c",&x);
			if(v.size()==0)
				v.push_back(x);
			else{
				if(a[v[v.size()-1]][x]!=0){
					x=a[v[v.size()-1]][x];
					v.pop_back();
					v.push_back(x);		
				}
				else{
					for(j=0;j<v.size();j++){
						if(b[v[j]][x]!=0){
							v.clear();
							break;
						}
					}
					if(v.size()!=0)
						v.push_back(x);
				}
			}
		}
		printf("Case #%d: [",test);
		if(v.size()!=0)
			printf("%c",v[0]);
		for(i=1;i<v.size();i++)
			printf(", %c",v[i]);
		printf("]\n");
	}

	return 0;
}
