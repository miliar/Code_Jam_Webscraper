#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#define M 1010
using namespace std;
vector <int> s;
int m[30][30];
int fg[30][30];
int main()
{
	int t,cas = 0;
	//freopen("./c.in","r",stdin);
	//freopen("./cc.out","w",stdout);
	cin>>t;
	while(t--){
		int c,d,n;
		for(int i = 0; i < 30; ++i)
			for(int j = 0; j < 30; ++j){
				m[i][j] = -1;
				fg[i][j] = 0;
			}
		s.clear();
		cin>>c;
		while(c--){
			string ss;
			cin>>ss;
			int index1 = ss[0] - 'A';
			int index2 = ss[1] - 'A';
			int index3 = ss[2] - 'A';
			if(m[index1][index2] < 0){
				m[index1][index2] = index3;
				m[index2][index1] = index3;
			}
		}
		cin>>d;
		while(d--){
			string ss;
			cin>>ss;
			int index1 = ss[0] - 'A';
			int index2 = ss[1] - 'A';
			fg[index1][index2] = 1;
			fg[index2][index1] = 1;
		}
		cin>>n;
		string ss;
		cin>>ss;
		for(int i = 0; i < n; ++i){
			s.push_back(ss[i] - 'A');
		}
		for(int i = 1; i < n; ++i){
			int j = i-1;
			while(j>=0 && s[j] == 100) --j;
			if(j < 0)
				continue;
			if(s[j] < 26){
				if(m[s[i]][s[j]] >= 0){
					s[i] = m[s[i]][s[j]];
					s[j] = 100;
					--i;
					continue;
				}			
			}
			for(j = 0; j < i; ++j){
				if(s[j] == 100)
					continue;
				if(fg[s[i]][s[j]] == 1){
					for(int k = 0; k <= i; ++k)
						s[k] = 100;
				}
			}
		}
		
		cout<<"Case #"<<++cas<<": [";
		int i = 0;
		for(i = 0; i < n; ++i){
			if(s[i] < 26){
				printf("%c",s[i++]+'A');
				break;
			}
		}
		for(; i < n; ++i){
			if(s[i] < 26){
				printf(", %c",s[i]+'A');
			}
		}
		cout<<"]"<<endl;
	}
	return 0;
}

