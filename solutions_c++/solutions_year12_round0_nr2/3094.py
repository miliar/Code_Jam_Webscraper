#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i=1;i<=t;i++){
        int n,s,p;
        vector<int> baza;
        cin >> n >> s >> p;
        for (int j=0;j<n;j++) {
            int value;
            cin >> value;
            baza.push_back(value);
        }
    //    sort (baza.begin(), baza.end());
        int pewniaki=0;
        int mozliwe=0;

        for (int j=0;j<n;j++){
            if (baza[j] >= 3*p-2) pewniaki++;
            else if (baza[j] >= 3*p-4 && baza[j] > 0) mozliwe++;

        }
        int wynik;
        if (p==0) wynik=n;
        else {
            wynik=pewniaki+min(mozliwe,s);
        }

        cout << "Case #" << i << ": " << wynik << "\n";

    }

    return 0;
}
