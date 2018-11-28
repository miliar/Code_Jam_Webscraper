#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

vector<char> invoque;
char combine[26][26];
bool oppose[26][26];


void resoud(){
	int C=-6,O=-6;
	char s[200];
	scanf("%d",&C);
	fill(combine[0],combine[26],0);
	fill(oppose[0],oppose[26],false);
	for (int i=0;i<C;i++){
		scanf("%s",s);
		combine[s[0]-'A'][s[1]-'A']=s[2]-'A';
		combine[s[1]-'A'][s[0]-'A']=s[2]-'A';
	}
	scanf("%d",&O);
	for (int i=0;i<O;i++){
		scanf("%s",s);
		oppose[s[0]-'A'][s[1]-'A']=true;
		oppose[s[1]-'A'][s[0]-'A']=true;
	}
//	puts("ok");
	scanf("%*d%s",s);
	for (int i=0;s[i];i++){
		char nouv=s[i]-'A';
		while (!invoque.empty() && combine[invoque.back()][nouv]){
			nouv=combine[invoque.back()][nouv];
			invoque.pop_back();
		}
		invoque.push_back(nouv);
		for (int j=0;j<invoque.size()-1;j++)
			if (oppose[invoque[j]][nouv]){
				invoque.clear();
				break;
			}
	}
	printf("[");
	for (int i=0;i+1<invoque.size();i++)
		printf("%c, ",invoque[i]+'A');
	if (!invoque.empty())
		printf("%c",invoque.back()+'A');
	printf("]");
	invoque.clear();
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		resoud();
		puts("");
	}
	return 0;
}
