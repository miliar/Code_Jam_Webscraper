#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int NA, NB;

int time1(string in)
{
	stringstream sstream1;
	stringstream sstream2;
	
	int h, m;
	string temp = in.substr(0, 2);
	sstream1 << temp;
	sstream1 >> h;
	temp = in.substr(3,2);
	sstream2 << temp;
	sstream2 >> m;
	return h*60+m;
}

int time2(string in, int T)
{
	stringstream sstream1;
	stringstream sstream2;
	
	int h, m;
	string temp = in.substr(0, 2);
	sstream1 << temp;
	sstream1 >> h;
	temp = in.substr(3,2);
	sstream2 << temp;
	sstream2 >> m;
	return h*60+m+T;
}

int result(vector<int> D, vector<int> A)
{
	int value=0;
	int i=0;
	int j=0;
	
	while (j<A.size()&&i<D.size())
	{
		if (A[j] <= D[i])
		{
			value++;
			i++;
			j++;
		}
		else if (A[j]>D[i])
		{
			i++;
		}
	}
	return value;
}

int main (int argc, char * const argv[]) {
	int N, T;
	string A1, A2;
	string B1, B2;
	int a, b;

	

	ifstream fin ("/B-large.in");
	ofstream fout ("/B-output.txt");
	
	fin >> N;
	
	for (int i=0; i<N; i++)
	{
		fin >> T;
		fin >> NA >> NB;
	vector<int> AD(NA);
	vector<int> BA(NA);
	vector<int> AA(NB);
	vector<int> BD(NB);
		for (int j=0; j<NA; j++)
		{
			fin >> A1 >> A2;
			AD[j] = time1(A1);
			BA[j] = time2(A2, T);
		}
		for (int k=0; k < NB; k++)
		{
			fin >> B1 >> B2;
			BD[k] = time1(B1);
			AA[k] = time2(B2, T);
		}
		sort(AD.begin(), AD.end());
		sort(BD.begin(), BD.end());
		sort(AA.begin(), AA.end());
		sort(BA.begin(), BA.end());

		a=result(AD, AA);
		b=result(BD, BA);
		
		fout << "Case #" << (i+1) << ": " << (NA-a) << " " << (NB-b) << endl;

			
	}
	
    return 0;
}
