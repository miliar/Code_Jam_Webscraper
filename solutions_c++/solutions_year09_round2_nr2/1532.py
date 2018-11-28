// The Next Number.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "iostream"
#include "fstream"

using namespace std;
#define MaxInt 1000000
int A[7];
int _tmain(int argc, _TCHAR* argv[])
{
	int num,i,j,k,n,m,tmp;
	ifstream ifile=ifstream("B-small-attempt4.in");
	ofstream ofile=ofstream("bsmall.txt");
	cin.rdbuf(ifile.rdbuf());
	cout.rdbuf(ofile.rdbuf());
	cin>>num;
	for(i=0;i<num;i++)
	{
		cin>>n;
		m=0;
		for(j=0;n>9;j++)
		{
			A[j]=n%10;//个位数在前
			n/=10;
			m++;
		}
		A[m++]=n;
		for(j=1;j<m;j++)
		{
			for(k=0;k<j;k++)
				if(A[k]>A[j])
				{
					tmp=A[j];
					A[j]=A[k];
					A[k]=tmp;

					for(j=j-1;j>=0;j--)
						for(k=j-1;k>=0;k--)
							if(A[k]<A[j])
							{
								tmp=A[j];
								A[j]=A[k];
								A[k]=tmp;
							}
					goto lable;
				}
		}
		A[m++]=0;
		for(j=0;j<m;j++)
			for(k=j+1;k<m;k++)
				if(A[j]<A[k])
				{
					tmp=A[j];
					A[j]=A[k];
					A[k]=tmp;
				}
		for(j=m-2;j>=0;j--)
			if(A[j]!=0)
			{
				A[m-1]=A[j];
				A[j]=0;
				break;
			}
lable:
			cout<<"Case #"<<i+1<<": ";
			for(j=m-1;j>=0;j--)
			{
				cout<<A[j];
			}
			cout<<endl;
	}

	/*getchar();
	getchar();*/
	return 0;
}

//50
//316221
//250677
//951861
//1010
//4
//909652
//987791
//6233
//754063
//319643
//234044
//709
//4000
//644932
//828999
//210
//201527
//792491
//9009
//65
//591116
//857931
//900
//859816
//115
//613869
//149989
//522316
//705939
//596594
//701686
//359710
//146725
//954952
//1051
//34
//228102
//703
//996520
//40
//830084
//218765
//880
//805511
//480
//954011
//30000
//77
//1000000
//808

