#include<string>
#include<iostream>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

int n;
string dic[10000];

bool contain(const string &word,const char c){
}

bool consistent(const string &word,const string &test,char c,bool *checked){
	if(word.find(c)==string::npos) return false;

	int len=test.length();
	if(len!=word.length()) return false;

	rep(i,len) if(test[i]=='_' && checked[word[i]-'a']) return false;

	rep(i,len){
		if(test[i]=='_' || (test[i]==word[i]));
		else return false;
	}
	return true;
}

int getScore(const string &word,const string &lst){
	bool b[26]={};
	int len=word.length();
	rep(i,len) b[word[i]-'a']=true;
	int cnt=count(b,b+26,true);

	int ans=0;
	string test(len,'_');
	bool checked[26]={};
	for(int i=0,j;i<lst.length();i++){
		if(cnt==0) break;

		char c=lst[i];
		for(j=0;j<n;j++){
			if(consistent(dic[j],test,c,checked)) break;
		}
		if(j==n) continue;

		if(b[c-'a']){
// printf("\n@ %c %d\n",c,cnt);
			rep(k,len) if(word[k]==c) test[k]=c;
			cnt--;
		}
		else{
// printf("\nX %c %d\n",c,cnt);
			ans++;
		}

		checked[c-'a']=true;
	}

	return ans;
}

string solve(const string &lst){
	int score=-1;
	string ans;
	rep(i,n){
		int tmp=getScore(dic[i],lst);
// printf("\n> %s: %d\n",dic[i].c_str(),tmp);
		if(score<tmp){
			score=tmp;
			ans=dic[i];
		}
	}
	return ans;
}

int main(){
	int T0; cin>>T0;
	for(int T=1;T<=T0;T++){
		int m; cin>>n>>m;
		rep(i,n) cin>>dic[i];

		cout<<"Case #"<<T<<":";
		rep(i,m){
			string lst; cin>>lst;
			cout<<" "<<solve(lst);
		}
		cout<<endl;
	}

	return 0;
}
