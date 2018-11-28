#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int cnt(string & str1, string & str2){
	int ans = 0;
	for (int i = 0; i < min(str1.size(),str2.size()); i++){
		if (str1[i] != str2[i]) return ans - 1;
		if (str1[i] == '/')
			ans++;
	}
	return ans;
}

struct node{
	map<string,int> childs;	
};

node nn[300000];
int size;

void clear(){
	for (int i = 0; i < size; i++)
		nn[i].childs.clear();
}

int insert(vector<string> & vec){
	int state = 0;
	int zzz = 0;
	for (int i = 1; i < vec.size(); i++){
		if (nn[state].childs.find(vec[i]) != nn[state].childs.end())
			state = nn[state].childs[vec[i]];
		else{
			nn[state].childs[vec[i]] = size;
			state = size;
			zzz++;
			size++;				
		}
	}
	return zzz;
}              

vector<string> split(string & str){
	vector<string> res;
	string cur = "";
	for (int i = 0; i < str.size(); i++)
		if (str[i] == '/'){
			res.push_back(cur);
			cur = "";
		}else cur += str[i];
	res.push_back(cur);
	return res;
}           

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t; scanf("%d",&t);
	//vector<pair<string,int>> vec;
	
	for (int tt = 0; tt < t; tt++){
		clear(); size = 1;
		vector<pair<string, int>> vec;
		//vec.push_back(make_pair("",0));	
		int n,m; 
		scanf("%d%d",&n,&m);
		for (int i = 0; i < n; i++){
			string str; cin >> str;
			vector<string> v = split(str);
			insert(v);
			//vec.push_back(make_pair(str,0));
		}
		int ans = 0;
		for (int i = 0; i < m; i++){
			string str; cin >> str;
			vector<string> v = split(str);
			ans += insert(v);
			//vec.push_back(make_pair(str,1));
		}		
		printf("Case #%d: %d\n",tt+1,ans);		
	}

	
	
	
	return 0;
}