#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct node{
	node (){
		for(int i=0;i<27;i++)
			next[i]=NULL;
	}
	map<string,int> m;
	node* next[27];

};

class trie{
	public:
		void insert(string str);
		void insert(string str,int off,node &r);
		int sum(string str,int off,node &r);
		int sum(string str);
		void travel(node &r);
		void travel(){travel(root);}
		bool check(string str,map<string,int> &m){
			map<string,int>::iterator eiter=m.end();
			if(m.find(str)==eiter) return false;
			return true;
		}
	private:
		node root;

};
void trie::travel(node &r)
{
	bool flag=false;
	for(int i=0;i<26;i++){
		if(r.next[i]!=NULL){
			flag=true;
			cout<<(char)('a'+i);
			travel(*(r.next[i]));
		}
	}
	if(!flag) cout<<endl;
}
int trie::sum(string str)
{
	return sum(str,0,root);
}
void trie::insert(string str)
{
	insert(str,0,root);
}
void trie::insert(string str,int off,node &r)
{
	if(off>=str.size()) {
		return ;}
	int idx=(int)(str[off]-'a');
	if(idx<0 || idx>26) return;
	if(r.next[idx]==NULL)
		r.next[idx]=new node();
	insert(str,off+1,*(r.next[idx]));
}
int trie::sum(string str,int off, node &r)
{
	string sub=str.substr(off);
	int rs=0;
	int trs;
	int idx;
	int end_off=off+1;
	string idxstr;

	if(off>=str.size()) return 1;

	if(check(sub,r.m))
		return r.m[sub];
	
	if(str[off]=='('){
		while(end_off<str.size() && str[end_off]!=')') end_off++;
		off+=1;
		while(off<end_off){
			idxstr="";
			idxstr=idxstr+str[off]+str.substr(end_off);

			idx=(int)(str[off]-'a');
			if(check(idxstr,r.m)){
				rs+=r.m[idxstr];
				off++;
				continue;
			}else{
				if(r.next[idx]==NULL){				
					r.m[idxstr]=0;
				}else{
					trs=sum(str,end_off+1,*(r.next[idx]));
					r.m[idxstr]=trs;
					rs+=trs;
				}
			}			
			off++;
		}
		r.m[sub]=rs;
		return rs;

	}
	else{
		idxstr="";
		idxstr=idxstr+str[off]+str.substr(end_off);

		idx=(int)(str[off]-'a');
		if(check(idxstr,r.m))
			return r.m[idxstr];
		if (r.next[idx]==NULL) {
			r.m[idxstr]=0;
			return 0;
		}
		trs=sum(str,off+1,*(r.next[idx]));
		r.m[sub]=trs;
		return trs;
	}
}


int main()
{
	int l,d,n;
	string str;
	trie t;
	ifstream fin("f:\\input.txt");
	ofstream fout("f:\\output.txt");
	fin>>l>>d>>n;
	for(int i=0;i<d;i++){
		fin>>str;
		t.insert(str);
	//	cout<<str<<endl;
	//	t.travel();
	}
	t.travel();
	for(int i=0;i<n;i++){
		fin>>str;
		int tmp=t.sum(str);
		fout<<"Case #"<<i+1<<": "<<tmp<<endl;
	}
	cout<<endl;
	t.travel();
	fin.close();
	fout.close();
	cout<<"over"<<endl;
	cin>>l;
	return 0;
}
