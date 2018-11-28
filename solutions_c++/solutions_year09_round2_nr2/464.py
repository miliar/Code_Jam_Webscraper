
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		char buf[1000];scanf("%s",buf);
		int len=strlen(buf);
		bool ret=next_permutation(buf,buf+len);
		
		static int npr=1;
		printf("Case #%d: ",npr++);
		if(ret==false){
			int pos=0;
			while(buf[pos]=='0')pos++;
			char ch=buf[pos];
			buf[pos]='\0';
			printf("%c%s0%s\n",ch,buf+0,buf+pos+1);
		}
		else printf("%s\n",buf);
	}
	return 0;
}
