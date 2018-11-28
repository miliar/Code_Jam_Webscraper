#include<iostream>
#include<cstdio>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;
int cnt;
char word[19]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};

void correct(vector<char> &str, int w, int cur){
	if(w==19)	cnt++;
	else if(str[cur]=='\n')	return;
	else if(word[w]==str[cur]){
		correct(str,w+1,cur+1);
		correct(str,w,cur+1);
	}
	else	correct(str,w,cur+1);
}

int main(void){
	int n;
	char c;
	cin>>n;
	getchar();
	for(int index=0;index<n;index++){
		cnt=0;
		vector<char> str;
		while(c=getchar()){
			str.push_back(c);
			if(c=='\n')	break;
		}
		for(int jndex=0;jndex<str.size();jndex++){
			if(str[jndex]==word[0])	correct(str,1,jndex+1);
		}
		cout<<"Case #"<<index+1<<": ";
		if(cnt/1000==0)	cout<<0;
		if(cnt/100==0)	cout<<0;
		if(cnt/10==0)		cout<<0;
		cout<< cnt <<endl;
	}
	return 0;
}
