//*******************************************
// Author: Samuel Jero
// Email: samuel.jero@gmail.com
// Date: 9/12/2009
//*******************************************
#include <string>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <sstream>
#include <cctype>
#include <limits>
#include <limits.h>
using namespace std;


void calc(string cur,string tmp, bool begin);
std::string int2str(long n);
long str2int(const std::string &str);


long num;
long next;
string str_num;


int main(){
	int testcases;
	cin>>testcases;
	
	for(int i=1; i <= testcases; i++){
		next=LONG_MAX;
		cin>>num;
		str_num=int2str(num);
		calc(str_num, "", true);
		cout<<"Case #"<<i<<": "<<next<<endl;
	}
return 0;
}

void calc(string cur, string build, bool begin){
	string temp;
	string b_tmp;
	string t_re;
	long re;
	if(cur==""){
		//cout<<"test"<<endl;
		re=str2int(build);
		//cout<<"con"<<endl;
		if((re > num)&&(re < next)){
			next=re;
		}
		else{
			if(build.length() <= str_num.length()){
				temp=cur;
				b_tmp=build;
				b_tmp+='0';
				//cout<<"      "<<temp<<" "<<b_tmp<<endl;
				calc(temp,b_tmp,false);
			}
		}
		return;
	}
	//cout<<cur<<endl;
	for(unsigned int i=0; i < cur.length(); i++){
	//cout<<"loop"<<endl;
		if(cur[i]=='0'){
			cur.erase(cur.begin()+i);
			i--;
			continue;
		}
		if(begin==true){
			string t=int2str(num);
			if(t[0] < cur[i]){
				continue;
			}
		}
		temp=cur;
		temp.erase(temp.begin()+i);
		//cout<<"Temp: "<< temp<<endl;
		b_tmp=build;
		b_tmp.push_back(cur[i]);
		//cout<<"      "<<temp<<" "<<b_tmp<<endl;
		calc(temp,b_tmp, false);
	}
	if(build.length() <= str_num.length()){
		temp=cur;
		b_tmp=build;
		b_tmp+='0';
		//cout<<"      "<<temp<<" "<<b_tmp<<endl;
		calc(temp,b_tmp,false);
	}
return;
}

std::string int2str(long n){
	std::stringstream ss;
	ss << n;
return ss.str();
}

long str2int(const std::string &str){
	std::stringstream ss(str);
	long n;
	ss >> n;
return n;
}
