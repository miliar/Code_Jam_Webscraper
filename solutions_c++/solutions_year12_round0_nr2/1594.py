// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;

int main()
{
	int tests;
    int googlers;
    int surprising;
    int minscore;

    int cutoffSafe;
    int cutoffSurprising;

    int sumSafe;
    int sumNeedsSurprising;

    int totalSum;

    int tmp;

	cin >> tests;
	for(int i = 1; i<=tests; i++){
	    sumSafe=0;
	    sumNeedsSurprising=0;
        cin >> googlers;
        cin >> surprising;
        cin >> minscore;

        cutoffSafe = minscore*3-2;
        cutoffSurprising = minscore*3-4;
        if(minscore==1){
            cutoffSurprising=1;
        }
        for(int j=0;j<googlers;j++){
            cin >> tmp;
            if(tmp>=cutoffSafe){
                sumSafe++;
            }else if(tmp>=cutoffSurprising){
                sumNeedsSurprising++;
            }
        }
        if(surprising >= sumNeedsSurprising){
            totalSum=sumSafe+sumNeedsSurprising;
        }else{
            totalSum=sumSafe+surprising;
        }
        cout << "Case #" << i << ": " << totalSum << endl;
	}
}

