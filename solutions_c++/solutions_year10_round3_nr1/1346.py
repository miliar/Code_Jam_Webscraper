// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
using namespace std;
using std::endl;



int _tmain(int argc, _TCHAR* argv[])
{

	int N,T;
    ifstream input("A-large.in",ios::in);
	ofstream output("A-large.out",ios::out);

	//freopen("A.in" , "r" , stdin);
 //   freopen("A.out" , "w" , stdout);
    input>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		input>>N;
		int **a = new int*[N];
        for (int i = 0;  i < N;  i++)
        {
          a[i] = new int[2];
        }
		//int a[N][2];
		for(int k=0;k<N;k++)
		{
		   
           input>>a[k][0]>>a[k][1];
		}
		long int count=0;
		for(int i=0;i<N;i++)
		{
			for(int j=i+1;j<N;j++)
			{
				if(a[i][0]>a[j][0]&&a[i][1]<a[j][1])
					count++;
				else if(a[i][0]<a[j][0]&&a[i][1]>a[j][1])
					count++;
			}
		}
        output<<"Case #"<<caseID<<": "<<count<<endl;
        for (int m = 0; m < N; m++)
        {
          delete[] a[m];
        }
         delete[] a;
         a = NULL;

	 }
	return 0;
}

