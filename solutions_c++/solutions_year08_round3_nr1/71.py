#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;



int main()
{
    int T;
    scanf("%d\n", &T);
    for(int t = 0; t<T; t++) {
        int P, K, L;
        cin >> P >> K >> L;
        vector<int> f;
        for (int i = 0; i < L; i++) {
            int n;
            cin >> n;
            f.push_back(n);
        }
        sort(f.begin(),f.end());
        reverse(f.begin(), f.end());
        long long res = 0;
        for (int i = 0, count = 1; i < L; i += K, count++) {
            long long sum = 0;
            for (int j = i; j < i + K && j < L; j++) {
                sum += f [j];
            }
            res += sum * count;
        }
        cout << "Case #" << t+1 << ": " << res << endl;
   }
   return 0;
}
   
        

            
