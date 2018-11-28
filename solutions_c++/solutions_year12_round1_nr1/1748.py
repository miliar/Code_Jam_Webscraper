#include<iostream>
#include<fstream>
#include<vector>
#include<iomanip>

using namespace std;
using std::showpoint;
int main(int argc, char** argv)
{
    ifstream input;
    ofstream output;
    int cases, i, j, size, res, A, B;
    int *arr1, *arr2;
    FILE* fp;    
    input.open("C:\\Users\\aditya\\workspace\\Cpp\\codejam\\round1\\A-small-attempt1.in");
    output.open("C:\\Users\\aditya\\workspace\\Cpp\\codejam\\round1\\output");
    output.close();
    fp = fopen("C:\\Users\\aditya\\workspace\\Cpp\\codejam\\round1\\output","w");
    if (input.is_open() )
    {
        input >> cases;
        // more output here
        
        for(i=1;i<=cases;i++)        
        {
            float p;
            int strokes=0;
            input >> A >> B;
            vector<float> probabilities;
            float min= 2 * B, product = 1.0, 
            expectedKeyStrokes, penaltyStrokes, probabilityOfSuccess;
            for (j=0;j<A;j++)
            {
                input >> p;
                product = product * p;
                probabilities.push_back(product);
                cout << product  << " " << probabilities[j] << " ";
            }     
            
            cout << endl;
            for (j=0;j<A;j++)
            {
                strokes = B-A+1 + 2*j;
                penaltyStrokes = 2*B-(A-j) + 2;
                probabilityOfSuccess = probabilities[A-j-1];
                expectedKeyStrokes =  strokes+ (B+1)* (1-probabilityOfSuccess) ;
                if (min > expectedKeyStrokes)
                    min = expectedKeyStrokes;
            }
            if ((B+2) < min )
                min = B+2;
            cout <<endl;
            fprintf(fp, "Case #%d: %6f\n", i, min);
  //          output << showpoint;
   //         output << "Case #" << i << ": " << setprecision (5)<< min <<endl;
        }
    
        input.close();
//        output.close();
    }
    else cout << "Unable to open file";
    fclose(fp);
    return 0;
}


