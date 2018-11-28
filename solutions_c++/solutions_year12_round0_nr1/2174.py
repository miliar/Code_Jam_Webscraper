#include<cstdio>
#include<cstring>
#include<cctype>
#include<iostream>
using namespace std;
char s[1024],c[256],*p;
void ppp(){
	char a[4][128]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv",
		"y qee"
	},
		b[4][128]={
			"our language is impossible to understand",
			"there are twenty six factorial possibilities",
			"so it is okay if you want to just give up",
			"a zoo"
	};
	int cc=0;
	for(int i=0;i<4;++i){
		for(int j=0;a[i][j];++j){
			if(!c[a[i][j]]){
				++cc;
				c[a[i][j]]=b[i][j];
			}
		}
	}
	/*cerr<< cc << endl;
	for(int i=0;i<256;++i)
	if(islower(i)|| (i==' ') ){
		if(c[i]){
			cerr <<(char)i <<": "<<c[i] << endl;
		}else cerr << (char)i << ": Not found\n";
	}*/
	c['z']='q';
}
int main(){
	int n;
	ppp();
	scanf("%d ",&n);
	for(int tc=1;tc<=n;++tc){
		gets(s);
		for(p=s;*p;++p)*p= c[*p];
		printf("Case #%d: %s\n",tc,s);
	}
	return 0;
}
