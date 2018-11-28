#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>

#define ln printf("\n")
#define rep(a,b) for(int a = 0; a < b; a++)

using namespace std;



char c[333];
char buf[1111];

bool read(){
	gets(buf);
	
	return true;
}

int cn = 1;

void process(){
	printf("Case #%d: ", cn++);
	
	int size = strlen(buf);
	rep(i,size) printf("%c", c[buf[i]]);
	ln;
}

void transcode(string a, string b){
	rep(i,a.size()) c[a[i]] = b[i];
}

int main(){
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	transcode("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	transcode("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	transcode("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	c['y'] = 'a';
	c['e'] = 'o';
	c['q'] = 'z';
	c['z'] = 'q';
	int t = -1;
	scanf("%d", &t);
	gets(buf);
	
	while(t-- && read()) process();
	
	//while(1);
	return 0;
}
