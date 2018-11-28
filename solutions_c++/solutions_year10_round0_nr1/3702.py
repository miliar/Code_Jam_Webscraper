#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int main()
{
    ifstream i;
    ofstream o;

    int sapper_no;
    int clicked;
    int case_no(0);
    int tem;




    i.open("sample.txt");
    o.open("answer.txt");
    i >> case_no;

    cout << case_no<<endl;
    for(int j = 0 ; j < case_no ; j++)
    {
        i >> sapper_no >> clicked;

        cout << sapper_no << clicked<<endl;

        clicked++;


        sapper_no = pow(2,sapper_no);

        tem = clicked % sapper_no;


        if(tem == 0)
            o << "Case #"<<j+1<<": ON"<<endl;
        else
            o << "Case #"<<j+1<<": OFF"<<endl;
    }

    o.close();
    i.close();

    return 0;
}
