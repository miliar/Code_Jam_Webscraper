#include <iostream>

using namespace std;

int main(){


	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int t = 0; t < T; ++ t){
		int N,M;
		cin>>N>>M;
		string dic[10000];
		string list[100];
		bool pass[10000];
		bool app[10000];
		char ch[10000];
		for(int i = 0; i < N; ++ i){
			cin>>ch;dic[i] = ch;
		}
		for(int j = 0; j < M; ++ j){
			cin>>ch;list[j] = ch;
		}
		
		
		cout<<"Case #"<<t+1<<":";
		for(int h = 0; h < M; ++ h){
			int minint = -1;
			string minst = "";
			for(int i = 0; i < N; ++ i){
				int minus =0;
				int passcount = 0;
				memset(pass,0,sizeof(bool) * 10000);
				memset(app,0,sizeof(bool) * 10000);
				
				
				for(int j = 0; j < N; ++ j)
					if (dic[j].length() != dic[i].length()){
						pass[j] = true; ++ passcount;
					}
				
				
					
				for(int j = 0; j < list[h].length(); ++ j){
					////////cai bucai ////////
					bool cai = false;
					for(int k = 0; k < N; ++ k)
						if (!pass[k]){
							for(int l = 0; l < dic[k].length(); ++ l){
								if (dic[k][l] == list[h][j] && !app[l]){
									cai = true; break;
								}
							}
							if (cai) break;
						}
					if (!cai) continue;
					char caich = list[h][j];
					//////////bian bu bina/////
					bool appbian = false;
					for(int l = 0; l < dic[i].length(); ++ l){
						if (dic[i][l] == list[h][j]){
							app[l] = true;
							appbian = true;
						}
					}
					if (!appbian) ++ minus;
					//////////pai bu pai /////
					for(int k = 0; k < N; ++ k)
						if (!pass[k]){
							bool paidiao = false;
							for(int l = 0; l < dic[k].length(); ++ l){
								if ((dic[k][l] == list[h][j] && !app[l])||(app[l] && dic[k][l] != dic[i][l])){
									paidiao = true; break;
								}
							}
							if (paidiao){
								pass[k] = true; ++ passcount;
							}
						}
					
					if (passcount == N - 1) break;
				}//end for j list[h].length()

				if (minus > minint){
					minint = minus;
					minst = dic[i];
				}
			
			}//end for i N
			cout<<" "<<minst.c_str();
		}
		cout<<endl;
	}


	return 0;
}