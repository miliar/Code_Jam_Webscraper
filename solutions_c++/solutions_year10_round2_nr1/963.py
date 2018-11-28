#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
#include<string>

using namespace std;
set<string> fp;

int createp(string ss);

int main(void){
	int t;
	char ss[200];
	int j;
	while(scanf("%d",&t)==1){
		int m,n;
		int result;
		for(int i=0;i<t;i++){
			result=0;
			scanf("%d%d",&m,&n);
			for(j=0;j<m;j++){
				scanf("%s",ss);
				createp(string(ss));
			}
			for(j=0;j<n;j++){
				scanf("%s",ss);
				result+=createp(string(ss));
			}
			fp.erase(fp.begin(),fp.end());
			printf("Case #%d: %d\n",i+1,result);
		}
	}
	return 0;
}


int createp(string ss){
	int result=0;
	string::size_type pos=ss.size()-1;
	while((pos!=string::npos)&&(pos!=-1)){
		if(fp.find(ss.substr(0,pos+1))!=fp.end());
		else{
			fp.insert(ss.substr(0,pos+1));
			result++;
		}
		pos=ss.find_last_of("/",pos);
		// printf("pos:%d\n",pos);
		if(pos!=-1)pos--;
	}
	return result;
}
