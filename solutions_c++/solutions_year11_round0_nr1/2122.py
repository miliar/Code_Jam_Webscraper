#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

#define pb push_back
#define fs first
#define sc second

using namespace std;

vector <pair<int, int> > buttons;
vector <int> buttonsOrange;
vector <int> buttonsBlue;

int main(void){
    int test, ntest;
    scanf ("%d", &test);

    ntest = test;
    while ( test--){

        int n, tmp;
        char buff[5];

        scanf ("%d", &n);
        buttons.clear();
        buttonsBlue.clear();
        buttonsOrange.clear();

        for (int i=0;i<n;++i){
            scanf ("%s %d", buff, &tmp);
            buttons.pb(make_pair(tmp,((buff[0] == 'O') ? 0 : 1)));
            if ( buff[0] == 'O') buttonsOrange.pb(tmp);
            else buttonsBlue.pb(tmp);
        }
        int indexOrange = 0, indexBlue=0, cnt = 0, posOrange=1, posBlue=1;

        for (int i=0;i<buttons.size();++i){
            int delta = abs(buttons[i].fs - ((buttons[i].sc == 0) ? posOrange : posBlue)) + 1;
            cnt+=delta;

            if ( buttons[i].sc == 0 ){
                posOrange = buttons[i].fs;
                ++indexOrange;

                if ( posBlue <= buttonsBlue[indexBlue])
                    posBlue=min(posBlue+delta, buttonsBlue[indexBlue]);
                else
                    posBlue=max(posBlue-delta, buttonsBlue[indexBlue]);

            }else{
                posBlue = buttons[i].fs;
                ++indexBlue;
                if ( posOrange <= buttonsOrange[indexOrange])
                    posOrange = min(posOrange+delta, buttonsOrange[indexOrange]);
                else
                    posOrange = max(posOrange-delta, buttonsOrange[indexOrange]);
            }
        }
        printf ("Case #%d: %d\n",ntest-test, cnt);
    }


    return 0;
}
