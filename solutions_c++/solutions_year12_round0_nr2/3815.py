#include <iostream>

using namespace std;

int main()
{
    int t,n,s,p,tripleta;
    cin >> t;
    for (int c=0;c<t;c++) {
        cin>>n>>s>>p;
        int res=0;
        for (int c2=0;c2<n;c2++) {
            cin>>tripleta;

            if (((tripleta/3 + ((tripleta%3)?1:0)) >= p) &&
                ((tripleta/3 + ((tripleta%3)?1:0)) <= 10))
                res++;
            else if (tripleta > 1 && (tripleta/3+((tripleta%3)?1:0)+1)>=p && s!=0 &&
                    (tripleta/3+((tripleta%3)?1:0)+1) <= 10) {
                res++;
                s--;
            }
        }
        cout << "Case #" << c+1 << ": " << res << endl;
    }
}
