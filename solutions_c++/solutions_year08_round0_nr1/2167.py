
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

using namespace std;

ofstream myOut("A-large.out");

void doCase(vector<string> engines, vector<string> queries, int I) {

    // Switches
    int numberOfSwitches = 0;


    // Find the latest engine name used
    string currentEngine;
    vector<string> notFound;
    vector<string>::iterator it;

    notFound = engines; // No engines are found

    // For every query
    for (it = queries.begin(); it < queries.end(); it++) {

        // If there is only engine left
        if (notFound.size() == 1 && *it == notFound.front()) {

            // Switch to it
            currentEngine = notFound.front();

            //cout << "    switch to: " << currentEngine << endl;

            // One more switch
            numberOfSwitches++;

            // Refresh the list
            //cout << "reset" << endl;
            notFound = engines;

            ////
            //vector<string>::iterator itt;
            //for (itt = notFound.begin() ; itt < notFound.end(); itt++)
                //cout << " " << *itt;
            //cout << endl;
            ////

            // Remove the current engine from the list
            vector<string>::iterator pos;
            pos = find(notFound.begin(), notFound.end(), currentEngine);
            //cout << "removed: " << *pos << endl;
            notFound.erase(pos);

            continue;
        } else {
            //cout << "no switch" << endl;
            //cout << " " << *it <<endl;
        }

        // Variables
        vector<string>::iterator pos;
        pos = find(notFound.begin(), notFound.end(), *it);

        // If the query has not been found yet
        if (pos != notFound.end()) {

            //cout << "removed: " << *pos << endl;

            // Remove it from the list
            notFound.erase(pos);
        }
    }

    cout << numberOfSwitches << endl;
    myOut << "Case #" << I + 1 << ": " << numberOfSwitches << endl;
}

int main(int argc, char *argv[]) {
    ifstream myFile("A-large.in");
    int caseNum, engNum, queNum;
    string ign;
    myFile >> caseNum;
    cout << "C: " << caseNum << endl;
    for (int caseI = 0; caseI < caseNum; caseI++) {
        vector<string> myEngines;
        myFile >> engNum;
        cout << "SENum: " << engNum << endl;
        getline(myFile, ign);
        for (int engI = 0; engI < engNum; engI++) {
            string temp;
            getline(myFile, temp);
            myEngines.push_back(temp);
            cout << " SE: " << temp << endl;
        }
        vector<string> myQueries;
        myFile >> queNum;
        getline(myFile, ign);
        cout << "QUNum: " << queNum << endl;
        for (int queI = 0; queI < queNum; queI++) {
            string temp;
            getline(myFile, temp);
            myQueries.push_back(temp);
            cout << " QU: " << temp << endl;
        }
        doCase(myEngines, myQueries, caseI);
    }
    return 0;
}
