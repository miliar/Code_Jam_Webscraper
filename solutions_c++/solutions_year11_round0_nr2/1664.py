
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

int combin_table[256][256];
int oppose_table[256][256];
vector<char> result;

void push_ele(char ch){
	if(result.size()!=0){
		char last = result[result.size()-1];
		if(combin_table[last][ch]!=0){
			result.pop_back();
			result.push_back(combin_table[last][ch]);
			return;
		}
	}

	for(vector<char>::iterator i=result.begin();
			i!=result.end();++i){
		if( oppose_table[*i][ch] ){
			result.clear();
			return;
		}
	}

	result.push_back(ch);
	return;
}

string solve()
{

	int combin_num;
	int oppose_num;

	memset(combin_table,0,sizeof(combin_table));
	memset(oppose_table,0,sizeof(oppose_table));

	string rule;
	cin>>combin_num;
	for(int i=0;i<combin_num;++i){
		cin>>rule;
		combin_table[rule[0]][rule[1]] = 
			combin_table[rule[1]][rule[0]] = rule[2];
	}
	cin>>oppose_num;
	for(int i=0;i<oppose_num;++i){
		cin>>rule;
		oppose_table[rule[0]][rule[1]] = 
			oppose_table[rule[1]][rule[0]] = 1;
	}

	int len;
	cin>>len;
	string ele_list;
	cin>>ele_list;

	result.clear();
	for(int i=0;i<len;++i){
		push_ele(ele_list[i]);
	}

	cout<<'[';
	for(vector<char>::iterator i=result.begin();
			i!=result.end();++i){
		if(i==result.begin()){
			cout<<*i;
		}else{
			cout<<", "<<*i;
		}
	}
	cout<<']';

	return "";
}

int main()
{
	int casenum;
	cin>>casenum;
	for(int i=0;i<casenum;++i){
		cout<<"Case #"<<(i+1)<<": ";
		cout<<solve()<<endl;
	}
}
