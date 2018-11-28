#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;


int main(){
	
	
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out","w",stdout);
	
	int t,i,c,d,n,j,p,k;
	cin >> t;

	for(i=0;i<t;i++){
		vector<string> v_combine;
		vector<string> v_opposite;
		cin >> c;
		for(j=0;j<c;j++){
			string combine;
			cin >> combine;
			v_combine.push_back(combine);
		}
		cin >> d;
		for(j=0;j<d;j++){
			string opposite;
			cin >> opposite;
			v_opposite.push_back(opposite);

		}
		cin >> n;
		string base;
		cin >> base;

		for(j=1;j<(base.length());j++){
			string baseSub = base.substr(j-1,2);
			for(p=0;p<v_combine.size();p++){
				string curCom = v_combine[p].substr(0,2);
				string curComRev = curCom;
				reverse(curComRev.begin(),curComRev.end());
				if(curCom==baseSub || curComRev==baseSub){
					string cur(1,v_combine[p][2]);
					base.replace(j-1,2,cur);
					break;
				}
			}
			char cur_char='+';
			for(p=0;p<v_opposite.size();p++){
				if(base[j]==v_opposite[p][0]){
					cur_char=v_opposite[p][1];
					break;
				}
				else if(base[j]==v_opposite[p][1]){
					cur_char=v_opposite[p][0];
					break;
				}
			}
			int min = j;
			if(cur_char!='+'){
				for(k=j-1;k>=0;k--){
					if(base[k]==cur_char){
						if(k<min) min=k;
						//base.erase(k,j-k+1);
						//j=k;
					}
				}
				if(min<j){
					base.erase(0,j+1);
					j=0;
				}
			}

		}
		
		printf("Case #%d: [",i+1);
		if(base.size()==0){
			printf("]\n");
			continue;
		}
		for(j=0;j<base.size();j++){
			if(j!=(base.size()-1)){
				printf("%c, ",base[j]);
			}
			else{
				printf("%c]\n",base[j]);
			}
		}

	}
	return 0;
}