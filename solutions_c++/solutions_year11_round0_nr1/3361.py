// Bot Trust-- Google Code Jam 2011 //
/*
Note : Nothing to say...
Alex
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>

using namespace std;
typedef unsigned long int uli;

struct order
{
    string color;
    uli button;
};

struct c // one case
{
    uli N;
    vector<order> orderList;
};

uli nextOrder(string color, uli orderState, c *currentCase)
{
    uli i=orderState;

    while ( currentCase->orderList.at(i).color != color )
    {
        i++;
        if (i==currentCase->N)
            return 0;
    }

    return currentCase->orderList.at(i).button;
}


int main()
{
    string inputFileName; // Here is what we need
    string outputFileName;
    uli T;
    vector<c> cases;
    vector<uli> output;

    cout << "Name of input file : "; // Asking for the input file
    cin >> inputFileName;

    ifstream iFile(inputFileName.c_str(), ios::in); // & trying to open it
    if(iFile)
    {
            string currentLine;
            cout << "Reading ..." << endl << endl;
            iFile >> T;
            cout << T << " cases will folow..."<<endl << endl;

            for (uli i=0;i<T;i++)
            {
                c currentCases;
                iFile >> currentCases.N;
                order currentOrder;
                for (uli j=0;j<currentCases.N;j++)
                {
                    iFile >> currentOrder.color >> currentOrder.button;
                    currentCases.orderList.push_back(currentOrder);
                }
                cases.push_back(currentCases);
            }
        iFile.close();

        cout << "Processing..." << endl;


        for (uli c_count=0;c_count<T;c_count++)  // For each cases
        {
            cout << "Case : " << c_count <<endl;
            c currentCases;
            currentCases = cases.at(c_count);

            uli time=0;
            uli orderState=0;
            uli OPos=1;
            uli BPos=1;

            while (orderState<currentCases.N)
            {
                //cout << "Time..." << time << endl;
                uli currentOrderState=orderState;

                uli OTarget = nextOrder("O",orderState,&currentCases);
                uli BTarget = nextOrder("B",orderState,&currentCases);

                if (OTarget != OPos) //Is the Orange Bot ready for the next button ?
                {
                    if (OTarget > OPos) //If not, we are moving
                        OPos++;
                    else
                        OPos--;
                    //cout << "O Moving : " << OPos << endl;
                }
                else if (currentCases.orderList.at(currentOrderState).color == "O")  //Is it the turn of the orange robot to push ?
                {
                    orderState++;   // if yes, we push the button aka passing to the next order
                    //cout << "O Pushing : " << OPos << endl;
                }

                if (BTarget != BPos) //Is the Blue Bot ready for the next button ?
                {
                    if (BTarget > BPos) //If not, we are moving
                        BPos++;
                    else
                        BPos--;
                    //cout << "B Moving : " << BPos << endl;
                }
                else if (currentCases.orderList.at(currentOrderState).color == "B")  //Is it the turn of the Blue robot to push ?
                {
                    orderState++;
                    //cout << "B Pushing : " << BPos << endl;
                }
                time++;
            }


            output.push_back(time);
        }


        cout << "Name of output file : ";   // Asking for output file
        cin >> outputFileName;

        ofstream oFile(outputFileName.c_str(), ios::out | ios::trunc);
        if(oFile)
        {
                for (uli i=0;i<cases.size();i++)
                {

                    oFile << "Case #" << i+1 << ": " << output.at(i) << endl;
                }

                oFile.close();
        }
        else
        {
            cout << "Unable to open the output file : " << outputFileName.c_str() << endl;
        }


    }
    else
    {
         cout << "Unable to open the input file : " << inputFileName.c_str() << endl;
    }


    cout << "Exiting ..." << endl;
    return 0;
}
