#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int q=1; q<=t; q++) {
        vector <char> elementList;
        char combinations[30][30]={{0}};
        int opposites[30][30]={{0}};
        int count[30]={0};
        int c;
        cin >> c;
        for (int i=0; i<c; i++) {
            char x,y,z;
            cin >> x >> y >> z;
            combinations[x-'A'][y-'A']=z;
            combinations[y-'A'][x-'A']=z;
        }
        int d;
        cin >> d;
        for (int i=0; i<d; i++) {
            char x,y;
            cin >> x >> y;
            opposites[x-'A'][y-'A']=1;
            opposites[y-'A'][x-'A']=1;
        }
        int n;
        cin >> n;
        for (int i=0; i<n; i++) {
            char x,y;
            cin >> x;
            if (elementList.empty()) {
                elementList.push_back(x);
                count[x-'A']++;
                continue;
            }
            y = elementList.back();
            if (combinations[x-'A'][y-'A']) {
                elementList.pop_back();
                count[y-'A']--;
                elementList.push_back(combinations[x-'A'][y-'A']);
                count[combinations[x-'A'][y-'A']-'A']++;
            }
            else {
                elementList.push_back(x);
                count[x-'A']++;
            }

            x=elementList.back();
            for (int j=0; j<30; j++) {
                if (opposites[x-'A'][j] && count[j]) {
                    for (int k=0; k<30; k++) count[k]=0;
                    while(!elementList.empty()) elementList.pop_back();
                }
            }
        }
        cout << "Case #" << q << ": [";
        for (int i=0; i<(int)(elementList.size())-1; i++) cout << elementList[i] <<", ";
        if (!elementList.empty()) cout << elementList[elementList.size()-1];
        cout << "]" << endl;

    }
    return 0;
}
