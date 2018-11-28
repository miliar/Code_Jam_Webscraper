#include <iostream>
#include <vector>

using namespace std;


bool opposed[50][50];
char combine[50][50];

int main() {
    int cases;
    cin >> cases;

    for(int c=0; c<cases; c++) {
        memset(opposed,0,sizeof(opposed));
        memset(combine,0,sizeof(combine));

        int C, D, N;
        cin >> C;
        for(int i=0; i<C; i++) {
            char from1, from2, to;
            cin >> from1 >> from2 >> to;
            combine[from1-'A'][from2-'A'] = to;
            combine[from2-'A'][from1-'A'] = to;
        }
            
        cin >> D;
        for (int i=0; i<D; i++) {
            char opp1, opp2;
            cin >> opp1>>opp2;
            opposed[opp1-'A'][opp2-'A'] = 1;
            opposed[opp2-'A'][opp1-'A'] = 1;
        }

        cin >> N;
        string res = "";
        char invoked;
        for(int i=0; i<N; i++) {
            cin >> invoked;
            //cout << "INVOKE: " << invoked<<endl;

            if (res.size() > 0 && combine[res[res.size()-1]-'A'][invoked-'A']) {
                //cout << "   COMBINE!"<<endl;
                res = res.substr(0, res.size()-1) + combine[res[res.size()-1]-'A'][invoked-'A'];
            }
            else {
                bool areOp = false;
                for(int j=0; j<res.size(); j++) {
                    if(opposed[res[j]-'A'][invoked-'A']) areOp = true;
                }

                if (areOp) { res = "";}
                else res += invoked;
            }
            //cout << "RES:"<<res<<endl;
        }

        cout << "Case #" <<(c+1) << ": [";
        for(int i=0; i<res.size(); i++) {
            if (i>0) cout << ", ";
            cout << res[i];
        }
        cout<< "]" << endl;
    }
}
