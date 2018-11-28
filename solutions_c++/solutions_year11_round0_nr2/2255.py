
/*Paresh Verma*/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<cstring>
#include<cmath>
#include<list>
#include<map>

#define pub push_back
#define pob pop_back
#define pp pair<char,char>

using namespace std;

int main(){
	int i,j,k,l,m,T;
	pp t;
	int c,d,n;
	char s[105],z;
	scanf("%d",&T);
	map<pp,char> com;
	map<pp,char> cle;
	map<pp,char>::iterator it;

	list<char> ele;
	list<char>::iterator lit;
	for(int p=1; p<=T; p++){
		com.clear();
		cle.clear();
		ele.clear();
		scanf("%d",&c);
		for(i=0;i<c;i++){
			scanf("%s",s);
			t.first=s[0]; t.second=s[1];
			com[t]=s[2];
			t.first=s[1]; t.second=s[0];
			com[t]=s[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;i++){
			scanf("%s",s);
			t.first=s[0]; t.second=s[1];
			cle[t]=s[2];
			t.first=s[1]; t.second=s[0];
			cle[t]=s[2];
		}
//		for(it=com.begin(); it!=com.end(); it++){
//			cout << (it->first).first<< (it->first).second << " " << it->second<<endl;
//		}
		scanf("%d",&n);
		scanf("%s",s);
		for(i=0;i<n;i++){
			if(ele.empty()){
				ele.push_back(s[i]);
			}
			else{
				z=s[i];
				while(1){
					t.first=z; t.second=ele.back();
					it = com.find(t);
					if(it!=com.end()){
						ele.pop_back();
						z=(it->second);
					}
					else
						break;
				}
				int flag=1;
				for(lit = ele.begin(); lit!=ele.end(); lit++){
					t.first = z; t.second=*lit;
					it=cle.find(t);
					if(it!=cle.end()){
						flag=0;
						ele.clear();
						break;
					}
				}
				if(flag)
					ele.push_back(z);
			}
		}
		printf("Case #%d: [",p);
		for(lit = ele.begin(); lit!=ele.end(); lit++){
			if(lit==ele.begin())
				printf("%c",*lit);
			else
				printf(", %c",*lit);
		}
		printf("]\n");
	}
	return 0;
}
