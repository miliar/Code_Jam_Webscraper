#include <iostream>

using namespace std;

int R, k, N;

int main() {
    int cases;
    int groups[1001];
    int money;
    cin >> cases;
    for(int c = 1; c<=cases; c++) {
        money = 0;
        cin >> R >> k >> N;
        for(int i=0; i<N; i++) cin >> groups[i];

        int index = 0;
        int people = 0;
        int money = 0;
        int s=0;
        for(int r=0; r<R; r++) {
            people = 0;
            s=index;
            if(people+groups[index] > k) 
                break;
            people += groups[index++];
            index %= N;
            while(people <=k && index != s) {
                if(people+groups[index] > k) 
                    break;
                people += groups[index++];
                index %= N;
            }
            money += people;
        }
        cout<<"Case #"<<c<<": "<<money<<endl;
    }
}
