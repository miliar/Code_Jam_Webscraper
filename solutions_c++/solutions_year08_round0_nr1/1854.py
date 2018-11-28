#include <stdio.h>
#include <string.h>

#include <iostream>
#include <vector>
using namespace std;

const int MAX = 1000;
// matrixǰ���������±꣬ �����ǲ�ѯ����
int out(vector<char *> se, vector<char *> query, int nos, int noq)
{
	int minTime = MAX;
	int SE[12][102];
	int time[12][102];
	int i, j, seIdx, line, col, currentTime, currentSEIndex, tmpTime;;
	char * currentQuery, * currentSE;
	for(seIdx = 0; seIdx < nos; seIdx++)
	{
		// ��ʼ��
		for(i = 0; i < nos; i++)
		{
			SE[i][0] = seIdx;
			time[i][0] = 0;
		}
		for(col = 1; col < noq + 1; col++)
		{
			currentQuery = query[col - 1];
			for(line = 0; line < nos; line++)
				time[line][col] = MAX;
			for(line = 0; line < nos; line++)
			{
				currentSEIndex = SE[line][col-1]; // ��ǰ�����±�
				currentSE = se[currentSEIndex]; // ��ǰ�����ַ���
				currentTime = time[line][col-1]; 
				if(!strcmp(currentQuery, currentSE)) // ����������ͬ
				{
					// �ı����洮,��������Ӧ��time����������㣬����
					for(j = 0; j < nos; j++)
					{
						if( j == currentSEIndex )
						{
							tmpTime = MAX;
						}
						else
						{
							tmpTime = currentTime + 1;
						}
						if(tmpTime < time[j][col])
							time[j][col] = tmpTime;
						SE[j][col] = j;
					}
				}
				else
				{
					for(j = 0; j < nos; j++)
					{
						if(j == currentSEIndex )
							tmpTime = currentTime;
						else
							tmpTime = MAX;
						if(tmpTime < time[j][col])
							time[j][col] = tmpTime;
						SE[j][col] = j;
					}
				}

			}
		}
		for(i = 0; i < nos; i++)
		{
			if(minTime > time[i][noq])
				minTime = time[i][noq];
		}
	}
	//for(i = 0; i < nos; i++)
	//{
	//	SE[i][0] = i;
	//	time[i][0] = 0;
	//}
	//for(col = 1; col < noq+1; col++) // ��ѯ���ַ����±�
	//{
	//	currentQuery = query[col-1]; // ��ǰ��ѯ�ַ���
	//	for(line = 0; line < nos; line++) // �������±�
	//	{
	//		currentSE = se[line]; // ��ǰ����������
	//		if(!strcmp(currentQuery, currentSE)) // ����������ͬ
	//		{
	//		}
	//		else
	//		{
	//			for(i = 0; i < nos; i++)
	//			{
	//				SE[line][col][i] = line; // ���䣬��һ�����������뵱ǰ����ͬ
	//				time[line][col][i] = 				
	//		}

	//	}

	//}
	//for(col = 1; col < noq + 1; col++)
	//{
	//	for(line = 0; line < nos; line++)
	//	{
	//		prevSE = se[matrix[line][col-1].first]; // ǰһ������

	//		currentQuery = query[i];


	//}
	return minTime;
}

int main()
{
	int len = 0;
	FILE * fin, * fout;
	fin = fopen("C:\\A-small.in", "r");
	fout = fopen("C:\\A-small.out", "w");
	int caseNum;
	fscanf(fin, "%d\n", &caseNum);
	int num = 0;
	for(; num < caseNum; num++)
	{
		int numOfSE, numOfQuery;
		fscanf(fin, "%d\n", &numOfSE);
		vector<char *> v_SE = vector<char *>(numOfSE);
		for(int i = 0; i < numOfSE; i++)
		{
			v_SE[i] = (char *)malloc(sizeof(char) * 256);
			fgets(v_SE[i], 256, fin);
			len = strlen(v_SE[i]);
			v_SE[i][len-1] = '\0';
		}
		//for(int i = 0; i < numOfSE; i++)
		//{
		//	printf("%d, %s\n", strlen(v_SE[i]), v_SE[i]);
		//}
		fscanf(fin, "%d\n", &numOfQuery);
		vector<char *> v_Query = vector<char *>(numOfQuery);
		for(int i = 0; i < numOfQuery; i++)
		{
			v_Query[i] = (char *)malloc(sizeof(char) * 256);
			fgets(v_Query[i], 256, fin);
			len = strlen(v_Query[i]);
			v_Query[i][len-1] = '\0';
		}
		int result = out(v_SE, v_Query, numOfSE, numOfQuery);
		fprintf(fout, "Case #%d: %d\n", num+1, result);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}