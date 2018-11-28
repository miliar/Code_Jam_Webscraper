#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int sai (string s)
{
    stringstream ss(s);
    int h;
    ss >> h;
    char bas;
    ss >> bas;
    int m;
    ss >> m;
    return h*60+m;
}

int main()
{
    int N;
    cin >> N;
    for (int caso=1;caso<=N;caso++)
    {
        int T;
        cin >> T;
        vector <int> sa;
        vector <int> sb;
        vector <int> la;
        vector <int> lb;
        int NA,NB;
        cin >> NA >> NB;
        for (int i=0;i<NA;i++)
        {
            string s;
            cin >> s;
            int hr=sai(s);
            sa.push_back(hr);
            cin >> s;
            hr=sai(s);
            lb.push_back(hr+T);
        }
        for (int i=0;i<NB;i++)
        {
            string s;
            cin >> s;
            int hr=sai(s);
            sb.push_back(hr);
            cin >> s;
            hr=sai(s);
            la.push_back(hr+T);
        }
        sort(sa.begin(),sa.end());
        sort(la.begin(),la.end());
        sort(sb.begin(),sb.end());
        sort(lb.begin(),lb.end());
        int ta=NA;
        int tb=NB;
        int ia=0;
        int ib=0;
        for (int i=0;i<NA and ib<NB;i++)
        {
            if (sa[i]>=la[ib])
            {
                ib++;
                ta--;
            }
        }
        for (int i=0;i<NB and ia<NA;i++)
        {
            if (sb[i]>=lb[ia])
            {
                ia++;
                tb--;
            }
        }
        cout << "Case #" << caso << ": " << ta << " " << tb << endl;
    }
}
