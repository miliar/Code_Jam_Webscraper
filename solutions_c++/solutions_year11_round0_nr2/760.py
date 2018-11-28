#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <hash_map>

using namespace std;
const int MNAX=100;
char alf[8] = {'Q','W','E','R','A','S','D','F'};

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int test;
	cin>>test;
	for (int t=1;t<=test;++t){
		string ans = "";
		char zamena[8][8];
		int rem[8][8];
		int c,d,n,i,j;
		for (i=0;i<8;++i){
			for (j=0;j<8;++j){
				zamena[i][j] = '-';
				rem[i][j] = 0;
			}
		}
		cin>>c;
		for (int ic=0;ic<c;++ic){
			string s;
			cin>>s;
			for (i=0;i<8;++i){
				if (alf[i]==s[0]){
					for (j=0;j<8;++j){
						if (alf[j]==s[1]){
							zamena[i][j] = s[2];
							zamena[j][i] = s[2];
						}
					}
				}
			}
		}
		cin>>d;
		for (int id=0;id<d;++id){
			string s;
			cin>>s;
			for (i=0;i<8;++i){
				if (alf[i]==s[0]){
					for (j=0;j<8;++j){
						if (alf[j]==s[1]){
							rem[i][j]=1;
							rem[j][i]=1;
						}
					}
				}
			}
		}
		cin>>n;
		for (int ni=1;ni<=n;++ni){
			char ch;
			cin>>ch;

			if (ans=="") ans+=ch;
			else{
				bool bl=false;
				for (i=0;i<8;++i){
					if (ans[ans.length()-1]==alf[i]){
						for (j=0;j<8;++j){
							if (ch==alf[j]){
								if (zamena[i][j]!='-'){
									ans[ans.length()-1] = zamena[i][j];
									bl = true;
								}
							}
						}
					}
				}

				if (!bl){
					for (int ia=0;ia<ans.length();++ia){
						for (i=0;i<8;++i){
							if (ans[ia]==alf[i]){
								for (j=0;j<8;++j){
									if (ch==alf[j]){
										if (rem[i][j]==1){
											ans = "";
											bl = true;
											break;
										}
									}
								}
								if (ans=="") break;
							}
						}
						if (ans=="") break;
					}
					if (!bl) ans += ch;
				}
			}


		}

		cout<<"Case #"<<t<<": [";
		if (ans!=""){
			for (i=0;i<(ans.length()-1);++i) 
				cout<<ans[i]<<", ";
			cout<<ans[ans.length()-1];
		}
		cout<<"]"<<endl;
	}
	return 0;
}
