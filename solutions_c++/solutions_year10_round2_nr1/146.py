#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

struct node{
	string name;
	int son;
	int bro;
};

vector<node>tr;
string seq[101];
int n,m;
int cnt;

int insert_seq(int v,int pos,int len){
	if(pos==len)return 0;
	int j = tr[v].son;
	while(j>=0){
		if(tr[j].name==seq[pos])
			return insert_seq(j,pos+1,len);
		j = tr[j].bro;
	}
	node tmp;
	tmp.name=seq[pos];
	tmp.son = -1;
	tmp.bro = tr[v].son;
	tr.push_back(tmp);
	tr[v].son = cnt;
	cnt++;
	return 1+insert_seq(cnt-1,pos+1,len);
}


int depart_seq(string str){
	int i;
	int len = 0;
	//cout<<str<<endl;
	seq[0] = "";
	for(i=1;i<str.length();i++){
		if(str[i]=='/'){
			len++;
			seq[len]="";
			continue;
		}
		seq[len]=seq[len]+str[i];
	}
	len++;
	/*for(i=0;i<len;i++)
		cout<<seq[i]<<" ";
	cout<<endl;*/
	return len;
}

void work(){
}

int main(){
	int tc;
	int tt;
	cin>>tc;
	for(tt=1;tt<=tc;tt++){
		cout<<"Case #"<<tt<<": ";
		cnt = 1;
		tr.clear();
		node tmp;
		tmp.name="/";
		tmp.son=tmp.bro=-1;
		tr.push_back(tmp);
		cin>>n>>m;
		string str;
		int i,ans=0;
		for(i=0;i<n;i++){
			cin>>str;
			insert_seq(0,0,depart_seq(str));
		}
		for(i=0;i<m;i++){
			cin>>str;
			ans+=insert_seq(0,0,depart_seq(str));
			//cout<<ans<<endl;
		}

		cout<<ans<<endl;
	}
}
