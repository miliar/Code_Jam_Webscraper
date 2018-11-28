#include <cstdio>
#include <iostream>
#include <fstream>
//#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	//ifstream fin ("A-small-attempt0.in");
	ifstream fin ("A-large.in");
    //ofstream fout ("A-output-small.txt");
	ofstream fout ("A-output-large.txt");

	int cases = 0;
	fin >> cases;
	/*{string buffer;
	getline(fin,buffer);} //if needed to read the next lines as lines*/

	for(int i=0; i<cases; i++)
	{
		cout << "Case #"<<(i+1) <<": "<<endl;
		fout << "Case #"<<(i+1) <<": "<<endl;

		int teams;
		fin >> teams;

		int **results = new int*[teams];
		float *wp = new float[teams];
		int *counter = new int[teams];

		for(int j=0; j<teams; j++)
		{
			results[j] = new int[teams];
			wp[j] = 0;
			counter[j] = 0;
			for(int k=0; k<teams; k++)
			{
				char temp;
				fin >> temp;
				results[j][k] = -1;
				if(temp != '.')
				{
					wp[j] += (temp-48);
					results[j][k] = temp - 48;
					counter[j]++;
				}
			}
			if(counter[j] > 0)
				wp[j] /= counter[j];
		}

		float *owp = new float[teams];

		for(int j=0; j<teams; j++)
		{
			owp[j] = 0;
			int count = 0;
			for(int k=0; k<teams; k++)
			{
				if(results[j][k] != -1)
				{
					owp[j] += (wp[k] * counter[k] - results[k][j])/(counter[k] - 1);
					count++;
				}
			}
			if(count > 0)
			{
				owp[j] /= count;
			}
		}
		
		//float *oowp = new float[teams];
		//float *result = new float[teams];

		for(int j=0; j<teams; j++)
		{
			float result = 0;
			int count = 0;
			for(int k=0; k<teams; k++)
			{
				if(results[j][k] != -1)
				{
					result += owp[k];
					count ++;
				}
			}

			if(count > 0)
				result /= count;

			result = 0.25*wp[j] + 0.5*owp[j] + 0.25*result;

			cout<<result<<endl;
			fout<<result<<endl;
		}

		//delete[] oowp;
		//delete[] result;
		delete[] owp;
		delete[] wp;
	}
	system("pause");
	return 0;
}