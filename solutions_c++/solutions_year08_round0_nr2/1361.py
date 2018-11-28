#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int N, NA, NB, T;
vector<string> A, B;


inline string turnaround(const string& arrival) {
    int h, m; sscanf(arrival.c_str(), "%d:%d", &h, &m);
    char tmp[16]; sprintf(tmp, "%02d:%02d", (h*60+m+T)/60, (m+T)%60);
    return tmp;
}


int main() {
    scanf("%d", &N);
    for (int tc=0; tc<N; tc++) {
        scanf("%d%d%d", &T, &NA, &NB);
        
        A.clear(); B.clear();
        
        while (NA-->0) {
            char tmpa[16]; scanf("%s", tmpa);
            char tmpb[16]; scanf("%s", tmpb);
            A.push_back(string(tmpa)+'-');
            B.push_back(turnaround(tmpb)+'+');
        }
            
        while (NB-->0) {
            char tmpb[16]; scanf("%s", tmpb);
            char tmpa[16]; scanf("%s", tmpa);
            B.push_back(string(tmpb)+'-');
            A.push_back(turnaround(tmpa)+'+');
        }
        
        sort(A.begin(), A.end()); // '+'  <  '-'
        sort(B.begin(), B.end()); // '+'  <  '-'
        
        int resultA=0, currA=0;
        for (int i=0; i<int(A.size()); i++) {
            if (A[i][5]=='+') currA++;
            else currA--;
            resultA=min(resultA, currA);
        }
    
        int resultB=0, currB=0;
        for (int i=0; i<int(B.size()); i++) {
            if (B[i][5]=='+') currB++;
            else currB--;
            resultB=min(resultB, currB);
        }
        
        printf("Case #%d: %d %d\n", tc+1, -resultA, -resultB);
    }
    
    return 0;
}

