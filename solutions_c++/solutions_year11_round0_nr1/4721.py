#include <iostream>
#include <list>
#include "InputReader.h"
#include "Sequence.h"

using namespace std;


int main()
{
    int rc = 1;
    int time;
    int counter = 0;

    InputReader* pin = new InputReader("A-large.in");
    Sequence* pseq = new Sequence();
    string strSequence;
    int nTc = pin->GetTotalTestCases();
//    cout<<nTc<<endl;
    //pin->Read_and_Print();
    while(rc > 0 )
    {
//        cout<<" loop "<<counter;
        rc = pin->Get_Next_Sequence(strSequence);
        if(rc < 0)
        {
//           cout<<"Stream ended"<<endl;
        }

        else
        {
//           cout<<strSequence<<endl;
           counter++;
           pseq->fillList(strSequence);
//           pseq->PrintList();
           time = pseq->CalculateTime();
           cout<<"Case #"<<counter<<": "<<time<<endl;
           strSequence.clear();
        }
    }
    if(counter != nTc)
    {
       cout<<"All test cases didn't execute "<<counter<<endl;
    }

    delete pin;
    delete pseq;
    return 0;
}
