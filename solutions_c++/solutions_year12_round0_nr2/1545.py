#include<fstream>

using namespace std;

int data[100];
	int T;// �������ݵ�����
	int N;//googleer��������
	int S;//surpring������
	int P;//��͵���߷���
	int t;//ÿһ��googler

int main()
{
	int i,j;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int num = 0;
	int numA = 0;
	int numB = 0;
	int numC = 0;
	int numD = 0;
	int numE = 0;

	fin >> T;//�����ܵĲ�����������

	for(i = 0; i != T; ++i)
	{
		num = 0;
		numA = 0;
		numB = 0;
		numC = 0;
		numD = 0;
		numE = 0;
		fin >> N;//����
		fin >> S;
		fin >> P;

		for(j = 0; j != N; ++j)
		{
			fin >> t;
			if(t / 3 >= P ||
				(t / 3 == P - 1 && t % 3 == 1))
				numA++;
			else
			{
				if(t / 3 == P - 1 && t % 3 == 0 && t > 0)
					numB++;
				else
				{
					if(t / 3 == P - 1 && t % 3 == 2)
						numC++;
					else
					{
							if(t / 3 == P - 2 && t % 3 == 2)
								numD++;
							else
								numE++;
					}
				}
			}
				if(numB + numD >= S)
					num = numA + numC + S;
				else
					num = numA + numC + numB + numD;
		
		}
			fout << "Case #" << i + 1 << ": " << num << endl;
	}

	return 0;
}

