#include < iostream >
#include < fstream >
using namespace std;
ifstream inFile;
ofstream outFile;

void run(long* pData,long left,long right)
{
	long i,j;
	long middle,iTemp;
	i = left;
	j = right;
	middle = pData[(left+right)/2];  //求中间值
	do{
		while((pData[i]>middle) && (i<right))//从左扫描大于中值的数
			i++;           
		while((pData[j]<middle) && (j>left))//从右扫描大于中值的数
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

void QuickSort(long* pData,long Count)
{
	run(pData,0,Count-1);
}

int main(){
	inFile.open("input.dat",ios::in);
	outFile.open("output.dat",ios::out);
	int r,N,P,K,L;
	long t,d[101];
    inFile >> N;
	//outFile  << N;
	for( int i = 1; i <= N; i ++){
		inFile >> P >> K >> L;
		if( P*K < L ){ 
			outFile << "Case #" << i << ": Impossible" << endl; break; }
		for( int j = 0; j < L; j ++) inFile >> d[ j ];
		QuickSort( d, L );
		//for( int j = 0; j < L; j ++) outFile << d[ j ] << endl;
		t = 0; r = 1;
		for( int j = 0; j < L; j ++){
			t = t + d[ j ]*r;
			if( (j+1)%K == 0 ) r ++;
		}
		outFile << "Case #" << i << ": " << t << endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}