#include <iostream.h>
#include <fstream>
#include <string.h>
#include <sstream>

using namespace std;



int calc(int ** scores, int N, int S, int p) {
    int total = 0;
    int mS = S; // modified S
    
    int v1 = (3 * p) - 2;
    int v2 = (3 * p) - 3;
    int v3 = (3 * p) - 4;
    

    if (v3 < 0)
       v3 = 0;
    
    for(int i = 0; i < N; i++){
           if (v1 <= (*scores)[i]) { // it is a target so add
              if (p == 0 || v1 != 0){
                total++;
              }
           }
           else if ((v2 == (*scores)[i]) && mS != 0) {
                if (p == 0 || v2 != 0){
                    total++;
                    mS--;     
                }
           }
           else if ((v3 == (*scores)[i]) && mS != 0) {
                if (p == 0 || v3 != 0){
                    total++;
                    mS--;     
                }
           }
    }
    

    
    
    
    return total;
}


int main() {
    ifstream myReadFile;
    ofstream myWriteFile;
    string output, exitVal;
    myReadFile.open("test.in"); // change it to the name of file *****
    myWriteFile.open("output.txt");
    int * scores;
    // read in T
    int T, N, S, p, curr, result;
    myReadFile >> T; // the number of times to loop
    
    // for buffer to read by line
    getline(myReadFile, output); // remove additional portion 

    //myReadFile >> output;
    
    for (int i = 0; i< T; i++){
        // get the next line of input
        myReadFile >> N;
        myReadFile >> S;
        myReadFile >> p;
        
        scores = new int[N];
        // load all scores into the array
        for (int j = 0; j < N; j++) {
            myReadFile >> curr;
            scores[j] = curr; 
           
        }
        
        // go through all cases
        result = calc(&scores, N, S, p);
        //getline(myReadFile, output);    
        //newVal = conv(output);
        myWriteFile << "Case #" << i+1 << ": " << result << endl;
        getline(myReadFile, output);
        delete [] scores;
    }

    // read in each entry
    /*
    for (int i= 0; i < T; i++) {
          getline(myReadFile,output);
          cout << "CASE #" << i+1 << ": " << checkHappyLine(output) << endl;
          //cout << output << endl;
          
    }
    */
    
    cout << "DONE" << endl;
    cin >> exitVal;
}
