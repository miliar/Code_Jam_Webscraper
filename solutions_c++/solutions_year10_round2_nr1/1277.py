//============================================================================


//============================================================================

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


const int Max = 100;



void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = "//")
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
};



int main() {

	ifstream inData;
	ofstream outData;

	outData.open("outputFile");
	inData.open("A-large.in");
//	inData.open(fileName);
	if(!inData){
		cerr << "error input file error"<<endl;
		exit(1);
	}
	int nTestCases;

	inData >> nTestCases;

	int caseNum =1;

	while(!inData.eof() && nTestCases !=0 ){

		int n, m;


		int totalNum = 0;
		inData >> n;
		inData >> m;
		string empty;
		getline(inData, empty);
		set <string> pathSet;

		while(n >0){
			n--;

			string tempStr;
			getline(inData,tempStr);
			pathSet.insert(tempStr);

		}
		while(m >0){

			m--;
			int count = 0;
			string tempStr;
			getline(inData,tempStr);
//			cout << tempStr <<endl;
			if(pathSet.find(tempStr) != pathSet.end()){
				continue;
			}else{

				  vector <string> tempSet;
				  Tokenize(tempStr,tempSet,"//");
				  vector<string>::iterator it = tempSet.begin();
				  string item;

//				  it--;
				  while ( it != tempSet.end()){
//					  cout << *it<<endl;
					  item += "/"+*it;
					  it++;
					  if(pathSet.find(item)!= pathSet.end()){
						 continue;
					  }else{
						  count++;
						  cout << item<<endl;
						  cout << count <<endl;
						  pathSet.insert(item);
					  }

				  }



			}

			  totalNum += count;
			  cout << totalNum <<endl;

		}



		outData << "Case #"<< caseNum<<": " << totalNum<<endl;
		caseNum++;

		nTestCases--;


	}

	inData.close();
	outData.close();

//	system("PAUSE");
	return 0;
}

