#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<queue>

using namespace std;

int main()
{
    int T;
    cin>>T;

    ofstream fout("square.out");

    //testcases
    for(int t = 1; t <= T; ++t){
        
        cout<<t<<endl;

        //reading input
        int W,Q;
        cin>>W>>Q;

        vector<string> board(W,"");
        for(int i = 0; i < W; ++i) cin>>board[i];

        fout<<"Case #"<<t<<":"<<endl;

        vector< vector< vector<string> > > visited(W,vector< vector<string> >(W,vector<string>(4000,"")));

        //starts the computing
        for(int q = 0; q < Q; ++q){
            int sum;
            cin>>sum;

            vector<string> solutions;

            //reseting visited
            for(int i = 0; i < W; ++i){
                for(int k = 0; k < W; ++k){
                    for(int m = 0; m < 4000; ++m) visited[i][k][m] = "";
                }
            }

            queue< vector<int> > next;

            vector<int> info(3,0);

            for(int i = 0; i < W; ++i){
                for(int k = 0; k < W; ++k){
                    if(board[i][k] != '-' && board[i][k] != '+'){
                        info[0] = board[i][k]-'0';
                        info[1] = i; 
                        info[2] = k;
                        next.push(info);
                        visited[i][k][(int)(board[i][k]-'0') + 2000] = string(1,board[i][k]);
                        
                        if(info[0] == sum) solutions.push_back(string(1,board[i][k]));
                    }
                }
            }
            
            //solution of length one
            if(!solutions.empty()) fout<<sum<<endl;

            //find solution
            else{
                bool quit = false;
                while(!quit){
                    info = next.front();
                    next.pop();
                    int s = info[0],
                        i = info[1],
                        k = info[2];

                    //cout<<s<<" "<<i<<" "<<k<<endl;
                    
                    //try all moves
                    for(int i_step = -1; i_step < 2; ++i_step){
                        for(int k_step = -1; k_step < 2; ++k_step){
                            if(i_step != 0 && k_step != 0) continue;
                            if(i_step == 0 && k_step == 0) continue;

                            int I = i+i_step,
                                K = k+k_step,
                                S = s;

                            //valid move
                            if(I >= 0 && K >= 0 && I < W && K < W){
                               
                                string sol = visited[i][k][s+2000];
                                
                                //if number
                                if(board[I][K] != '-' && board[I][K] != '+'){
                                    if(sol[sol.size()-1] == '+') S += board[I][K] - '0';
                                    else S -= board[I][K] - '0';
                                }

                                sol.push_back(board[I][K]);
                                //cout<<sol.size()<<endl;

                                //found a solution
                                if(S == sum){
                                    if(!solutions.empty() && solutions[0].size() < sol.size()) quit = true;
                                    solutions.push_back(sol);
                                }

                                //better move
                                if(visited[I][K][S+2000] == "" || visited[I][K][S+2000] > sol){
                                    visited[I][K][S+2000] = sol;
                                    vector<int> temp(3,0);
                                    temp[0] = S;
                                    temp[1] = I;
                                    temp[2] = K;
                                    next.push(temp);
                                }
                            }
                        }
                    }
                }
                string best = solutions[0];
                for(int i = 0; i < solutions.size(); ++i) if(best > solutions[i]) best = solutions[i];
                fout<<best<<endl;
            }
        }
    }

    return 0;
}
