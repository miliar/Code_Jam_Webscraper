#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

const string inputFile = "B-large.in";
const int numOfLetters = 26; 


// Possible optimizations:
// no need for 26x26

int get_coor(char c)
{
	return int(c-'A'+1);
}

string get_char(int i)
{
	string s = "x";
	s[0] = (char(i-1+'A'));
	return s;
}

string process(int** mat, int * arr, int currentC, int totalNum)
{
/*if(currentC>totalNum)
	{
		return "[]";
	}*/
	
	string result ;
	result.reserve(totalNum*8);
	result = "[";
	int startSearching =1;
	

	for(int n= currentC; n<=totalNum; n++)
	{
	//	cout<<n<<" "<<arr[n]<<" "<<startSearching<<endl;
			bool isBroken= false;
		for(int i = startSearching; i<n-1; i++)
		{
			if(mat[arr[i]][arr[n]] < 0) // -1 or -2*
 			{
				result = "[";	
				startSearching = n+1;
				isBroken = true;
			//	cou<<result<<endl;
				break;
			}
		}

			// FIX 2
			if(n!=1 && n>startSearching && mat[arr[n-1]][arr[n]]  == -1) // -1 or -2*
 			{
				result = "[";	
				startSearching = n+1;
				isBroken = true;
			}
//		cout<<result<<endl;
	
	
	if(!isBroken)
	{
		if(n!= totalNum )
		{
			if(mat[arr[n]][arr[n+1]]  == -1) // -1 or -2
			{
				result = "[";	
				startSearching = n+2;
				n++; // UPDATE count - ignore next character
			}
			else if(mat[arr[n]][arr[n+1]] == 0) // will be true if any of them is non-base 
			{
				result.append(get_char(arr[n]));
				result.append(", ");
			}
			else if(mat[arr[n]][arr[n+1]] > 0)
			{
			//	result.append(get_char(mat[arr[n]][arr[n+1]]));
			//	result.append(", ");
		// FIX 1
				arr[n]=arr[n+1] = mat[arr[n]][arr[n+1]];  /// to prevent cases such as  1 ABC 1 AB 5 ABABB
			}
			else
			{
				// FIX 1
								arr[n]=arr[n+1] = mat[arr[n]][arr[n+1]]/-2; // specail case- opposite and combinable
			}
		}
		else if(startSearching!= totalNum+1)
		{
				result.append(get_char(arr[totalNum]));

		}
		
	}


 // cout<<result<<endl;
	}
	
	
		
		result.append("]");
		
		return result;
	
}


int main()
{
	
	ifstream input;
	input.open(inputFile.c_str());
	int T;
	input>>T;
	ofstream output;
	output.open((inputFile+".out").c_str());
	
	
	int** matOfElements = new int* [numOfLetters+1];
	for(int i=1; i<=numOfLetters; i++)
	{
		matOfElements[i] = new int[numOfLetters+1];

	}
	
	
	for(int t=1;t<=T; t++)	
	{
		int C,N,D;
		input>>C;
		
		for(int i=1; i<=numOfLetters; i++)
		{
			for(int j=1; j<=numOfLetters; j++)
			{
				matOfElements[i][j] = 0;
			}
		}
		
		string strTemp;
		for(int c=1; c<=C; c++)
		{
			input>>strTemp;
			int coor1 = get_coor(strTemp[1]);
			int coor0 = get_coor(strTemp[0]);
			matOfElements[coor0][coor1]  = matOfElements[coor1][coor0] = get_coor(strTemp[2]);
		}
		
		input>>D;
		for(int d=1; d<=D; d++)
		{
				input>>strTemp;
				int coor1 = get_coor(strTemp[1]);
				int coor0 = get_coor(strTemp[0]);
					if(matOfElements[coor0][coor1] == 0)  // if they combine -  mark them as special
					{
						matOfElements[coor0][coor1]  = matOfElements[coor1][coor0] = -1;  // -1 indicates opposite elements
					}
					else
					{
							matOfElements[coor0][coor1]  = matOfElements[coor1][coor0] = -2*matOfElements[coor0][coor1];  // -2 indicates opposite elements, 
										// but combinable if they are consecutive
						
					}
					
		}
		
		input>>N>>strTemp;
		int* arrOfElements =new int[N+1];
		for(int n=1; n<=N; n++)
		{
			
			arrOfElements[n] = get_coor(strTemp[n-1]);
		}
		
		string result =	process(matOfElements,arrOfElements,1,N);
			
			
				output<<"Case #"<<t<<": "<<result<<endl;
			
				
		
	}
	
	for(int i=1; i<=numOfLetters; i++)
	{
		delete [] matOfElements[i];
	}
	delete [] matOfElements;

	return 0;
}
