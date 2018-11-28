#include <iostream>
#include < fstream >
using namespace std;
ifstream inFile;
ofstream outFile;

void run(int* pData,int left,int right)
{
	int i,j;
	int middle,iTemp;
	i = left;
	j = right;
	middle = pData[(left+right)/2];  //���м�ֵ
	do{
		while((pData[i]<middle) && (i<right))//����ɨ�������ֵ����
			i++;           
		while((pData[j]>middle) && (j>left))//����ɨ�������ֵ����
			j--;
		if(i<=j)//�ҵ���һ��ֵ
		{
			//����
			iTemp = pData[i];
			pData[i] = pData[j];
			pData[j] = iTemp;
			i++;
			j--;
		}
	}while(i<=j);//�������ɨ����±꽻����ֹͣ�����һ�Σ�

	//����߲�����ֵ(left<j)���ݹ�����
	if(left<j)
		run(pData,left,j);
	//���ұ߲�����ֵ(right>i)���ݹ��Ұ��
	if(right>i)
		run(pData,i,right);
}

void QuickSort(int* pData,int Count)
{
	run(pData,0,Count-1);
}

int main()
{
	inFile.open("input.dat",ios::in);
	outFile.open("output.dat",ios::out);
	int T,n,min,x[10],y[10];
	inFile >> T;
	for( int i = 1; i <= T; i++ ){
	    inFile >> n;
		for( int j = 0; j < n; j++ ) inFile >> x[j];
		for( int j = 0; j < n; j++ ) inFile >> y[j];
    	QuickSort(x,n);
		QuickSort(y,n);
		min = 0;
		for( int j = 0; j < n; j++) min = min + x[j] * y[n - j - 1];
		outFile << "Case #" << i << ": " << min << endl;
	}
	inFile.close();
	outFile.close();
	return 0;
}
