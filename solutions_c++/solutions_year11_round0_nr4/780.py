#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<cmath>
using namespace std;

int main()
{
	int T;
    freopen("D.in" , "r" , stdin);
    freopen("D.out" , "w" , stdout);
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
		unsigned int iN;
		unsigned int iHits;
		double f;
		cin>>iN;
		iHits = iN;
		for(int i=1;i<=iN;i++)
		{
			int iC;
			cin>>iC;
			if(iC == i)
			{
				iHits--;
			}
		}
		f = iHits;
        cout<<"Case #"<<caseID<<": "<<setiosflags(ios::fixed)<<setprecision(6)<<f<<endl;
    }
    return 0;
}
