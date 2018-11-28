#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<int> list_check(int now, int d,char str, vector<int> boolean_list, vector<string> talk){
	for(int i=0;i<d;i++){
		//cout << boolean_list[i];
		if(boolean_list[i] == 0) continue;
		if(talk[i][now] != str){
			boolean_list[i] = 0;
		}
	}
	
	return boolean_list;
}

int main(){
	int l,d,n;
	cin >> l >> d >> n;
	
	vector<string> talk;
	for(int i=0;i<d;i++){
		string temp;
		cin >> temp;
		talk.push_back(temp);
		//cout << talk[i] << endl;
	}
	
	vector<int> charact;
	for(int k1=0,k2=0;k2<d;k1++){
		bool conclude = false;
		for(int j=0;j<charact.size();j++){
			if(charact[j] == talk[k2][k1]){
				//cout << "*";
				conclude = true;
				break;
			}
		}
		
		if(!conclude){
			charact.push_back((char)talk[k2][k1]);
			//cout << talk[k2][k1];
		}
		//cout << k1 << " " << k2 << endl;
		if(k1 >= talk[k2].size()){
			k2++;
			k1=0;
		}
	}
	
	for(int k=0;k<n;k++){
		vector<int> boolean_list;
		for(int i=0;i<d;i++) boolean_list.push_back(1);
		
		string str;
		cin >> str;
		
		for(int j=0,now=0;j<str.length();j++){
			if(str[j] == '('){
				for(j++;str[j]!=')';j++){
					vector<int> boolean_list2 = list_check(now,d,str[j],boolean_list,talk);
					for(int x=0;x<boolean_list.size();x++) boolean_list[x] += boolean_list2[x];
					//cout << "check " << str[j] << ", ";
				}
				for(int x=0;x<boolean_list.size();x++){
					if(boolean_list[x] < 2) boolean_list[x] = 0;
					else boolean_list[x] = 1;
				}
			}
			else{
				boolean_list = list_check(now,d,str[j], boolean_list,talk);
				//cout << "check " << str[j] << ", ";
			}
			now++;
		}
		
		int ans=0;
		for(int i=0;i<d;i++){
			ans+=boolean_list[i];
		}
		cout << "Case #" << k+1 << ": " << ans << endl;
	}
	
	return 1;
}
