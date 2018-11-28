#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
#include <map>

#define dprintf(...) printf(__VA_ARGS__)
#define dprintf(...)

using namespace std;

typedef map<char,int> dictionary;

void getline(char* buff) {
	while(((*buff)=getchar())!='\n') buff++;
	(*buff)=0;
}

int main(void) {
	int cases,i,maxnum,j;
	long long seconds;
	long long exp;
	dictionary dict;
	char buff[1024],tmp,*point;
	scanf("%d\n",&cases);
	dprintf("%d cases to proceed\n",cases);
	for(i=1;i<=cases;i++) {
		exp=1;
		seconds=0;
		maxnum=2;
		dict.clear();
		getline(buff);
		dprintf("Processing '%s'\n",buff);
		point=buff;
		dict.insert(make_pair(tmp=(*point),1));
		while((*point)==tmp) point++;
		if(*point)
			dict.insert(make_pair(*point,0));
		while(*point) {
			if(dict.find(*point)==dict.end()) {
				dprintf("Adding '%c' with value %d\n",*point,maxnum);
				dict.insert(make_pair(*point,maxnum++));
			}
			point++;
		}
		for(j=strlen(buff)-1;j>0;j--,exp*=maxnum) {
			dprintf("Processing '%c' - value %d, exponent %lld\n",buff[j],dict.find(buff[j])->second,exp);
			seconds+=(dict.find(buff[j])->second)*exp;
		}
		seconds+=exp;
		printf("Case #%d: %lld\n",i,seconds);
	}
	return 0;
}
