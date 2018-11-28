#include <vector>
#include <string>
#include <list>
#include <map>
#include <utility>
#include <cmath>
#include <algorithm>
#include <sstream>
#include<iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
#define FOR0(i,n) for (i = 0; i < n; i++) 
#define FOR1(i,n) for (i = 1; i <= n; i++) 
int i,j,k;

int L,D,N;
VS allwords;
VS words;
void solve(string word);
int main()
{
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);
	
	cin>>L>>D>>N;
	FOR0(i,L) words.push_back("");
	FOR0(i,D){
		string tmp;
		cin>>tmp;
		allwords.push_back(tmp);
	}
	FOR1(i,N){
		string tmp;
		cin>>tmp;
		int result = 0;
		solve(tmp);
		FOR0(j,D){
			int flag = true;
			FOR0(k,L)
				if(words[k].find(allwords[j][k]) == -1){flag = false;break;} 
			if(flag) result++;
		}
		cout<<"Case #"<<i<<": "<<result<<endl;
	}
	return 0;
}
void solve(string word)
{
	int count = 0;
	FOR0(j,word.length()){
		if(word[j] == '('){
			int qqq = word.find(')',j);
			words[count++] = word.substr(j + 1,word.find(')',j) - j - 1);
			j = word.find(')',j);
		}
		else words[count++] = word[j];
	}
}