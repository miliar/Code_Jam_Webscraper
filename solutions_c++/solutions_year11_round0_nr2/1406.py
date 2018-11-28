/**
* @author Gareve
* @problem
* @judge
*/
#define DEBUG
#ifndef NDEBUG	
	#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;
#else
	#define DBG(a) ;
#endif
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <map>

using namespace std;

int nt,nd,len;
string str,res,tmp;
map<string,char> tr;
bool del[300][300];

void f(char c){
	res.push_back(c);
	if(res.length()<2)return;
	tmp = res.substr(res.size()-2);
	sort(tmp.begin(),tmp.end());
	
	if(tr.find(tmp)!=tr.end()){
	   	c = tr[tmp];
		res = res.substr(0,res.size()-2);
		res.push_back(c);
		return;
	}
	
	for(int i=0;i<res.size()-1;i++){
		if(del[c][res[i]]){
			res = "";
			return;
		}
	}

}
void resuelva(){
	tr.clear();
	memset(del,false,sizeof(del));
	cin>>nt;
	for(int i=1;i<=nt;i++){
		cin>>str;
		sort(str.begin(),str.begin()+2);
		tr[str.substr(0,2)]=str[2];
	}
	int a,b;
	cin>>nd;
	for(int i=1;i<=nd;i++){
		cin>>str;
		a=str[0];
		b=str[1];
		del[a][b]=del[b][a]=true;
	}
	res = "";
	cin>>len>>str;
	for(int i=0;i<len;i++)
		f(str[i]);

	printf("[");
	for(int i=0;i<res.length();i++){
		if(i>0)printf(", ");
		printf("%c",res[i]);
	}
	printf("]\n");
}
int main(){
	int q;
	cin>>q;
	for(int i=1;i<=q;i++){
		printf("Case #%d: ",i);
		resuelva();
	}
}

