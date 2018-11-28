#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n-1;i>=0;i--)

int main(){
	string tmp;
	int T;
	cin >> T;
	rep(NN,T){
		int C,D;
		
		cin >> C;
		char graph[128][128] = {0};
		bool del[128][128] = {0};
		rep(i,C){
			cin >> tmp;
			graph[tmp[0]][tmp[1]] = graph[tmp[1]][tmp[0]] = tmp[2];
		}
		
		cin >> D;
		rep(i,D){
			cin >> tmp;
			del[tmp[0]][tmp[1]] = del[tmp[1]][tmp[0]] = true;
		}
		int N;
		cin >> N;
		stack<char> st;
		
		char memo[999];
		rep(i,N){
			char c; cin >> c;
			if(st.size()){
				char tp = st.top();
				if(graph[tp][c] != 0){
					st.pop();
					st.push(graph[tp][c]);
				}else st.push(c);
			}else st.push(c);
			
			memo[st.size()-1] = st.top();
			rev(j,st.size()-1){
				if(del[memo[j]][memo[st.size()-1]]){
					while(st.size()) st.pop();
					break;
				}
			}
		}
		string view;
		while(st.size()){view+=st.top();st.pop();}
		reverse(view.begin(),view.end());
		cout << "Case #" << NN+1 << ": [" ;
		rep(i,view.size()) cout << (i?", ":"") <<  view[i]; 
		cout << "]" << endl;
	}
}