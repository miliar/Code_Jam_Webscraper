#include<iostream>
#include<set>
#include<string>
#include<vector>

using namespace std;



int main(void){
    int T;
    cin>>T;
    vector<string> P(4);
    for(int tcase = 1; tcase <= T; ++tcase){
        for (int i=0;i<4;++i) cin>>P[i];
        string res = "Draw";
        bool full = true;
        for(char CH = 'O'; CH <= 'X'; CH += 'X'-'O'){
        //rows
        for(int i=0;i<4;++i){
            int sum = 0;
            for(int j=0;j<4;++j){
                if (P[i][j] == CH || P[i][j] == 'T') ++sum;
                full &= P[i][j]!='.';
            }
            if(sum==4) res = CH+string(" won");
        }
        //columns
        for(int i=0;i<4;++i){
            int sum = 0;
            for(int j=0;j<4;++j){
                if (P[j][i] == CH || P[j][i] == 'T') ++sum;
            }
            if(sum==4) res = CH+string(" won");
        }
        //diagonals
        int sum = 0;
        for(int j=0;j<4;++j){
            if (P[j][j] == CH || P[j][j] == 'T') ++sum;
        }
        if(sum==4) res = CH+string(" won");
        
        sum = 0;
        for(int j=0;j<4;++j){
            if (P[3-j][j] == CH || P[3-j][j] == 'T') ++sum;
        }
        if(sum==4) res = CH+string(" won");
        
        }
        
        if(res=="Draw" && !full) res = "Game has not completed";
                
        
        cout<<"Case #"<<tcase<<": "<<res<<endl;
    }
}
