#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
	int n, s, q, i, j, k, l, sum, res1, res2;
	string buf;
	vector<string> eng, que;
	vector<bool> flag;
	cin>>n;
	for (i =0 ; i < n ; i++){
		cin>>s;
		getline(cin,buf);
		eng.clear();
		flag.clear();
		for (j = 0; j < s; j++){
			getline(cin,buf);
			eng.push_back(buf);
			flag.push_back(true);
		}
		cin>>q;
		getline(cin,buf);
		que.clear();
		for (j = 0; j < q; j++){
			getline(cin,buf);
			que.push_back(buf);
		}
		res1 = 0;
		sum = s;
		for (j = que.size()-1; j >=0 ; j--){
			for (k = 0 ; k < (int)eng.size(); k++){
				if (flag[k] == true && eng[k] == que[j]){
					flag[k] = false;
					sum--;
					break;
				}
			}
			if (sum == 0){
				res1++;
				sum = s-1;
				for(l = 0; l < (int)flag.size(); l++)
					flag[l] = true;
				flag[k] = false;
			}
		}
		res2 = 0;
		sum = s;
		for(l = 0; l < (int)flag.size(); l++)
			flag[l] = true;
		for (j = 0; j < que.size(); j++){
			for (k = 0 ; k < (int)eng.size(); k++){
				if (flag[k] == true && eng[k] == que[j]){
					flag[k] = false;
					sum--;
					break;
				}
			}
			if (sum == 0){
				res2++;
				sum = s-1;
				for(l = 0; l < (int)flag.size(); l++)
					flag[l] = true;
				flag[k] = false;
			}
		}
			cout<<"Case #"<<i+1<<": "<<(res1<res2?res1:res2)<<endl;
	}
	return 0;
}