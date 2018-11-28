#include<iostream>
#include<string>
#include<map>
#include<vector>
#include <set>
using namespace std;
int L,D,N;
vector<string> dic;
int main(){
	cin>>L>>D>>N;
	for(int i=0;i<D;i++){
		string s;
		cin>>s;
		dic.push_back(s);
	}
	vector<string>vs;
	for(int test=0;test<N;test++){
		string s;
		vs.clear();
		cin>>s;
		int val=0;
		for(int i=0;i<s.size();i++){
			string ss="";
			if(s[i]=='(')
			{	i++;
				while(s[i]!=')' && i<s.size()){
					ss+=s[i++];
				}
				//i++;
				vs.push_back(ss);

			}else{
				ss=s[i];
				vs.push_back(ss);
			}val++;
		}
		
		int res=0;
		for(int i=0;i<D;i++){
			int flg1=0;
			for(int j=0;j<dic[i].size();j++){
				int flg=0;
				for(int k=0;k<vs[j].size();k++){
					if(vs[j][k]==dic[i][j]){
						flg=1;break;
					}
				}
				if(flg==0)break;
				else flg1++;
			}
			if(flg1==dic[i].size())res++;
		}
		printf("Case #%d: %d\n",test+1,res);
	}
	
}