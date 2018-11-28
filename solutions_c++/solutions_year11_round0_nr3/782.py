#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

int main()
{
	int T;
    freopen("C.in" , "r" , stdin);
    freopen("C.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		unsigned int iN = 0;
		unsigned int iSmall = 0xffffffff;
		unsigned int iAddAll = 0;
		unsigned int iExorAll = 0;
		unsigned int iY;
		cin>>iN;
		for(int i=0;i<iN;i++)
		{
			int iC;
			cin>>iC;
			iExorAll ^= iC;
			iAddAll += iC;
			if(iC < iSmall)
			{
				iSmall = iC;
			}
		}
		iY = iAddAll - iSmall;
        cout<<"Case #"<<caseID<<": ";
		if(0 == iExorAll)
		{
			cout<<iY<<endl;
		}
		else
		{
			cout << "NO"<<endl;
		}
    }
    return 0;
}
