#include <iostream>
#include <sstream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::stringstream;

unsigned long G[1000];
unsigned long Ac_Money[1000];

string int2str(int num);

int main()
{
    unsigned T_in, R_in, K_in;
    cin >> T_in;
    int N_in;
    unsigned R;
    unsigned prefix_Time, period_Time;
    unsigned long G_sum, cur_Sum, prefix_Sum, period__Sum, Money;
    int beg, end;
    unsigned CaseNum = 1;
    while(CaseNum <= T_in) {

        cin >> R_in >> K_in >> N_in;

        G_sum = 0;
        for(int i = 0; i < N_in; i++) {
            cin >> G[i];
            G_sum += G[i];
        }

        if(G_sum <= K_in)
            cout << "Case #" << CaseNum << ": " << (G_sum * R_in) << endl;
        else {
            string str;
            Money = 0;
            R = 0;
            beg = end = 0;
            while(R < R_in) {
                cur_Sum = 0;
                for(end = beg; cur_Sum <= K_in; end++) {
                    if(end >= N_in) end -= N_in;
                    cur_Sum += G[end];
                }
                end--;
                if(end < 0) end += N_in;
                cur_Sum -= G[end];
                end--;
                if(end < 0) end += N_in;

                string cur_Str = int2str(beg) + "-" + int2str(end) + " ";
                string::size_type found = str.find(cur_Str);

                if(found == string::npos) {
                    str += cur_Str;
                    beg = end + 1;
                    if(beg >= N_in) beg -= N_in;
                    Money += cur_Sum;
                    Ac_Money[R] = Money;
                    R++;
                } else {
                    prefix_Time = 0;
                    string prefix_Str = str.substr(0, found);
                    found = 0;
                    while( (found = prefix_Str.find(" ", found+1)) != string::npos)
                        prefix_Time++;
                    prefix_Sum = Ac_Money[prefix_Time-1];

                    period__Sum = Money - prefix_Sum;
                    period_Time = R - prefix_Time;

                    int period = (R_in - R) / period_Time;
                    Money += period * period__Sum;
                    R += period * period_Time;

                    str.clear();
                }
            }
            cout << "Case #" << CaseNum << ": " << Money << endl;
        }
        CaseNum++;
    }

    return 0;
}

string int2str(int num)
{
    stringstream ss;
    ss << num;
    return ss.str();
}
