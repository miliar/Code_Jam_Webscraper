#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

void runCase()
{
	int C, D, N;
	map<string,char> trans;
	set<string> oppo;
	
	scanf("%d",&C);
	for(int i = 0; i < C; i++) {
		char buf[4] = {0};
		scanf("%s",buf);
		trans[string(buf,2)] = buf[2];
	}
	
	scanf("%d",&D);
	for(int i = 0; i < D; i++) {
		char buf[3] = {0};
		scanf("%s",buf);
		oppo.insert(string(buf,2));
	}
	
	scanf("%d",&N);
	char myList[100+1] = {0};
	scanf("%s",myList);
	
	for(int i = 1; i < N; i++) {
		swap(myList[i],myList[i-1]);
		if(trans.count(string(myList+i-1,2)) != 0) {
			char c = trans[string(myList+i-1,2)];
			myList[i] = c;
			myList[i-1] = '#';
		}
		
		swap(myList[i],myList[i-1]);		
		if(trans.count(string(myList+i-1,2)) != 0) {
			char c = trans[string(myList+i-1,2)];
			myList[i] = c;
			myList[i-1] = '#';
		}
		
		bool cls = false;
		for(int j = 0; j < i; j++) {
			string op1 = "  ", op2 = "  ";
			op1[0] = myList[i];
			op1[1] = myList[j];
			
			op2[0] = myList[j];
			op2[1] = myList[i];
			
			if(oppo.count(op1) != 0 || oppo.count(op2) != 0) {
				cls = true;
				break;
			}
		}
		
		if(cls) {
			for(int j = 0; j <= i; j++) {
				myList[j] = '#';
			}
		}
	}
	
	string res = "[";
	for(int i = 0; i < N; i++) {
		if(myList[i] != '#') {
			res += myList[i];
			res += ", ";
		}
	}
	
	int sz = res.length();
	if( res[sz-1] == ' ' ) {
		res = res.substr(0,sz-2);
	}
	res += "]";
	printf("%s\n",res.c_str());
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();
	
	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
}

int main()
{
	solve();
	return 0;
}
