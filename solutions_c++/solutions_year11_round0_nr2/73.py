#include<stdio.h>
#include<set>
#include<map>
using namespace std;
map<pair<char,char>,char> merge;
inline char getmerge(char a,char b){
    map<pair<char,char>,char>::iterator it;
    it=merge.find(make_pair<char,char>(a,b));
    if(it!=merge.end())return it->second;
    it=merge.find(make_pair<char,char>(b,a));
    if(it!=merge.end())return it->second;
    return 0;
}
set<char> conf[30];
char inp[1000];
char out[1000];
int main(){
    int t,i,j,cas=1;
    scanf("%d",&t);
    while(t--){
	for(i=0;i<26;i++)conf[i].clear();
	merge.clear();
	int r;
	scanf("%d",&r);
	while(r--){
	    char tmp[10];
	    scanf("%s",tmp);
	    merge[make_pair<char,char>(tmp[0],tmp[1])]=tmp[2];
	}
	scanf("%d",&r);
	while(r--){
	    char tmp[10];
	    scanf("%s",tmp);
	    conf[tmp[0]-'A'].insert(tmp[1]);
	    conf[tmp[1]-'A'].insert(tmp[0]);
	}
	scanf("%d",&r);
	scanf("%s",inp);
	int oc=0;
	for(i=0;i<r;i++){
	    out[oc++]=inp[i];
	    if(oc>1){
		char c=getmerge(out[oc-1],out[oc-2]);
		if(c){
		    oc-=2;
		    out[oc++]=c;
		}
	    }
	    if(oc){
		for(j=0;j<oc;j++){
		    if(conf[out[oc-1]-'A'].find(out[j])!=conf[out[oc-1]-'A'].end())break;
		}
		if(j<oc)oc=0;
	    }
	}
	printf("Case #%d: [",cas++);
	if(oc==0)puts("]");
	else{
	    for(i=0;i<oc;i++){
		if(i)printf(", ");
		printf("%c",out[i]);
	    }
	    puts("]");
	}
    }
}
