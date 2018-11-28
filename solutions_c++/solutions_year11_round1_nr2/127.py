#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solve(vector<string> dict, string list) {
    int maxi=-1;
    string r;
    for (int i=0; i<dict.size(); i++) {
        int contain[26]={0};
        int left[100]={0};
        int leftnum=0,point=0;
        for (int j=0; j<dict[i].size(); j++) {
            contain[dict[i][j]-'a']=1;
        }
        for (int j=0; j<dict.size(); j++) {
            if (dict[i].size()==dict[j].size()) {
            left[j]=1;
            leftnum++;
            }
        } 
        for (int j=0; j<list.size(); j++) {
            if (leftnum==1)break;
            int cand[26]={0};
            int candn=0;
            for (int k=0; k<dict.size(); k++) {
                if (left[k]==0)continue;
                for (int l=0; l<dict[k].size(); l++) {
                    if(cand[dict[k][l]-'a']==0)candn++;
                    cand[dict[k][l]-'a']=1;
                }
            }
            if (cand[list[j]-'a']==0)continue;
            if (contain[list[j]-'a']==0)point++;
            int pos[10]={0};
            for (int k=0; k<dict[i].size(); k++) {
                if (dict[i][k]==list[j])pos[k]=1;
            }
            for (int k=0; k<dict.size(); k++) {
                if (left[k]==0)continue;
                int flg=1;
                for (int l=0; l<dict[i].size(); l++) {
                    if (pos[l]==0&&dict[k][l]==list[j] ||
                        pos[l]==1&&dict[k][l]!=list[j]) {
                        flg=0;
                        break;
                    }
                }
                if (flg==0) {
                    left[k]=0;
                    leftnum--;
                }
            }
        }
        if (point > maxi) {
            maxi = point;
            r = dict[i];
        }
    }
    return r;
}

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int n,m;
        vector<string> dict;
        string tmp;
        cin >> n >> m;
        for (int j=0; j<n; j++) {
            cin >> tmp;
            dict.push_back(tmp);
        }
        cout << "Case #" << i+1 << ":";
        for (int j=0; j<m; j++) {
            string list;
            cin >> list;
            cout << " " << solve(dict,list); 
        }
        cout << endl;
    }
    return 0;
}
