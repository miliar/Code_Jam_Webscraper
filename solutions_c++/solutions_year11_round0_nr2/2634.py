#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 1010
#define datat int
#define ansdatat int

int n;

string cha_to[maxn], opp[maxn];

char ch[10000];
map<pair<char,char> , char> mcha;
map<pair<char,char> , int> mopp;

void init_deal(){
	mopp.clear();
	mcha.clear();
}

int main(){
	
	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		init_deal();
		
		char sta[maxn];
		pair<char, char> p_ch;

		int tc;
		scanf("%d", &tc);
		for(int i = 1;i<=tc;i++){
			scanf("%s", ch);
			cha_to[i] = ch;
			p_ch = make_pair(ch[0],ch[1]);
			mcha[p_ch] = ch[2];
			p_ch = make_pair(ch[1],ch[0]);
			mcha[p_ch] = ch[2];
//			cout<<cha_to[i]<<endl;
		}

		int topp;
		scanf("%d", &topp);
		for(int i = 1;i<=topp;i++){
			scanf("%s", ch);
			opp[i] = ch;
			p_ch = make_pair(ch[0],ch[1]);
			mopp[p_ch] = 1;
			p_ch = make_pair(ch[1],ch[0]);
			mopp[p_ch] = 1;
			
//			cout<<opp[i]<<endl;
		}
		int nn;
		scanf("%d", &nn);
		scanf("%s", ch);
		string s = ch;
//		cout<<s<<endl;

		int top = 0;
		for(int i = 0;i<nn;i++){
			top++;
			sta[top] = s[i];
			while(true){
				if(top>1){
					p_ch = make_pair(sta[top-1],sta[top]);
					if(mcha.find(p_ch) != mcha.end()){
						char n_ch = mcha[p_ch];
						top--;
						sta[top] = n_ch;
					}
					else{
						break;
					}
				}
				else{
					break;
				}
			}

			for(int j = 1;j<=top;j++)
				for(int k = j+1;k<=top;k++){
				p_ch = make_pair(sta[j], sta[k]);
				if(mopp[p_ch] == 1){
					top = 0;
					break;
				}
			}


		}

		


		printf("Case #%d: [",ttt);
		if(top>0){
			printf("%c", sta[1]);
			for(int i = 2;i<=top;i++){
				printf(", %c", sta[i]);
			}
		}
		printf("]\n");



	}
	

	return 0;
};

