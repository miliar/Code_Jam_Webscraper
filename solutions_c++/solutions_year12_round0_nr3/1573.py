#include<fstream>
#include<cmath>
#include<vector>

using namespace std;

int wei(int x);//�ж�һ�����м�λ

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	//���ݶ�������
	int T;//��������
	int A;
	int B;
	int i,j;//����ʹ��
	int weishu = 0;//һ�����ж���λ
	int M = 0;//���ٴ�
	int count = 0;
	int k;//��ʱ����
	int x;
	vector<int> answer;
	bool tag = true;

	fin >> T;
	for(i = 0; i != T; ++i)
	{
		count = 0;
		fin >> A;
		fin >> B;

		for(j = A; j <= B; ++j)
		{
			k = j;
			weishu = wei(j);
			M = (int)pow((double)10,weishu) / 10;

			x = 1;
			for(int n = 0; n != weishu; n++)
			{
				tag = true;

				if(k / 10 + k % 10 * M <= B && 
						k / 10 + k % 10 * M > j)
				{
					for(unsigned m = 0; m != answer.size(); ++m)
					{
						if(k / 10 + k % 10 * M == answer[m])
						{
							tag = false;
							break;
						}
					}
					if(tag)
					{
						answer.push_back(k / 10 + k % 10 * M);
						count++;
					}
				}
				k = k / 10 + k % 10 * M;
			}
			answer.clear();

		}
		fout << "Case #" << i + 1 << ": " << count << endl;



	}

	return 0;
}

int wei(int x)//�ж�һ�����м�λ
{
	int count = 0;
	while(x)
	{
		count++;
		x = x / 10;
	}

	return count;
}


			

