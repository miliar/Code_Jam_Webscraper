// Code jam 2012
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

const int maxNumber = 1000;
int array[maxNumber];
int index = 0;

int numOfDigits (int num)
{
    int numDigits = 0;
    while (num!=0) {
        num/=10;
        numDigits++;      
    }
    return numDigits;
}


int countRecycle(int n, int num, int m)
{
    int numDigits = numOfDigits(num); 
    if (numDigits==0 || numDigits==1)
       return 0;
    
    int count = 0, sum = 0, temp =num;
    int multiplier = 1;
    for (int i=0; i<numDigits-1; i++)
        multiplier *= 10;
    int x, i = index;
    
    while (count!=numDigits)
    {
       i++;
       if (find(array, array+i, temp)==array+i && numOfDigits(temp)==numDigits && temp<=m && temp>=n)
          array[i] = temp;
       else
           i--;
                
       x = temp%multiplier;
       temp = temp/multiplier;
       temp += (x*10);
       count++;
            
    }
    int temp2 = i-index;
    index = i;
    
    for (int j=1; j<temp2; j++)
        sum += j;
        
    return sum;                         
}


int main()
{
    string fname1 = "C-small-attempt1.in";
    string fname2 = "recycledNumbOutput.txt";
    string str;
    
    ifstream inFile(fname1.c_str());
    ofstream outFile(fname2.c_str());
    
    int count;
    inFile >> count;
    // getline (inFile, str);
    
    int n, m;
    int avg;
    int num1, num2;
    int total =0;
    for (int x=1; x<=count; x++)
    {
        total = 0;
        index = 0;
        inFile >> n;
        inFile >> m;
        // getline (inFile, str);
        
        for (int i=n; i<=m; i++)
        {
            total+=countRecycle(n, i, m);
        }
        outFile << "Case #" << x <<": " <<total << endl;
   
    }
    
    inFile.close();
    outFile.close();
    
    system("pause");
    return 0;
}
