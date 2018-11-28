

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <iostream>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <string>
#include <complex>
#include <functional>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <fstream>
using namespace std;

/*bool cmp(const acm &A, const acm &B)
{
	if(A.x < B.x) return true;
	if(B.x < A.x) return false;
	if(A.y < B.y) return true;
	return false;
	if(A.m>B.m)return true;
	if(A.m<B.m)return false;
	if(A.t<B.t)return true;
	if(A.t>B.t)return false;
	if(A.n<B.n)return true;
	return false;
}*/

int t;//testCast;
int c,d,n;
int top;
//string combine[64];
vector<string>combine;
//string oppose[32];
vector<string>oppose;
string result;
char stack[128];


void readin(){
	result.clear();
	combine.clear();
	oppose.clear();
	scanf("%d",&c);
	string tmp;
	for(int i=0;i<c;i++){
		cin>>tmp;
		combine.push_back(tmp);
	}
	scanf("%d",&d);
	for(int i=0;i<d;i++){
		cin>>tmp;
		oppose.push_back(tmp);
	}
	scanf("%d",&n);
	cin>>result;
	//for()
}

void check_combine(){
	
	if(top-1<0)return;
	for(int i=0;i<combine.size();i++){
		if ((stack[top]==combine[i][0]&&stack[top-1]==combine[i][1])||
			(stack[top]==combine[i][1]&&stack[top-1]==combine[i][0])){
			//stack[top]=NULL;
			stack[--top]=combine[i][2];
			return;
		}
	}

}
void check_oppose(){

	//for(int i=0;i<top;i++){
	for(int i=top-1;i>=0;i--){
		for(int j=0;j<oppose.size();j++){
			if ((stack[i]==oppose[j][0]&&stack[top]==oppose[j][1])||
				(stack[i]==oppose[j][1]&&stack[top]==oppose[j][0])){
				//while(top>=i)
					//top--;
					top=-1;
				//continue;
				return;
			}
		}
	}

}

void solve(){
	/*int num=result.size();
	for(int i=1;i<num;i++){
		for(int j=0;j<combine.size();i++){
			if((result[i]==combine[j][0]&&
				result[i-1]==combine[j][1])||
				(result[i]==combine[j][1]&&
				result[i-1]==combine[j][0]))
		}
	}*/

	top=-1;

	//for(int i=0;i<n;i++)
	//	stack[i]=NULL;
	int num=result.size();
	for(int i=0;i<num;i++){
		stack[++top]=result[i];
		check_combine();
		check_oppose();
	}

}

int main() {
	freopen("D:/B-large.in","r", stdin);
	freopen("D:/B-large.out", "w", stdout);

	while(scanf("%d",&t)!=EOF){
		for(int cast=1;cast<=t;cast++){
			readin();
			solve();
			printf("Case #%d: ",cast);
			if(top<0)printf("[]\n");
			else {
				printf("[");
				for(int i=0;i<top;i++)
					printf("%c, ",stack[i]);
				printf("%c]\n",stack[top]);
			}
		}
	}

    //printf("hello\n");
    return 0;
}






