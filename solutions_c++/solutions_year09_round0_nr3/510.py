#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;

//ifstream fin("c.in");
//#define cin fin

string rule = "welcome to code jam";
map<int,int> scaned;
int wCount(int cur, int rCur, string p){
		int curPos = cur*100 + rCur;
		if(scaned.find(curPos)==scaned.end()){ //use DP method to accelerate
				int sum = 0;
				int size = p.size() + rCur + 1 - rule.size(); //if p is less than rule, impossible
				for(int i = cur; i<size; i ++){
						if(p[i] == rule[rCur]){
								if(rCur == rule.size()-1)
										sum ++;
								else{
										int temp = wCount(i+1, rCur+1, p);
										//if(temp == 0) //when run in ubuntu, it cost more time
										//		break;
										sum += temp;
								}
						}
				}
				scaned[curPos]=sum%10000; // %10000 in case of int overflow
				return scaned[curPos];
		}
		return scaned[curPos];
}

char result[5];//case output message
char orig[] = "0000";
char* wFormat(int n){//format to 00xx format
		memcpy(result,orig,5); //init to 0000
		for(int i = 3; n > 0; i --){
				result[i] = '0'+n%10;
				n/=10;
		}
		return result;
}
int main(){
		int n;
		string p;
		cin>>n;
		getline(cin,p); //eat the \n of the first line
		for(int i = 1; i <= n; i ++){
				getline(cin,p);
				scaned.clear();
				cout<<"Case #"<<i<<": "<<wFormat(wCount(0,0,p))<<endl;
		}
		return 0;
}
