#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;

void initv(vector<string> &v,string dict[],int D){
	v.clear();
	for(int i=0;i<D;i++)
		v.push_back(dict[i]);
}
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int L,D,N;
	cin>>L>>D>>N;
	string dict[5010];
	for(int i=0;i<D;i++)
		cin>>dict[i];
	char pat[450];
	vector<string> v;
	for(int i=0;i<N;i++){
		initv(v,dict,D);
		scanf("%s",pat);
		char *apat=pat;
		int numtok=0;
		while(*apat!='\0'){
			
			bool temp[26]={0};
			if(*apat=='('){
				apat++;
				while(*apat!=')'){
					temp[*apat-'a']=true;
					apat++;
				}
				apat++;
			}else if(isalpha(*apat)){
				temp[*apat-'a']=true;
				apat++;
			}else{
				apat++;
				continue;
			}
			if(numtok>=L){
				numtok++;
				break;
			}
			int vsize=v.size();
			vector<string>::iterator it;
			for(it=v.begin();it!=v.end();){
				if(temp[(*it)[numtok]-'a'])
					it++;
				else
					v.erase(it);
			}
		numtok++;
		}
	printf("Case #%d: %d\n",i+1,(numtok!=L)?0:v.size());
	}
	return 0;
}
