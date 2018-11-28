#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
typedef string::iterator sitr;
string wel="welcome to code jam";
string tri="welcom tdja";

void trim(string& str,string w){
	size_t pos=0;
	for(;;){
		pos=str.find_first_not_of(w,pos);
		if(pos==string::npos)break;
		str.erase(pos,1);
	}
}

int search(string& str,int pos,int next){
	char ch=wel[next];
	size_t idx=str.find_first_of(ch,pos);

	// 見つからなかった
	if(idx==string::npos) return 0;

	// 次に検索すべき文字
	int c2;
	if(next==(int)wel.size()-1){
		c2=1;
	}
	// 次の文字を判定する
	else {
		c2=search(str,idx+1,next+1);
	}

	// ほかの選び方を探す
	int c1=search(str,idx+1,next);

	return (c1+c2)%10000;
}

int main(){
	string text;
	getline(cin,text);
	int n=atoi(text.c_str());
	for(int t=1;t<=n;t++){
		getline(cin,text);
		trim(text,wel);
		cout<<"Case #"<<t<<": ";
		int c=search(text,0,0);
		printf("%04d\n",c);
	}
	return 0;
}


