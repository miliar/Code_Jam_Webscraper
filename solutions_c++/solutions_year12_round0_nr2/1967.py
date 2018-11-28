#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>

using namespace std;

vector <int> lst;

bool within(int a, int b, bool surprise) {

    if (!surprise)    return (0<=a <=10 && 0<=b<=10 && abs(b-a)<=1);
    else return (0<=a <=10 && 0<=b<=10 && abs(b-a)==2);
}

bool within(int a, int b, int c) {

    return (0<=a <=10 && 0<=b<=10&& 0<=c<=10);
}



int find(int surN, int quanlify) {

    int quanPair = 0;
    int sursofar = 0;
    bool surprise = false;
    for (int i = 0; i< lst.size(); i++) {
        //cout << "0";
        int num=lst.at(i);
        //  cout << "num is "<<num<< endl;
        int contest = min(num, 10);

        while(contest >= quanlify&&num>=contest&& num>=quanlify) {

            if ((num-contest)%2 == 0 && within((num-contest)/2,contest,surprise)) break;

            else if (within(num - contest*2, contest,surprise)) break;

            contest = contest-1;
        }

        if (contest >= quanlify&&num>=contest&& num>=quanlify) quanPair++;
        else {
            surprise=true;
            contest = min(num, 10);
            while(contest >= quanlify&&num>=contest&& num>=quanlify) {

                if ((num-contest)%2 == 0 && within((num-contest)/2,contest,surprise)) break;

                else if (within(num - contest*2, contest,surprise)) break;

                else if (contest *3 -3 == num && within(contest, contest-2, contest-1)) {
                    break;
                }
                contest = contest-1;
            }

            if (contest >= quanlify&&num>=contest&& num>=quanlify) sursofar++;

        }
        surprise=false;


    }

    return quanPair+min(sursofar, surN);

}

int main() {

    int cases;
    int googlerN;
    int surNum;
    int scorelim;
    int score;
    cin >> cases;
    for (int i = 1; i<= cases; i++) {
        cin >> googlerN;
        cin >> surNum;
        cin >> scorelim;
        lst.clear();

        for (int j = 1; j<=googlerN; j++) {
            cin >> score;
            lst.push_back(score);
        }
        cout << "Case #" << i<<": "<<find(surNum, scorelim) << endl;
    }


    return 0;
}

