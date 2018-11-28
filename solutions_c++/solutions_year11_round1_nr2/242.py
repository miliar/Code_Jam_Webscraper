#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<string>  dic;
string order;
vector<int> correct, buffer;
bool bit [200];

bool same(int a , int b, char x){
	string aa = dic[a];
	string bb = dic[b];
	if(aa.size()  != bb.size())return false;
	for(int i = 0 ; i < aa.size(); i++ ){
		if((aa[i]== x && bb[i] !=x) || (bb[i]== x && aa[i] != x)){
//			cout << aa[i] << bb[i] << endl;
			return false;
		}
	}
	return true;
}
int calc(int u){
	int ans = 0;
	buffer.clear();
//	cout << "test" <<u<<endl;
	for(int j = 'a'; j <= 'z'; j++)bit[j]=false;
//	for(char j = 'a'; j <= 'z'; j++)cout  << j <<bit[j] << endl;
	for(int i = 0; i< dic.size(); i++){
		if(dic[i].size()== dic[u].size()){
			buffer.push_back(i);
			int ss = dic[i].size();
			for(int k = 0; k < ss; k++)bit[dic[i][k]]= true;
		}
	}
//	for(char j = 'a'; j <= 'z'; j++)cout  << j <<bit[j] << endl;
//	cout << endl;
	
	for(int i = 0 ; i < 26; i++){
//		cout <<"size" << buffer.size() << endl;
//		for(char j = 'a'; j <= 'z'; j++)cout << j <<bit[j] << endl;
		if(buffer.size()==1)return ans;
		if(!buffer.empty())correct = buffer;
		buffer.clear();
		if(!bit[order[i]])continue;
//		cout << "check" << order[i] << endl;

		for(int j = 'a'; j <= 'z'; j++)bit[j]=false;
		for(int j = 0; j <correct.size(); j++){
			if(same(correct[j],u,order[i])){
				buffer.push_back(correct[j]);
				int ss = dic[correct[j]].size();
				int s = correct[j];
				for(int k = 0; k < ss; k++)bit[dic[s][k]]= true;
			}
		}
		if(dic[u].find(order[i],0)== string::npos)ans++;
//		cout <<"wrong" << ans << endl;
	}
	return ans;
}
void work(int x)
{
	int n,m;
	cin >> n >> m;
	dic.clear();
	cout << "Case #" << x << ":";
	for(int i = 0; i<n ;i++){
		string t;
		cin >> t;
		dic.push_back(t);
	}
	for(int i = 0; i< m; i++){
		cin >> order;
		int max = 0;
		int ans = 0;
		for(int j = 0 ; j < n; j++){
			int temp = calc(j);
			if(temp > max){
				max = temp;
				ans = j;
			}
		}
		cout <<" "<< dic[ans];
	}
	cout << endl;
	
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)work(i);
}
