#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>

using namespace std;

vector <int> lst;
bool within(int a, int b) {

    return (0<=a <=10 && 0<=b<=10 && abs(b-a)<=1 );
}

bool within2(int a, int b) {

    return (0<=a <=10 && 0<=b<=10 && abs(b-a)==2 );
}
bool within(int a, int b, int c) {

    return (0<=a <=10 && 0<=b<=10&& 0<=c<=10);
}



int find(int nsur, int quanlify) {


    int maxsofar = 0;
    int sursofar = 0;

    for (int i = 0; i< lst.size(); i++) {
        //cout << "0";
        int num=lst.at(i);
      //  cout << "num is "<<num<< endl;
        int contest = min(num, 10);
      //  cout << "c is "<<contest << endl;

// quanlify only
        while(contest >= quanlify&&num>=contest&& num>=quanlify) {
            //cout << "contest now is " << contest << endl;
            if ((num-contest)%2 == 0 && within((num-contest)/2,contest)) {
               // cout << "break1 at " << contest << endl;
                break;
            }

            else if (within(num - contest*2, contest)) {
               // cout << "break2 at " << contest << endl;
                break;
            }

            contest = contest-1;
        }

        if (contest >= quanlify&&num>=contest&& num>=quanlify) maxsofar ++;
        else {


            contest = min(num, 10);

            while(contest >= quanlify&&num>=contest&& num>=quanlify) {
               // cout << "contest now is " << contest << endl;
                if ((num-contest)%2 == 0 && within2((num-contest)/2,contest)) {
                   // cout << "break1 at " << contest << endl;
                    break;
                }

                else if (within2(num - contest*2, contest)) {
                   // cout << "break2 at " << contest << endl;
                    break;
                }

                else if (contest *3 -3 == num && within(contest, contest-2, contest-1)) {
                   // cout << "break3 at " << contest << endl;
                    break;
                }

                contest = contest-1;
            }


            if (contest >= quanlify&&num>=contest&& num>=quanlify) sursofar++;

        }

// get surprise
       // cout << "sursofar is " << sursofar<< endl;
        //cout << "maxsofar is " << maxsofar << endl<<endl;
    }

    return maxsofar+min(sursofar, nsur);

}

int main() {

    int num;
    int ncontestants;
    int nsur;
    int qua;
    int n;
cin >> num;
    for (int i = 1; i<= num; i++) {
        cin >> ncontestants;
        cin >> nsur;
        cin >> qua;
        lst.clear();

        for (int j = 1; j<=ncontestants; j++) {
            cin >> n;
            lst.push_back(n);
        }
        cout << "Case #" << i<<": "<<find(nsur, qua) << endl;
    }


    return 0;
}

