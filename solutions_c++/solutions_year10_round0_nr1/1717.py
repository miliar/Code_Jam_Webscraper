// test2.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <iostream>
#include <math.h>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
    int n;
    cin >> n;
    __int64 t;
    double a,b;
    for(int i=0;i<n;i++){
        cin>>a>>b;
        t = pow(2,a);
        if(fmod((b+1),t)==0)
            cout<<"Case #"<<i+1<<": ON\n";
        else
            cout<<"Case #"<<i+1<<": OFF\n";
    }
   
   // system("PAUSE");
	return 0;
}

