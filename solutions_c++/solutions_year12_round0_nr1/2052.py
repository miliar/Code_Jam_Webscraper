#import <iostream>
#import <map>
using namespace std;
map<char,char>m;

void createMap()
{
	char from[] = "qaozejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
        char to[] =   "zyeqour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	int i = 0;
	while( from[i] != '\0'){
		m[from[i]] = to[i];
		i++;
	}
	return;
}

void replace(char *st){
	while(*st != '\0'){
		*st = m[*st];
		st++;
	}
}
		

int main(){
	int N;
	scanf("%d", &N);
	char ans[105];
	createMap();
	int i = 1;
	while(N--){

		scanf(" %[^\n]s",ans);
		replace(ans);
		printf("Case #%d: %s\n",i++,ans);
	}	
	return 0;
}


