#include <iostream>

using namespace std;

int main()
{
    int n, it =1;
    int T, S, p, tot;
    int count, mod, bandmod=0;
    int score;
    cin>>T;
    while(T)
    {
        cin >> n; cin >> S; cin >> p;
        count = bandmod = mod = score = 0;

        for( int i=0 ; i<n ; i++ )
        {
            cin >> tot;
            if(tot > 0)
            {
            score = tot/3;
            mod = tot%3;
            if(mod > 0)
            {
                score ++;
                bandmod = 1;
            }
            if( score >= p )
            {
                count++;
            }
            else if(S > 0)
            {
                if(score+1 >= p)
                {
                    count++;
                    S--;
                }
            }
            }
            else if( tot == 0 && p == 0 )
                count++;
        }
        cout << "Case #" << it << ": " << count << endl;
        T--;
        it++;
    }
    return 0;
}
