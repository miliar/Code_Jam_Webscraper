#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v;
char s[100];

bool Input(){
	scanf("%s",&s);
	v.clear();
	for(int i=0;s[i];++i){
		v.push_back(s[i]-'0');
	}
    return 1;
}

int Cmp(vector<int>& v1,vector<int>&v2){
	for(int i=0;i<(int)v1.size();++i){
		if(v1[i]<v2[i]) return -1;
		else if(v1[i]>v2[i]) return 1;
	}
	return 0;
}

void Proc(vector<int>& v){
	sort(v.begin(),v.end());
	int i=0;
	while(i<v.size()&&v[i]==0){
		++i;
	}
	swap(v[0],v[i]);
	return;
}

void Solve(int cn){
	if(!next_permutation(v.begin(),v.end())){
		v.push_back(0);
		Proc(v);
	}
	printf("Case #%d: ",cn);
	for(int i=0;i<v.size();++i){
		printf("%d",v[i]);
	}
	printf("\n");
    return;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("ans2.txt","w",stdout);
	int tn,id=0;
	scanf("%d",&tn);
	while(tn--){
		Input();
        Solve(++id);
    }
    return 0;
}
