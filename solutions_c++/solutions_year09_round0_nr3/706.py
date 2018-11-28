#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;
string w,ww;
string s;
int dp[500][19];

int compute(int si, int wi){
	//cout<<si<<" "<<wi<<endl;
	if(wi==19)
		return 1;
	if(si==s.size())
		return 0;
	if(dp[si][wi]!=-1)
		return dp[si][wi];
	int use=-1;
	int nouse=-1;
	for(int i=si+1; i<s.size(); ++i){
		if(s[i]==w[wi]){
			nouse=i;
			break;
		}
	}
	if(wi!=18){
		for(int i=si+1; i<s.size(); ++i){
			if(s[i]==w[wi+1]){
				use=i;
				break;
			}
		}
	}else{
		use=100;
	}
	int rtn=0;
	if(use!=-1){
		rtn=(rtn+compute(use, wi+1))%10000;
	}
	if(nouse!=-1){
		rtn=(rtn+compute(nouse, wi))%10000;
	}
	//cout<<si<<" "<<wi<<" "<<rtn<<endl;
	dp[si][wi]=rtn;
	return rtn;
}

int main(){
	w="welcome to code jam";
	ww="acdejlmotw";
	bool used[26];
	bool found[26];
	
	memset(used,0,sizeof(used));
	for(int i=0; i<ww.size(); ++i){
		used[ww[i]-'a']=true;
	}
	
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	
	
	int ca;
	fin>>ca;
	string ss;
	getline(fin,ss);
	for(int cas=1; cas<=ca; ++cas){
		memset(found,0,sizeof(found));
		getline(fin,ss);
		s="";
		bool first=true, space=false;
		for(int i=0; i<ss.size(); ++i){
			if(used[ss[i]-'a'] || ss[i]==' '){
				if(first){
					if(ss[i]=='w'){
						first=false;
						s+=ss[i];
					}
				}else{
					s+=ss[i];
				}
			}
		}
		for(int i=0; i<500; ++i)
			fill_n(dp[i],19,-1);
		int rtn=(s.size()>=19)?compute(0,0):0;
		
		
		fout<<"Case #"<<cas<<": ";
		for(int i=1000; i!=0; i/=10)
			fout<<(rtn/i)%10;
		fout<<endl;
	}
}
