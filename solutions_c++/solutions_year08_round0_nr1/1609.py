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
		//建立向量engineName 来存放所有search engines的name

		getline(inFileStream,strline);
		int searchEngineNum = atoi(strline.c_str());
		strline.clear();
		
		//存放名字的向量
		vector<string> engineName(searchEngineNum);
		//存放标志位的容器
		//bitset< searchEngineNum> flag(0);
		vector<bool> flag( searchEngineNum);
		
		//初始化引擎名和标志位
		for (int i=0; i< searchEngineNum; i++ )
		{
			getline(inFileStream, strline);
			engineName[i] = strline;
			flag[i] = 0;
			strline.clear();
		}
		//对剩下的几行query逐行扫描
		//获得query的行数
		getline(inFileStream, strline);
		int queryNum = atoi(strline.c_str());
		strline.clear();

		int matchCount = 0;
		//对每一行
		for (int i=0; i<queryNum; i++)
		{
			getline(inFileStream, strline);
			//将query内容与engineName中每项对比，直到找到有相同的
			for (int j=0; j<searchEngineNum; j++)
			{
				//当找到相同的engine时
				if (engineName[j] == strline)
				{
					//首先检测这个match在之前是否检测到。如果没有检测到，说明是新match
					if ( flag[j] == 0)
					{
						//当已找到的engine数小于总的engine数时，不需要switch，将标志位改动
						if ( matchCount < searchEngineNum-1)
						{
							flag[j] = 1;
							matchCount++;
						//	break;
						}
						else //匹配的engine数已经等于总的engine，需要switch。
							//swith之前所用的是最后一个匹配的engine，当最后一个匹配的query到达时swith
						{
							switchNum[caseCount]++;
							for (int k=0;k<searchEngineNum;k++)
								flag[k] = 0;
							//上一轮的找到的最后一个match，是switch之后的第一个match
							flag[j] = 1;
							matchCount = 1;
						//	break;
						}
					} 
				//  else 这个match已经在前面找到过，跳过。
				//  当一个与query match的engine被找到后，就不需要再在循环中找match。
					break;
				}// else 没找到match，继续在循环中找。
			}
		}
	}
	inFileStream.close();
	fstream outFileStream(outFileName.c_str(), ios_base::out);
	for (int i=0;i< caseNum;i++)
		outFileStream << "Case #" << i+1 <<": " << switchNum[i] << endl;
	outFileStream.close();
}