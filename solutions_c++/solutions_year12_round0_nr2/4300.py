#include<iostream>
#define MAXN 100
int points[MAXN];

using namespace std;

int solve(int N, int S, int p){
    int ans=0;

    for(int i=0; i<N; i++){
        if(points[i]/3 >= p)
            ans++;
        else if(points[i] % 3 > 0 && points[i]/3 + 1 >= p)
            ans++;
        else if(points[i] % 3 == 2 && points[i]/3 + 2 >= p && S > 0){
            ans++;
            S--;
        }
        else if(points[i] % 3 == 0 && points[i] > 0 && points[i]/3 + 1 >=p && S > 0){
            ans++;
            S--;
        }
        else {}


    }
    return ans;
}

int main(){
int T, N, S, p;

cin >> T;

for(int i=1; i<=T; i++){
    cin >> N >> S >> p;
    for(int j=0; j<N; j++)
        cin >> points[j];
    cout << "Case #" << i << ": ";
    cout << solve(N, S, p) << endl;

}
}
