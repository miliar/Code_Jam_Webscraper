#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
using namespace std;

const int kind=26;
int L,D,N,ans;
string w[20],tmp;

struct Treenode
{
    int count;
    Treenode *next[kind];
    Treenode()
    {
        count=1;
        for(int i=0;i<kind;i++)
            next[i]=NULL;
    }
};

void insert(Treenode *&root,char *word)
{
    Treenode *location=root;
    int i=0,branch=0;
    
    if(location==NULL) {location=new Treenode();root=location;}

    while(word[i])
    {
        branch=word[i]-'a';
        if(location->next[branch]) location->next[branch]->count++;
        else location->next[branch]=new Treenode();
        i++;
        location=location->next[branch];
    }
}

int search(Treenode *root,char *word)
{
    Treenode *location=root;
    int i=0,branch=0,ans;

    if(location==NULL) return 0;

    while(word[i])
    {
        branch=word[i]-'a';
        if(!location->next[branch]) return 0;
        i++;
        location=location->next[branch];
        ans=location->count;
    }
    return ans;
}
void dfs(int deep,Treenode *root){
	Treenode *location=root;
    int i=0;
    if(deep == L) {
		ans++;return ;
	}

	for(i=0;i<w[deep].length();i++){
		char doit[30];
		memset(doit,0,sizeof doit);
		strcpy(doit,w[deep].c_str());
		int val = doit[i]-'a';
		if(location->next[val] != NULL){
			dfs(deep+1,location->next[val]);
		}
	}

}

int main()
{
	ifstream fin("C:\\Documents and Settings\\Administrator\\桌面\\A-small-attempt1.in");
	ofstream fout("C:\\Documents and Settings\\Administrator\\桌面\\新建 文本文档 (3).txt");
	int i,p,start;
	char word[20],str[1000];

	while(fin>>L>>D>>N/*scanf("%d%d%d",&L,&D,&N)!=EOF*/){
		Treenode *root=NULL;
		while(D--){
			//scanf("%s",word);
			fin>>word;
			insert(root,word);
		}
		for(i=0;i<N;i++){
			//scanf("%s",str);
			fin>>str;
			ans = p = start = 0;
			while(start<strlen(str)){
				tmp.erase();
				if(str[start]=='('){
					while( 1 ){
						start++;
						if(str[start] == ')') break;
						tmp += str[start];
					}
					start++;
					w[p++] = tmp;
					
				}
				else{
					w[p++] = str[start];
				
					start++;
				}
			}
			dfs(0,root);
			//printf("Case #%d: %d\n",i+1,ans);
			fout<<"Case #"<<i+1<<": "<<ans<<endl;
		}
		
	}
    return 0;
}