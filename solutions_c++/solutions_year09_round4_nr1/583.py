#include<iostream>
#include<vector>
#include<string>
#include<fstream>
#include<queue>
#include<set>

using namespace std;

int value(const string& s){
    for(int i = s.size()-1; i >= 0; --i){
        if(s[i] == '1') return i;
    }
}

void print(const vector<int>& vec){
    for(int i = 0; i < vec.size(); ++i){
        cout<<vec[i]<<" ";
    }
    cout<<endl;
}

int main()
{

    int T;
    cin>>T;

    ofstream fout("a.out");

    for(int t = 0; t < T; ++t){
        
        //input
        int N;
        cin>>N;
        
        vector<int> data(N,0);

        for(int n = 0; n < N; ++n){
            string line;
            cin>>line;
            data[n] = value(line);
        }

        //compute
        int moves = 0;

        for(int i = 0; i < N; ++i){
            if(data[i] <= i) continue;

            for(int k = i+1; k < N; ++k){
                if(data[k] <= i){
                    for(int m = k; m > i; --m){
                        int temp = data[m];
                        data[m] = data[m-1];
                        data[m-1] = temp;
                        ++moves;
                    }
                    break;
                }
            }
        }

        //output
        fout<<"Case #"<<t+1<<": "<<moves<<endl;

    }

    return 0;
}

