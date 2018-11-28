#include<iostream>
#include<cstdlib>
#include<map>
using namespace std;

map<string,int>m;

int main(){
	int T,N,M;
	string str;
	char ch[4096];
	int cnt = 0;
	int tmp_ch;
	int ch_cnt=0;


	cin >> T;
	
	for(int i=0;i<T;i++){
		m.clear();
		cnt = 0;
		scanf("%d %d ",&N,&M);
		for(int j=0;j<N;j++){
			ch_cnt = 0;
			tmp_ch=1;
			for(;tmp_ch!='\n';){
				tmp_ch=getchar();
				ch[ch_cnt++] = tmp_ch;
				ch[ch_cnt] = 0;
				if(ch_cnt != 1 && (tmp_ch=='/'||tmp_ch=='\n')){
					ch[ch_cnt-1]='/';
					str = ch;
					m[str]++;
					//cout << "resist" << str << endl;
				}
			}
		}
		for(int j=0;j<M;j++){
			ch_cnt = 0;
			tmp_ch=1;
			for(;tmp_ch!='\n';){
				tmp_ch=getchar();
				ch[ch_cnt++] = tmp_ch;
				ch[ch_cnt] = 0;
				if(ch_cnt != 1 && (tmp_ch=='/'||tmp_ch=='\n')){
					ch[ch_cnt-1]='/';
					str = ch;
					if(m[str] == 0){
						m[str]++;
						cnt++;
						//cout << "new resist" << str << endl;
					}
				}
			}
		}
		

		printf("Case #%d: %d\n",i+1,cnt);
	}
		
		
	
	return 0;
}
