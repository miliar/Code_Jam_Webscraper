#include <iostream>
#include <cmath>
using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	cin>>T;

	for(int t = 0; t < T; ++ t)
	{
		char combine[26 * 26];
		char opposed[26 * 26];
		memset(combine,0,sizeof(char) * (26 * 26));
		memset(opposed,0,sizeof(char) * (26 * 26));
		string st;
		int C,D,N;
		cin>>C;
		for(int i = 0; i < C; ++ i){
			char ch;
			int a,b,c;
			cin>>ch; a = ch - 'A';
			cin>>ch; b = ch - 'A';
			cin>>ch; c = ch - 'A';
			combine[a * 26 + b] = ch;
			combine[b * 26 + a] = ch;
		}
		cin>>D;
		for(int i = 0; i < D; ++ i){
			char ch;
			int a,b;
			cin>>ch; a = ch - 'A';
			cin>>ch; b = ch - 'A';
			opposed[a * 26 + b] = 1;
			opposed[b * 26 + a] = 1;
		}
		cin>>N;

		for(int i = 0; i < N; ++ i){
			char ch;
			cin>>ch;
			int chi = ch - 'A';
			if (st.size() > 0){
				if (combine[(st[st.size() - 1] - 'A') * 26 + chi] != 0){
					st[st.size() - 1] = combine[(st[st.size() - 1] - 'A') * 26 + chi];
				}
				else{
					bool f = true;
					for (int i = 0; i < st.size(); ++ i)
						if (opposed[(st[i] - 'A') * 26 + chi] == 1){
							st = "";f = false;break;
						}
					if (f) st += ch;
				}
			}else st = ch;
		}

		cout<<"Case #"<<t + 1<<": [";
		if (st.size() > 0){
			for(int i = 0; i < st.size()-1; ++ i)
				cout<<st[i]<<", ";
			cout<<st[st.size() - 1]<<"]"<<endl;
		}else cout<<"]"<<endl;
	}
	return 0;
}