#include <iostream>
#include <vector>;
#include <fstream>;
#include <string>;
#include <sstream>;
using namespace std;

struct Pair
{
	int n;
	int m;
};

vector<int> stringToVector(string a)
{
	vector<int> number;
	for(int i=0; i<a.size(); i++)
	{
		if(a[i]=='0')
		{
			number.push_back(0);
			continue;
		}
		if(a[i]=='1')
		{
			number.push_back(1);
			continue;
		}
		if(a[i]=='2')
		{
			number.push_back(2);
			continue;
		}
		if(a[i]=='3')
		{
			number.push_back(3);
			continue;
		}
		if(a[i]=='4')
		{
			number.push_back(4);
			continue;
		}
		if(a[i]=='5')
		{
			number.push_back(5);
			continue;
		}
		if(a[i]=='6')
		{
			number.push_back(6);
			continue;
		}
		if(a[i]=='7')
		{
			number.push_back(7);
			continue;
		}
		if(a[i]=='8')
		{
			number.push_back(8);
			continue;
		}
		if(a[i]=='9')
		{
			number.push_back(9);
			continue;
		}
	}
	return number;
}

vector<int> intToVector(int n)
{
	vector<int> N;
	stringstream s;
	s << n;
	string text = s.str();

	return stringToVector(text);
}

int vectorToInt(vector<int> N)
{
	ostringstream oss;
	for(int i=0; i<N.size(); i++)
		oss << N[i];

	 int final = 0;
	 std::istringstream iss(oss.str());
	 iss >> final;

	 return final;
}

bool isExist(Pair p, vector<Pair> pairs)
{
	for(int i=0; i<pairs.size(); i++)
		if(pairs[i].n == p.n && pairs[i].m == p.m)
			return true;
	return false;
}

void main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("C-small-attempt0.in");
	//inFile.open("test.in");
	//inFile.open("A-large-practice.in");
	outFile.open("output.txt");


	int totalNumber = 0;
	inFile >> totalNumber;
	int counter = 0;
	while(counter < totalNumber)
	{
		int number = 0;
		string a;
		inFile >> a;
		string b;
		inFile >> b;
		vector<int> A = stringToVector(a);
		vector<int> B = stringToVector(b);

		if(A.size() > 1)
		{
			vector<int> N = A;
			vector<int> M;
			vector<Pair> pairs;
			int n = vectorToInt(N);
			int m = vectorToInt(M);
			int a = vectorToInt(A);
			int b = vectorToInt(B);

			while (n < b)
			{
				for(int i=1; i<N.size(); i++)
				{
					M.clear();
					if(N[i] >= N[0])
					{
						for(int j=i; j<N.size(); j++)
						{
							M.push_back(N[j]);
						}
						for(int j=0; j<i; j++)
						{
							M.push_back(N[j]);
						}
						m = vectorToInt(M);
						if (m > n && m <= b)
						{
							Pair p;
							p.n = n;
							p.m = m;
							if(!isExist(p,pairs))
							{
								pairs.push_back(p);
								number ++;
							}
						}
					}
				}
				n ++;
				N = intToVector(n);
			}
		}
		outFile << "Case #";
		outFile << counter + 1;
		outFile << ": ";
		outFile << number;
		outFile << "\n";

		counter ++;
	}
}
