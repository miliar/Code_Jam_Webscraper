#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <iostream>
using namespace std;

//char names[100][110];

int main(){
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t,T,i;
	char line[110];
	gets(line);
	T=atoi(line);
	for(t=1;t<=T;t++){
		gets(line);
		int s=atoi(line);
		map<string,int> m;
		m.clear();
		for(i=0;i<s;i++){
			gets(line);
			m[string(line)]=1;
		}
		gets(line);
		int q=atoi(line);
		int avail=s;
		int sw=0;
		for(i=0;i<q;i++){
			gets(line);
			if(m[string(line)]==1){
				if(avail==1){
					sw++;
					for(map<string,int>::iterator p=m.begin();p!=m.end();p++)
						p->second=1;
					avail=s;
				}
				m[string(line)]=0;
				avail--;
			}
		}
		printf("Case #%d: %d\n",t,sw);
	}
	return 0;
}