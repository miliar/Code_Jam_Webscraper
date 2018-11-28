#include <iostream>
#include <fstream>
#include <string>
#include <deque>
#include <map>
#include <list>
#include <vector>
#include <iterator>
#include <set>
#include <algorithm>
#include<cmath>

using namespace std;
typedef unsigned long long uint_64 ;
typedef long long int_64 ;
#define all(c) c.begin(), c.end()
#define TRACE(X) std::cerr<<X<<std::endl;

int main()
{
	uint_64 numCase;
	cin >> numCase;
	//TRACE("number of cases"<<numCase)
	uint_64 numCaseCounter;
    uint_64 i,k,j,n,c;
	//long long c;
	for (numCaseCounter = 0; numCaseCounter < numCase; numCaseCounter++)
	{
		
//TRACE("Inputcase "<<numCaseCounter+1)

		uint_64 numOftrees,A,B,C,D,X0,Y0,M;
		cin>>numOftrees;
        std::vector <std::pair<uint_64,uint_64> > treecoor;	

		cin>>A;
				cin>>B;		cin>>C;		cin>>D;		cin>>X0; cin>>Y0;		cin>>M;
				//TRACE("values"<<A<<B<<C<<D<<X0<<Y0<<M)
		treecoor.push_back(pair<uint_64,uint_64>(X0,Y0));
				         uint_64 X=X0,Y=Y0;
		for (j=1;j<numOftrees;j++  )
		{

		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
		treecoor.push_back(pair<uint_64,uint_64>(X,Y));
		}

		//TRACE("process Case "<<numCaseCounter+1)
//process

        uint_64 number_oftrees=0;
		for (i=0;i<numOftrees-2 ; i++)
		{
			//TRACE("i")
			for (k=i+1;k<numOftrees-1 ;k++ )
			{			//TRACE("j")
				for (j=k+1;j<numOftrees ;j++ )
				{			//TRACE("k")
					if (0==(treecoor[i].first +treecoor[j].first +treecoor[k].first)%3 
						&& 0==(treecoor[i].second +treecoor[j].second +treecoor[k].second)%3)
					{
				//TRACE("INSIDE")
						number_oftrees++;
					}
				}
			}
		}

//TRACE("Inputcase "<<numCaseCounter+1)



//TRACE("write Case "<<numCaseCounter+1)
//output replace ans
		cout << "Case #" << (numCaseCounter+1) << ": " << number_oftrees << endl;
	}
	return 0;
}
