#include <iostream>
#include <vector>
using namespace std;

struct Depart {
    int sta, end;
    int from;
    
    Depart(int from) {
        this->from = from;   
    }
};

bool departComp(Depart a, Depart b) {
    return a.sta < b.sta;   
}

int main() {
    int cases;
    cin >> cases;
    for(int caseCount=0; caseCount<cases; caseCount++) {
        int t, na, nb, tmp1, tmp2;
        char tmp3;
        vector<Depart> departs;
        vector<int> trains[2] = {vector<int>(), vector<int>()};
        
        cin >> t >> na >> nb;

        for(int i=0; i<na; i++) {
            Depart d(0);
            cin >> tmp1 >> tmp3 >> tmp2; 
            d.sta = tmp1*60+tmp2;
            cin >> tmp1 >> tmp3 >> tmp2; 
            d.end = tmp1*60+tmp2+t;
            departs.push_back(d);
        }
        for(int i=0; i<nb; i++) {
            Depart d(1);
            cin >> tmp1 >> tmp3 >> tmp2;
            d.sta = tmp1*60+tmp2;
            cin >> tmp1 >> tmp3 >> tmp2; 
            d.end = tmp1*60+tmp2+t;
            departs.push_back(d);
        }

        sort(departs.begin(), departs.end(), departComp);                
        
        int tX[2] = {0,0};
        
        for(int i=0; i<departs.size(); i++) {
            Depart d = departs[i];
            if (trains[d.from].size()>0 && trains[d.from][0] <= d.sta) {
                trains[d.from].erase(trains[d.from].begin());   
            } else {
                tX[d.from]++;   
            }
            trains[1-d.from].push_back(d.end);
            sort(trains[1-d.from].begin(), trains[1-d.from].end());
        }

        cout << "Case #" << caseCount+1 << ": " << tX[0] << " " << tX[1] << endl;
    }
}
