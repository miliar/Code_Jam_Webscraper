#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

struct CombinedElement {
    char A;
    char B;
    char C;
};

struct OpposedElement {
    char A;
    char B;
};

int main (void) {
    int testCases = 0;
    int willCombine = 0;
    int willOppose = 0;
    int i = 0;
    int currentTest = 0;
    int numberOfElements = 0;
    int didCombine = 0;
    string input;

    ifstream fileInput("input.in");
    ofstream fileOutput("output.txt");

    if (fileInput.is_open()) {
        fileInput >> input;
        istringstream stream(input);
        stream >> testCases;
    }

    for (currentTest = 0; currentTest < testCases; currentTest++) {

    if (fileInput.is_open()) {
        fileInput >> input;
        istringstream stream(input);
        stream >> willCombine;
    }

    CombinedElement *combine = new CombinedElement[willCombine];

    for (i = 0; i < willCombine; i++) {
        fileInput >> input;
        combine[i].A = input[0];
        combine[i].B = input[1];
        combine[i].C = input[2];
    }

    if (fileInput.is_open()) {
        fileInput >> input;
        istringstream stream(input);
        stream >> willOppose;
    }

    OpposedElement  *oppose = new OpposedElement[willOppose];

    for (i = 0; i < willOppose; i++) {
        fileInput >> input;
        oppose[i].A = input[0];
        oppose[i].B = input[1];
    }

    fileInput >> input;
    istringstream stream(input);
    stream >> numberOfElements;

    char *elements = new char[numberOfElements];
    int Place = 0;
    Place++;

    fileInput >> input;

    if (numberOfElements >= 2) {

    elements[0] = input[0];
    elements[1] = input[1];
    didCombine = 0;
    for (i = 0; i < willCombine; i++) {
        if ((combine[i].A == elements[0] && combine[i].B == elements[1]) || (combine[i].B == elements[0] && combine[i].A == elements[1])) {
            Place--;
            elements[0] = combine[i].C;
            didCombine = 1;
            break;
        }
    }
    if (didCombine == 0) {
        for (i = 0; i < willOppose; i++) {
            if ((oppose[i].A == elements[0] && oppose[i].B == elements[1]) || (oppose[i].B == elements[0] && oppose[i].A == elements[1])) {
                Place = -1;
            }
        }
    }

    int j;


    for (i = 2; i < numberOfElements; i++) {
        Place += 1;
        elements[Place] = input[i];
        didCombine = 0;
        for (j = 0; j < willCombine; j++) {
            if ((combine[j].A == elements[Place - 1] && combine[j].B == elements[Place]) || (combine[j].B == elements[Place - 1] && combine[j].A == elements[Place])) {
                Place--;
                elements[Place] = combine[j].C;
                didCombine = 1;
                break;
            }
        }
        if (didCombine == 0) {
            int k;
            for (k = 0; k < Place; k++) {
                for (j = 0; j < willOppose; j++) {
                    if ((oppose[j].A == elements[k] && oppose[j].B == elements[Place]) || (oppose[j].B == elements[k] && oppose[j].A == elements[Place])) {
                        Place = -1;
                        break;
                    }
                }
            }
        }
    }
    cout << "Case #" << (currentTest + 1) << ": [";
    fileOutput << "Case #" << (currentTest + 1) << ": [";
    for (i = 0; i < Place; i++) {
        cout << elements[i];
        fileOutput << elements[i];
        cout << ", ";
        fileOutput << ", ";
    }
    if (Place >= 0) {
    cout << elements[Place];
    fileOutput << elements[Place];
    }
    cout << "]" << endl;
    fileOutput << "]" << endl;
    } else if (numberOfElements == 1) {
        cout << "Case #" << (currentTest + 1) << ": [";
        fileOutput << "Case #" << (currentTest + 1) << ": [";
        cout << input[0];
        fileOutput << input[0];
        cout << "]" << endl;
        fileOutput << "]" << endl;
    }   else if (numberOfElements == 0) {
        cout << "Case #" << (currentTest + 1) << ": [";
        fileOutput << "Case #" << (currentTest + 1) << ": [";
        cout << "]" << endl;
        fileOutput << "]" << endl;
    }

    delete combine;
    delete oppose;
    delete elements;
    }




}
