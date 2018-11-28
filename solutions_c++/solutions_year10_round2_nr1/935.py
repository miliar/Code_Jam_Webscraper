#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
class Dir{
public:
	string name;
	vector<Dir *> next;
	Dir(string fn="/"):name(fn){
	}
};
Dir * root=NULL;
int N,M;
int init();
const int SIZE = 10000;
char buff[SIZE];
void clear(Dir * );
int insert(char *);
int main(){
	freopen("dat.in","r",stdin);
	freopen("dat.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for (int i=0;i<cas;i++){
		int ans=init();
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
int init(){
	clear(root);
	root=new Dir();
	scanf("%d%d",&N,&M);
	gets(buff);
	for (int i=0;i<N;i++){
		gets(buff);
		//printf("org: %s\n",buff);
		insert(buff);
	}
	int sum=0;
	for (int i=0;i<M;i++){
		gets(buff);
		//puts(buff);
		int tmp=insert(buff);
		//printf("add: %d\n",tmp);
		sum+=tmp;
	}
	return sum;
}
void clear(Dir * ptr){
	if (ptr){
		int len = ptr->next.size();
		for (int i=0;i<len;i++){
			if (ptr->next[i]){
				clear(ptr->next[i]);
				ptr->next[i]=NULL;
			}
		}
		delete ptr;
	}
}
int insert(char * str){
	char wd[200];
	int sp=0;
	Dir *ptr=root;
	int cnt=0;
	for (int i=1;str[i];i++){
		if ('/'==str[i]){
			wd[sp]=0;
			string fname(wd);
			bool isfd=false;
			int len =ptr->next.size(); 
			for (int i=0;i<len;i++){
				if (fname.compare(ptr->next[i]->name)==0){
					isfd=true;
					ptr=ptr->next[i];
					break;
				}
			}
			if (!isfd){
				cnt++;
				Dir * tmp = new Dir(fname);
				ptr->next.push_back(tmp);
				ptr=tmp;
			}
		}else{
			wd[sp++]=str[i];
		}
	}
	wd[sp]=0;
	string fname(wd);
	bool isfd=false;
	int len =ptr->next.size(); 
	for (int i=0;i<len;i++){
		if (fname.compare(ptr->next[i]->name)==0){
			isfd=true;
			ptr=ptr->next[i];
			break;
		}
	}
	if (!isfd){
		cnt++;
		Dir * tmp = new Dir(fname);
		ptr->next.push_back(tmp);
		ptr=tmp;
	}
	return cnt;
}
