#include "../include/Dance.h"
#include <stdio.h>

using namespace std;

Dance::Dance()
{
    //ctor
}

Dance::~Dance()
{
    //dtor
}


void Dance::Process(ifstream& in, ofstream& out) {
    int num;
    in >> num;
    int count;

    //string line;
    for (count = 0; count < num; ++count) {
        out << "Case #" << count + 1 << ": ";
        int n, s, p;
        in >> n >> s >> p;
        int supprise_count = 0;
        int threshold1, threshold2;
        switch(p) {
            case 0:
                threshold2 = 0;
                threshold1 = 0;
                break;
            case 1:
                threshold2 = 1;
                threshold1 = 1;
                break;
            default:
                threshold2 = (p - 1) * 3 - 1;
                threshold1 = threshold2 + 2;
                break;
        }
        int count1 = 0;
        int count2 = 0;
        for (int i = 0; i < n; ++i) {
            int v;
            in >> v;
            if (v >= threshold1) count1 ++;
            else if (v >= threshold2) count2 ++;
        }
        if (count2 > s) count2 = s;
        out << count1 + count2 << endl;
    }
}
