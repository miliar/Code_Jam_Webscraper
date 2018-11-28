#include <iostream>
#include <fstream>
#include <vector>
#include<algorithm>
#include <functional>
#include <numeric>
using namespace std;

int main()
{
      int number_of_test = 0;  
      long c = 0;                      
      int N = 0;

      ifstream inputFile;
      inputFile.open("C-large.in");

      if (!inputFile)
      {
            cout << "input file error, check file name and path!" <<endl;
      }
      inputFile >> number_of_test;
      cout << "total number of test cases is:  " << number_of_test <<endl;
     // cin.get();

      ofstream outputFile;
      outputFile.open("SmallOutput.txt");

      for (int testID = 0; testID < number_of_test; testID ++)
      {
          //  cout << "current testID = " << testID <<endl;

            inputFile >>N;
          //  cout << "number of pieces = " << N <<endl;
           // cin.get();

            if (N ==0)
            {
                  cout << "There cannot be 0 candies in the bag" <<endl;
            }

            vector<int> candyVal;
            for (int i = 0; i < N; i++)
            {
                  inputFile >> c;
                  candyVal.push_back(c);
                //  cout << "read in candy value is:" << c <<endl;
            }

            //Now decide whether it is possible for Sean to keep Patrick from crying
            int bitAddSum = 0;

            //This test is not right~, should be some other op
            for (int j = 0; j < candyVal.size(); j++)
            {
                  bitAddSum = bitAddSum ^ candyVal.at(j);
            }

        //    cout << "bitAddSum = " << bitAddSum <<endl;

            if (bitAddSum != 0 )
            {
                  outputFile << "Case #"<< testID+1 <<":  NO" << endl;
            }
            else
            {
                  //find out the maximal sum for current test cases
                  //and output the maximal possible value
                  
                 int totalSum =  std::accumulate( candyVal.begin(), candyVal.end(), 0 );
                  int minVal= 1E7;
                  for (int j = 0; j < candyVal.size(); j++ )
                  {
                        if (candyVal.at(j) < minVal)
                        {
                              minVal = candyVal.at(j);
                        }
                  }

              //    cout << "current min value is:" << minVal <<endl;
                  int maxSum = totalSum - minVal;
                  outputFile << "Case #" <<testID+1 << ": " <<maxSum <<endl;
            }
      }

     // cin.get();
      return 0;
}