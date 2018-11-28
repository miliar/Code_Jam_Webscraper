#include<iostream>
#include<vector>

using namespace std;

int hex(char a){
    if('0' <= a && a <= '9') return a-'0';
    else return a-'A' + 10;
}

int main()
{
    int T; cin>>T;
    for(int t = 1; t <= T; ++t){
        int M,N;
        cin>>M>>N;

        vector< vector<bool> > board(M,vector<bool>(N,false));

        for(int i = 0; i < M; ++i){
            string s; cin>>s;

            for(int k = 0; k < s.size(); ++k){
                int x = hex(s[k]);

                int pos = 0;
                while(x > 0){
                    board[i][(1+k)*4-pos-1] = (x%2 != 0);
                    x /= 2;
                    ++pos;
                }
            }
        }

        /*for(int i = 0; i < M; ++i){
            for(int k = 0; k < N; ++k){
                cout<<board[i][k];
            }
            cout<<endl;
        }

        return 0;
        */

        vector<int> ans(520, 0);
        vector< vector<bool> > used(M,vector<bool>(N,false));

        for(int size = min(N,M); size > 0; --size){
            for(int i = 0; i + size <= M; ++i){
                for(int k = 0; k + size <= N; ++k){
                   
                    //if(size == 6) cout<<"pos: "<<i<<" "<<k<<endl;
                    
                    bool valid = true;
                    for(int a = 0; a < size && valid; ++a){
                        
                        if((a != 0 && board[i+a][k] == board[i+a-1][k]) || used[i+a][k]) {
                            //if(size == 6 && i == 0 && k == 13) cout<<"error1"<<endl;
                            valid = false;
                        }
                        for(int b = 1; b < size && valid; ++b){
                            if(board[i+a][k+b] == board[i+a][k+b-1] || used[i+a][k+b]){
                                valid = false;
                                //if(size == 6 && i == 0 && k == 13){
                              //      cout<<"error2 "<<i+a<<" "<<k+b<<endl;
                                  //  if(used[i+a][k+b]) cout<<"used"<<endl;
                                //}
                            }
                        }
                    }

                    //if(valid && size == 6) cout<<"VALID!!"<<endl;
                    if(valid){
                        ++ans[size];
                        for(int a = 0; a < size; ++a){
                            for(int b = 0; b < size; ++b){
                                used[i+a][k+b] = true;
                            }
                        }
                    }
                }
            }
        }

        int diff = 0;
        for(int i = 0; i < ans.size(); ++i){
            if(ans[i] != 0) ++diff;
        }

        cout<<"Case #"<<t<<": "<<diff<<endl;
        for(int i = ans.size()-1; i >= 0; --i){
            if(ans[i] != 0) cout<<i<<" "<<ans[i]<<endl;
        }
    }

    return 0;
}
