#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int b=1,o=1;
        vector<int> bq,oq,q;
        int m;
        cin >> m;
        for (int j=0; j<m; j++) {
            int tmp;
            string col;
            cin >> col >> tmp;
            if (col=="B") {
                bq.push_back(tmp);
                q.push_back(tmp);
            } else {
                oq.push_back(tmp);
                q.push_back(100+tmp);
            }
        }
        int time=0;
        int bw=0,ow=0;
        while(q.size() != 0) {
            time++;
            if (q[0]>100) {
                if (o==oq[0]) {
                    ow=1;
                    q.erase(q.begin());
                    oq.erase(oq.begin());
                }
            } else {
                if (b==bq[0]) {
                    bw=1;
                    q.erase(q.begin());
                    bq.erase(bq.begin());
                }
            }
            if (bq.size()>0&&bw==0) {
                if (b<bq[0])b++;
                if (b>bq[0])b--;
            }
            if (oq.size()>0&&ow==0) {
                if (o<oq[0])o++;
                if (o>oq[0])o--;
            }
            bw=0;
            ow=0;
        }
        cout << "Case #" << i+1 << ": " << time << endl;
    }
    return 0;
}
