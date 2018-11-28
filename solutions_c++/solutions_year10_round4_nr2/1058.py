#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

struct Tr {
    int c;
    bool t;
    Tr* l;
    Tr* r;
    Tr* par;
};

int N;

vector<pair<int,int> > par(int n, int size, int P) {
    vector<pair<int,int> > ret;
    ret.push_back(make_pair(0,0));     
    int min = 0;
    int max = size;
    for(int i = 0; i < P - 1; ++i) {
        int piv = (min + max) / 2;
        if(n < piv) {
            max = piv;
            ret.push_back(make_pair(ret.back().first+1,ret.back().second*2));
        } else {
            min = piv;
            ret.push_back(make_pair(ret.back().first+1,ret.back().second*2+1));
        }
    }
    return ret;
}

int main() {
    cin>>N;

    for(int Case = 1; Case <= N; ++Case) {
        int P;
        cin>>P;
        int nc = 1<<P;
        int ncc = nc;

        vector<int> M(nc);
        
        for(int j = 0; j < nc; ++j) {
            cin>>M[j];
            M[j] = P - M[j];
        }

        vector<vector<int> > L;

        ncc /= 2;
        while(ncc != 0) {
            L.resize(L.size() + 1);
            for(int i = 0; i < ncc; ++i) {
                int ni;
                cin>>ni;
                L.back().push_back(ni);
            }
            ncc /= 2;
        }

        reverse(L.begin(),L.end());

        /*
        for(int i = 0; i < M.size(); ++i) {
            
        }
        */

        /*
        for(int i = 0; i < 8; ++i) {
            vector<pair<int,int> > p = par(i,M.size(),P);
            for(int j = 0; j < p.size(); ++j) cout<<p[j].first<<" "<<p[j].second<<endl;
        }
        */

        set<pair<int,int> > taken;
        int cost = 0;

        for(int i = 0; i < nc; ++i) {
            //cout<<"nc:; "<<i<<endl;
            vector<pair<int,int> > vp = par(i,nc,P);
            int ind = 0;
            while(M[i] > 0) {
                if(ind == vp.size()) break;
                if(!taken.count(vp[ind])) {
                    cost += L[vp[ind].first][vp[ind].second];
                    int p = nc / (1<<vp[ind].first);
                    int rd = p * vp[ind].second;
                    int ru = p * (vp[ind].second + 1);
                    //cout<<"vp:"<<endl;
                    //cout<<vp[ind].first<<" "<<vp[ind].second<<" "<<rd<<" "<<ru<<endl;
                    for(int j = rd; j < ru; ++j) {
                        M[j]--;
                    }
                    taken.insert(vp[ind]);
                }
                ++ind;
            }
            for(int a = 0; a < M.size(); ++a) {
                //cout<<M[a]<<" ";
            }
            //cout<<endl;
        }

        printf("Case #%d: %d\n",Case,cost);
    }

    return 0;
}
