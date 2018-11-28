#include <iostream>
#include <algorithm>

using namespace std;

void solve(){
    long long R, k;
    int N;
    cin >> R >> k >> N;
    long long g[N];

    for(int i=0; i<N; i++){
        cin >> g[i];
    }

    long long people1[N];
    int next1[N];
    long long people1k[N];
    int next1k[N];

    // Simulate one ride
    for(int i=0; i<N; i++){
        long long seats = k;
        int next = i;

        while(true){
            if(seats < g[next]) break;
            seats -= g[next];
            next = (next + 1) % N;
            if(next == i) break;
        }
        people1[i] = k - seats;
        next1[i] = next;
    }

    // Simulate many rides
    int manyRides = 300;
    for(int i=0; i<N; i++){
        long long people = 0;
        int next = i;
        for(int j=0; j<manyRides; j++){
            people += people1[next];
            next = next1[next];
        }
        people1k[i] = people;
        next1k[i] = next;
    }

    // Run for input
    long long runs = R;
    long long profit = 0;
    long long next = 0;
    while(runs >= manyRides){
        profit += people1k[next];
        next = next1k[next];
        runs -= manyRides;
    }
    while(runs > 0){
        profit += people1[next];
        next = next1[next];
        runs--;
    }
    cout << profit;
    return;
}

int main(){
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }

    return 0;
}
