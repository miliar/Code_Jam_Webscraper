									/*	In the name of God	*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;
int mp[256]={0};
string e="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
string d="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
char s[10001],*p;

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);	
	mp['y']='a';
	mp['e']='o';
	mp['q']='z';
	int ti,tc,i,j,k;
	rep(i,e.size())
		mp[e[i]]=d[i];
	mp['z']='q';
	gets(s);
	sscanf(s,"%d",&tc);
	rep(ti,tc){
		printf("Case #%d: ",ti+1);
		gets(s);
		p=strtok(s," ");
		while (1){
			for (i=0;p[i];i++)
				printf("%c",mp[p[i]]);
			p=strtok(NULL," ");
			if (p!=NULL)
				printf(" ");
			else
				break;
		}
		printf("\n");
	}
	return 0;
}