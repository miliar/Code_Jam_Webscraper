#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

int main (int argc, char * const argv[]) {
	ifstream input("A-large.in");
	ofstream output("output1.txt");
	int T;
	int N;
	int M;
	input>>T;
	for(int i=0;i<T;i++)
	{
		input>>N;
		input>>M;
		string directories[10000];
		int num=0;
		int answer=0;
		for(int j=0;j<N;j++)
		{
			input>>directories[num];
			num++;
		}
		for(int j=0;j<M;j++)
		{
			string temp;
			input>>temp;
			for(int k=1;k<temp.length();k++)
			{
				if(temp[k]=='/')
				{
					int add=1;
					for(int count=0;count<num;count++)
					{
						if(temp.substr(0,k)==directories[count])
							add=0;
					}
					if(add==1)
					{
						directories[num]=temp.substr(0,k);
						num++;
						answer++;
					}
				}
			}
			int add=1;
			for(int count=0;count<num;count++)
			{
				if(temp==directories[count])
					add=0;
			}
			if(add==1)
			{
				directories[num]=temp;
				num++;
				answer++;
			}
		}
		output<<"Case #"<<i+1<<": "<<answer;
		if(i!=T-1)
			output<<endl;
	}
    return 0;
}
