#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <string>
using namespace std;

typedef vector<int> attempt;

bool cgb(int score, int b)
	{int avg=b*3;
	if (score>=avg-2) return true;
	return false;
	}
bool cgbs(int score, int b)
	{int avg=b*3;
	if (score>=avg-4) return true;
	return false;
	}
int findMaxBest(int p, int S, vector<int> scores)
	{int result = 0 ;
	 for (int i = 0; i < scores.size(); i++)
		{if (scores[i] < p) continue; 
		if (cgb(scores[i], p))
			{result ++;  
			continue;
			}
			if (cgbs(scores[i], p))
			{if (S != 0)
				{S--;
				result++;
				continue;
				}
			}
		}
		return result;
	}




int main(int argc, char* argv[])
{	char *input="B-large.IN";
	char *output="Output.txt";
	int temp_int, temp_N;
	int N,S,p;
	ifstream fin; 
    ofstream fout;
	attempt temp_at;
	vector<int> temp;
	vector<int>scores;
	vector<attempt> data;
	
	int T,i,j;
	fin.open(input);
	fout.open(output);

	while(!fin.eof()){
	fin>>T;
	for(i=0; i<T; i++)
		{temp.clear();
		 fin>>temp_N;
		 temp.push_back(temp_N);
		 for (j=0; j<temp_N+2; j++)
			{fin>>temp_int; 
			 temp.push_back(temp_int);
			}
		 data.push_back(temp); 
		}
	
	}

for (i=0; i<data.size()/2; i++)
{N=data[i][0];
 S=data[i][1];
 p=data[i][2];
 scores.clear();
 for (j=3; j<data[i].size(); j++)
	 scores.push_back(data[i][j]);
 fout<<"Case #"<<i+1<<": "<<findMaxBest(p,S,scores)<<"\n";
}

	 fin.close();
	fout.close();
	data.clear();
	return 0;

}
