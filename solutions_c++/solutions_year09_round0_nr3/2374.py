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

	// $B8+$D$+$i$J$+$C$?(B
	if(idx==string::npos) return 0;

	// $B<!$K8!:w$9$Y$-J8;z(B
	int c2;
	if(next==(int)wel.size()-1){
		c2=1;
	}
	// $B<!$NJ8;z$rH=Dj$9$k(B
	else {
		c2=search(str,idx+1,next+1);
	}

	// $B$[$+$NA*$SJ}$rC5$9(B
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


