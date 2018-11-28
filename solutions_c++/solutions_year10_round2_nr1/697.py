#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>

using namespace std;

int n,m;
vector<string> old[250];
vector<string> cur;
int find_first_unmatch(){
	int i,j,max=0;
	for(i=0;i<n;i++){
		for(j=0;j<old[i].size() && j<cur.size() && old[i][j] == cur[j];j++);
		if(j==cur.size()) return j;
		if(j > max)
			max=j;
	}
	return max;
}
int mkdir(int pos){
	return cur.size()-pos;
}
void solve(){
	int i,k,count=0;
	char *tok, path[108];
	scanf("%d %d", &n, &m);
	for(i=0;i<n;i++){
		old[i].clear();
		scanf("%s", path);
		for(tok=strtok(path,"/");tok!=NULL;tok=strtok(NULL,"/"))
			old[i].push_back(tok);
//		for(k=0;k<old[i].size();k++)
//			printf("%s ", old[i][k].c_str());
//		printf("\n");
	}
	for(k=0;k<m;k++){
		cur.clear();
		scanf("%s", path);
		for(tok=strtok(path,"/");tok!=NULL;tok=strtok(NULL,"/"))
			cur.push_back(tok);
//		for(i=0;i<cur.size();i++)
//			printf("%s ", cur[i].c_str());
//		printf("\n");
		i = find_first_unmatch();
//		printf("longest match = %d\n", i);
		count += mkdir(i);
//		printf("mkdir=%d\n",mkdir(i));
		old[n++] = cur;
	}
	printf("%d\n", count);
}
int main(){
    int i,T;
    scanf("%d", &T);
    for(i=1;i<=T;i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
