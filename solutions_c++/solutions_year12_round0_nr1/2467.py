#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))

string inp1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
string inp2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string inp3="de kr kd eoya kw aej tysr re ujdr lkgc jv";

string out1="our language is impossible to understand";
string out2="there are twenty six factorial possibilities";
string out3="so it is okay if you want to just give up";

int main(){

	map<char,char> code;
	rei(i,0,inp1.size()){
		code[inp1[i]]=out1[i];
	}
	rei(i,0,inp2.size()){
                code[inp2[i]]=out2[i];
        }
        rei(i,0,inp1.size()){
                code[inp3[i]]=out3[i];
        }
	code['z']='q';
	code['q']='z';
	int test;
	cin>>test;
	cin.ignore();
	ree(caseNo,1,test){
		string in="";
		getline(cin,in);
		
		rei(i,0,in.size()){
			in[i]=code[in[i]];
		}
		printf("Case #%d: ",caseNo);
		cout<<in<<endl;
	}
}






