#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char** argv)
{
    int caseNo;
    cin >> caseNo;
    for(int curCase = 1; curCase <= caseNo; curCase++)
    {
        int newNum = 0;
        std::string num;
        cin >> num;
        map<char , long double> chart;

        for(string::iterator iter = num.begin(); iter != num.end(); iter++)
        {
            if ( chart.find( *iter ) == chart.end() )
            {
                if ( newNum == 0 )
                {
                    chart[*iter] = static_cast<long double>(1);
                    newNum++;
                }
                else if ( newNum == 1 )
                {
                    chart[*iter] = static_cast<long double>(0);
                    newNum++;
                }
                else
                {
                    chart[*iter] = static_cast<long double>(newNum);
                    newNum++;
                }
            }
        }

        long double order = static_cast<long double>(newNum);
        long double total = 0.0;
        long double mul = 1.0;
        for(string::reverse_iterator iter = num.rbegin(); iter != num.rend(); iter++)
        {
            total += chart[*iter] * mul;
            //cout <<"total : " << total << "chart : (" << *iter << ","<<chart[*iter]<< ") " << " mul : " << mul << endl;; // XXX
            mul = mul * order;
        }
        printf("Case #%d: %.0Lf\n", curCase, total);

    } // end - for

} // end - main
