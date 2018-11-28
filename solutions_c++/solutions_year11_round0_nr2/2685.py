#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

char comb[26][26];
char opp[26][26];

#define index(c) c-'A'

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);

	int k;
	cin>>k;

	for(int i=0;i<k;i++){
		memset(comb,0,sizeof(comb));
		memset(opp,0,sizeof(opp));

		int c;
		cin>>c;
		for(int j=0;j<c;j++){
			string tmp;
			cin>>tmp;
			comb[index(tmp[0])][index(tmp[1])]=tmp[2];
			comb[index(tmp[1])][index(tmp[0])]=tmp[2];
		}

		cin>>c;
		for(int j=0;j<c;j++){
			string tmp;
			cin>>tmp;
			opp[index(tmp[0])][index(tmp[1])]=1;
			opp[index(tmp[1])][index(tmp[0])]=1;
		}

		string ordernum;
		string order;
		string ans;
		cin>>ordernum>>order;
		for(size_t j=0;j<order.size();j++){
			if(ans.size()==0){
				ans.push_back(order[j]);
				continue;
			}

			char c=comb[index(order[j])][index(ans[ans.size()-1])];
			if(c)ans[ans.size()-1]=c;
			else{
				int k;
				bool flag=false;
				for(k=ans.size()-1;k>-1;k--){
					if(opp[index(ans[k])][index(order[j])]){
						ans.clear();
						flag=true;
						break;
					}
				}
				if(!flag)ans.push_back(order[j]);
			}
		}


		cout<<"Case #"<<i+1<<": [";
		for(unsigned int i=0;i<ans.size();i++){
			if(i!=0)cout<<", ";
			cout<<ans[i];
		}
		cout<<"]"<<endl;
	}


	return 0;
}