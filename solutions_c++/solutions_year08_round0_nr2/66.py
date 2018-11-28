#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#define sqr(x) ((x)*(x))

using namespace std;

int main()
{
    int N;
    cin >> N;
    for(int cccccc=0;cccccc < N;++cccccc)
    {
        cout << "Case #" << cccccc+1 << ": ";

        // CODE
        vector<int> SAStart, SAEnd, SBStart, SBEnd;
        int NA, NB, T;
        cin >> T;
        cin >> NA >> NB;
        for (int i=0;i<NA;++i)
        {
            int st, en, hh, mm;
            string str;
            cin >> str;
            sscanf(str.c_str(), "%d:%d", &hh, &mm);
            st = hh * 60 + mm;
            cin >> str;
            sscanf(str.c_str(), "%d:%d", &hh, &mm);
            en = hh * 60 + mm;
            SAStart.push_back(st);
            SAEnd.push_back(en);
        }
        for (int i=0;i<NB;++i)
        {
            int st, en, hh, mm;
            string str;
            cin >> str;
            sscanf(str.c_str(), "%d:%d", &hh, &mm);
            st = hh * 60 + mm;
            cin >> str;
            sscanf(str.c_str(), "%d:%d", &hh, &mm);
            en = hh * 60 + mm;
            SBStart.push_back(st);
            SBEnd.push_back(en);
        }
        sort(SAStart.begin(), SAStart.end());
        sort(SAEnd.begin(), SAEnd.end());
        sort(SBStart.begin(), SBStart.end());
        sort(SBEnd.begin(), SBEnd.end());
        for (int i=0;i<SBEnd.size();++i)
        {
            for (vector<int>::iterator iter = SAStart.begin(); iter != SAStart.end(); ++iter)
            {
                if (*iter >= SBEnd[i] + T)
                {
                    SAStart.erase(iter);
                    break;
                }
            }
        }
        cout << SAStart.size() << " ";
        for (int i=0;i<SAEnd.size();++i)
        {
            for (vector<int>::iterator iter = SBStart.begin(); iter != SBStart.end(); ++iter)
            {
                if (*iter >= SAEnd[i] + T)
                {
                    SBStart.erase(iter);
                    break;
                }
            }
        }
        cout << SBStart.size() << endl;
        // END OF CODE
    }
    return 0;
}