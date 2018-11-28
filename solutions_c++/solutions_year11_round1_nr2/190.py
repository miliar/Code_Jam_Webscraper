#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

int N,M,ans,cnt[26];
string word[10000],List,answord;

void Work(){
	scanf("%d %d",&N,&M);
	for (int i=0;i<N;i++) cin>>word[i];
	for (int i=0;i<M;i++){
		cin>>List;
		ans=-1;
		for (int j=0;j<N;j++){
			vector<string> Left;
			int len=word[j].length();
			for (int k=0;k<N;k++)
				if (word[k].length()==len){
					Left.push_back(word[k]);
				}
			int p=0,mistakes=0;
			while (Left.size()>1){
				memset(cnt,0,sizeof(cnt));
				int size=Left.size();
				for (int k=0;k<size;k++){
					for (int l=0;l<len;l++) cnt[Left[k][l]-'a']=1;
				}
				while (!cnt[List[p]-'a']) p++;
				bool flag=false;
				for (int l=0;l<len;l++) if (word[j][l]==List[p]){flag=true;break;}
				if (flag){
					int opt=0;
					for (int l=0;l<len;l++) if (word[j][l]==List[p]) opt|=(1<<l);
					vector<string> newLeft;
					for (int k=0;k<size;k++){
						flag=true;
						for (int l=0;l<len;l++)
							if ((opt&(1<<l)) && Left[k][l]!=List[p] ||
							(!(opt&(1<<l))) && Left[k][l]==List[p]){flag=false;break;}
						if (flag) newLeft.push_back(Left[k]);
					}
					Left=newLeft;
				}else{
					mistakes++;
					vector<string> newLeft;
					for (int k=0;k<size;k++){
						flag=true;
						for (int l=0;l<len;l++)
							if (Left[k][l]==List[p]){flag=false;break;}
						if (flag) newLeft.push_back(Left[k]);
					}
					Left=newLeft;
				}
				p++;
			}
			if (mistakes>ans){
				ans=mistakes;
				answord=word[j];
			}
		}
		cout<<" "<<answord;
	}
	cout<<endl;
}

int main(){
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	int Test;scanf("%d",&Test);
	for (int kase=1;kase<=Test;kase++){
		printf("Case #%d:",kase);
		Work();
	}
	return 0;
}
