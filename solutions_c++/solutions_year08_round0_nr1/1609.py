#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

static const string inFileName("A-large.in");
static const string outFileName("A-large.out");

int main()
{
	fstream inFileStream(inFileName.c_str(),ios_base::in);
	string strline;

	getline(inFileStream, strline);
	int caseNum = atoi(strline.c_str());
	strline.clear();

	vector<int> switchNum(caseNum);

	for ( int caseCount=0; caseCount < caseNum; caseCount++)
	{
		switchNum[caseCount] = 0;
		//��������engineName ���������search engines��name

		getline(inFileStream,strline);
		int searchEngineNum = atoi(strline.c_str());
		strline.clear();
		
		//������ֵ�����
		vector<string> engineName(searchEngineNum);
		//��ű�־λ������
		//bitset< searchEngineNum> flag(0);
		vector<bool> flag( searchEngineNum);
		
		//��ʼ���������ͱ�־λ
		for (int i=0; i< searchEngineNum; i++ )
		{
			getline(inFileStream, strline);
			engineName[i] = strline;
			flag[i] = 0;
			strline.clear();
		}
		//��ʣ�µļ���query����ɨ��
		//���query������
		getline(inFileStream, strline);
		int queryNum = atoi(strline.c_str());
		strline.clear();

		int matchCount = 0;
		//��ÿһ��
		for (int i=0; i<queryNum; i++)
		{
			getline(inFileStream, strline);
			//��query������engineName��ÿ��Աȣ�ֱ���ҵ�����ͬ��
			for (int j=0; j<searchEngineNum; j++)
			{
				//���ҵ���ͬ��engineʱ
				if (engineName[j] == strline)
				{
					//���ȼ�����match��֮ǰ�Ƿ��⵽�����û�м�⵽��˵������match
					if ( flag[j] == 0)
					{
						//�����ҵ���engine��С���ܵ�engine��ʱ������Ҫswitch������־λ�Ķ�
						if ( matchCount < searchEngineNum-1)
						{
							flag[j] = 1;
							matchCount++;
						//	break;
						}
						else //ƥ���engine���Ѿ������ܵ�engine����Ҫswitch��
							//swith֮ǰ���õ������һ��ƥ���engine�������һ��ƥ���query����ʱswith
						{
							switchNum[caseCount]++;
							for (int k=0;k<searchEngineNum;k++)
								flag[k] = 0;
							//��һ�ֵ��ҵ������һ��match����switch֮��ĵ�һ��match
							flag[j] = 1;
							matchCount = 1;
						//	break;
						}
					} 
				//  else ���match�Ѿ���ǰ���ҵ�����������
				//  ��һ����query match��engine���ҵ��󣬾Ͳ���Ҫ����ѭ������match��
					break;
				}// else û�ҵ�match��������ѭ�����ҡ�
			}
		}
	}
	inFileStream.close();
	fstream outFileStream(outFileName.c_str(), ios_base::out);
	for (int i=0;i< caseNum;i++)
		outFileStream << "Case #" << i+1 <<": " << switchNum[i] << endl;
	outFileStream.close();
}