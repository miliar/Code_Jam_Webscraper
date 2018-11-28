#include<iostream>
#include<fstream>
#include<vector>
#include<list>

using namespace std;

int pow10[10] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

//int matrix[10000][10000];

int shift(int num, int jaritsu)
{
	int temp = num % 10;
	num = num / 10;
	num = num + temp * pow10[jaritsu];

	return num;
}

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int n;

	fin>>n;

	for(int i=0; i<n; i++)
	{
		int result = 0;
		int a, b;
		int number;
		
		fin>>a>>b;

		number = (int)log10((double)a);
		
		for(int j=a; j<=b; j++)
		{
			int temp = j;
			int jungbok[10] = {0, };

			for(int k=0; k<number; k++)
			{
				temp = shift(temp, number);

				if( j<temp && a <= temp && temp <= b )
				{
					int l;
					for(l=0; l<k; l++)
					{
						if(temp == jungbok[l])
						{
							break;
						}
					}

					if(l != k)
						continue;

					jungbok[k] = temp;

//					fout<< j << " : " << temp << endl;
/*
					if(j<temp)
					{
						if(matrix[j][temp])
							fout<<"error here"<<endl;
						matrix[j][temp]++;
					}
					else if (temp < j)
					{
						if(matrix[temp][j])
							fout<<"error here"<<endl;
						matrix[temp][j]++;
					}
					else
					{
						fout<<"how to come here?"<<endl;
					}
*/
					result++;
				}
			}
		}

		fout<<"Case #"<<(i+1)<<": "<<result<<endl;
	}

	return 0;
}