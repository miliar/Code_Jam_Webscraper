#include <iostream.h>
#include <fstream>
#include <string.h>
#include <sstream>

using namespace std;

// converting base from 
// http://www.daniweb.com/software-development/cpp/code/217243
/*
string conv(int decimal, int base){
            if(decimal == 0) return "0";
            char NUMS[] = "0123456789ABCDEF"; // Characters that may be used
            std::string result = ""; // Create empty string ready for data to be appended
            do{
                result.push_back(NUMS[decimal%base]);
                // Append the appropriate character in NUMS based on the equation decimal%base
     
                decimal /= base; // Calculate new value of decimal
            }
            while(decimal != 0); // Do while used for slight optimisation
 
            return std::string(result.rbegin(), result.rend());
            // using std::string() constructer with iterators to reverse the string
 }

int checkHappyNum(int number, int base){
    string h;
    
     // digit variable
     int digit;
     int total = 0;
     int count = 0;
     string tempNumber = conv(number, base);
     string prevTempNum = "-1";
     string pprevTempNum = "-2";
     while (total != 1 && pprevTempNum != tempNumber) {
         total = 0;
         pprevTempNum = prevTempNum;
         prevTempNum = tempNumber;
         // loop through all digits
         for (int i = 0; i < tempNumber.size(); i++){
             digit = tempNumber[i] - '0';
             total += digit * digit;
         }
         tempNumber = conv(total, base);
        
         //myfile << count++ << ": "  << tempNumber << endl;   
         
     }
     if (tempNumber == "1"){
        return number;
     }
     else{
         return -1;
     }
}

int checkHappyLine(string line){
     // istringstream for iterating
     istringstream iss(line);
     int base;
     int * baseValues;
     int size = 0;
     bool allMatch = false;
     int smallest = -1;
     int tempSmallest = -1;
     int retVal;
     
     
     // count number of entries
     while (iss >> base) {
           size += 1;
           
     } 
     baseValues = new int [size];
     istringstream iss2(line);
     
     // get all base values
     for (int i = 0; iss2 >> base; i++) {
         baseValues[i] = base;
     }
     
     // run from 2 - inf
     for (retVal = 2; !allMatch; retVal= retVal++){
         
         smallest = checkHappyNum(retVal, baseValues[0]);
         if (smallest != -1){
            for (int j = 1; j < size; j++){
                cout << "retVal = " << retVal << " and baseVal = " << baseValues[j] << endl;
                tempSmallest = checkHappyNum(retVal, baseValues[j]);
                
                if (tempSmallest != -1){
                   allMatch = true;
                }
                else{
                    allMatch = false;
                    break;
                }
            }             
         }
     }
     
     return retVal;
     
}
*/

string conv(string original) {
       string newString = "";
       // go through the list of characters
       for (int i = 0; i < original.size(); i++){
           
           if (original[i] == 'a') {
              newString += 'y';
           }
           else if (original[i] == 'b') {
                newString += 'h';
           }
           else if (original[i] == 'c') {
                newString += 'e';
           }
           else if (original[i] == 'd') {
                newString += 's';
           }
           else if (original[i] == 'e') {
                newString += 'o';
           }
           else if (original[i] == 'f') {
                newString += 'c';
           }
           else if (original[i] == 'g') {
                newString += 'v';
           }
           else if (original[i] == 'h') {
                newString += 'x';
           }
           else if (original[i] == 'i') {
                newString += 'd';
           }
           else if (original[i] == 'j') {
                newString += 'u';
           }
           else if (original[i] == 'k') {
                newString += 'i';
           }
           else if (original[i] == 'l') {
                newString += 'g';
           }
           else if (original[i] == 'm') {
                newString += 'l';
           }
           else if (original[i] == 'n') {
                newString += 'b';
           }
           else if (original[i] == 'o') {
                newString += 'k';
           }
           else if (original[i] == 'p') {
                newString += 'r';
           }
           else if (original[i] == 'q') {
                newString += 'z';
           }
           else if (original[i] == 'r') {
                newString += 't';
           }
           else if (original[i] == 's') {
                newString += 'n';
           }
           else if (original[i] == 't') {
                newString += 'w';
           }
           else if (original[i] == 'u') {
                newString += 'j';
           }
           else if (original[i] == 'v') {
                newString += 'p';
           }
           else if (original[i] == 'w') {
                newString += 'f';
           }
           else if (original[i] == 'x') {
                newString += 'm';
           }
           else if (original[i] == 'y') {
                newString += 'a';
           }
           else if (original[i] == 'z') {
                newString += 'q';
           }
           else if (original[i] == ' ') {
                newString += ' ';
           }
           
           
       }
       return newString;
}


int main() {
    ifstream myReadFile;
    ofstream myWriteFile;
    string output, exitVal, newVal;
    myReadFile.open("test.in"); // change it to the name of file *****
    myWriteFile.open("output.txt");
    // read in T
    int T;
    myReadFile >> T; // the number of times to loop
    
    // for buffer to read by line
    getline(myReadFile, output); // remove additional portion 

    //myReadFile >> output;
    
    for (int i = 0; i< T; i++){
        // get the next line of input
        getline(myReadFile, output);    
        newVal = conv(output);
        myWriteFile << "Case #" << i+1 << ": " << newVal << endl;
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
