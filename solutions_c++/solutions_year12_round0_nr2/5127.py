#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream file;
    file.open("input.in");
    int cases;
    file>>cases;
    ofstream fileout;
    fileout.open("output.in");
    for(int tempo=0;tempo<cases;tempo++)
    {
    int goog,spec,min,score[100],count_ans,count_spec;
    file>>goog>>spec>>min;
    for(int temp=0;temp<goog;temp++)
    file>>score[temp];
    count_ans=0;
    count_spec=0;
    for(int temp=0;temp<goog;temp++)
    {
        int sc,rem;
        sc = score[temp]/3;
        rem = score[temp] - sc*3;
        if(rem == 0)
        {
            if(sc >= min)
            count_ans++;

            else if(sc == min-1 && count_spec<spec && sc>0)
            {
                count_spec++;
                count_ans++;
            }
        }

        else if(rem == 1)
        {
            if(sc>=min || sc == min-1)
            count_ans++;
        }

        else if(rem==2)
        {
            if(sc>=min || sc == min-1)
            count_ans++;

            else if(sc == min-2 && count_spec<spec && sc > 0)
            {
                count_spec++;
                count_ans++;
            }
        }
    }
    fileout<<"Case #"<<(tempo+1)<<": "<<count_ans<<"\n";
    }
    fileout.close();
    file.close();
    return 0;
}
