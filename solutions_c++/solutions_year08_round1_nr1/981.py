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
	middle = pData[(left+right)/2];  //求中间值
	do{
		while((pData[i]<middle) && (i<right))//从左扫描大于中值的数
			i++;           
		while((pData[j]>middle) && (j>left))//从右扫描大于中值的数
			j--;
		if(i<=j)//找到了一对值
		{
			//交换
			iTemp = pData[i];
			pData[i] = pData[j];
			pData[j] = iTemp;
			i++;
			j--;
		}
	}while(i<=j);//如果两边扫描的下标交错，就停止（完成一次）

	//当左边部分有值(left<j)，递归左半边
	if(left<j)
		run(pData,left,j);
	//当右边部分有值(right>i)，递归右半边
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
