#include<iostream>
#include<cstdlib>
#include<string>
#include<vector>
#include<algorithm>
#include<cassert>
#include<cstdio>
using namespace std;

#define TYPE string
#define ARR_SZ(arr) sizeof(arr)/sizeof(TYPE)
#define ARR_TO_VEC(arr,vec) { \
for(int i=0;i<ARR_SZ(arr);i++) \
        vec.push_back(arr[i]);\
}

bool doesExist(const string&,const string&, const int wsize);

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int wordSize,dictLength,checkListLength;
	vector<string> dict, checkList;
	cin>>wordSize>>dictLength>>checkListLength;

	for(int i=0;i<dictLength;i++) {
		string temp;
		cin>>temp;
		dict.push_back(temp);
	}

	for(int i=0;i<checkListLength;i++) {
		string temp;
		cin>>temp;
		checkList.push_back(temp);
	}

	for(int i=0;i<checkListLength;i++) {
		int count = 0;
		for(int j=0;j<dictLength;j++) {
			if(doesExist(checkList[i],dict[j],wordSize))
				count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}

bool doesExist(const string &sample, const string &dict,const int wsize) {
	int i = 0;
	int j = 0;

	while(j < wsize) {
		if(sample[i]=='(') {
			while(sample[++i] != dict[j] && sample[i] != ')')
				;
			if(sample[i]==')')
				return false;
			while(sample[++i]!=')')
				;
			j++;
			i++;
		}
		else {
			if(sample[i]!=dict[j])
				return false;
			i++;
			j++;
		}
	}
	return true;
}