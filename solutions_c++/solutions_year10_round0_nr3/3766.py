#include <iostream>
#include <fstream>
#include <queue>
using namespace std;
int main()
{
	//char * str=new char[80];
	//cout<< "Hello. Enter the file name: ";
	//cin >> str;
	ifstream infile("C-small-attempt0.in",ifstream::in);
	ofstream outfile("probc.out",ifstream::out);
	int ni,tests,nj;
	infile >> tests;
	unsigned int r,n,k,el,know,money;
	queue<int> * qmain;
	ni=0;
	while (ni<tests)
	{
		money=0;
		qmain=new queue<int>;
		infile >> r;
		infile >> k;
		infile >> n;
		for (unsigned int i=0; i<n; i++)
		{
			infile >> el;
			qmain->push(el);
		}
		for (unsigned int i=0; i<r;i++)
		{
			know=k;
			nj=0;
			while (nj<qmain->size())
			{
				el=qmain->front();
				if (know>=el)
				{
					money+=el;
					qmain->pop();
					qmain->push(el);
					know-=el;
				}
				else break;
				nj++;
			}
		}
		outfile << "Case #"<<ni+1<<": "<<money<<"\n";
		delete qmain;
		ni++;
	}
	cout << "work of program is ended\n";
	system("pause");
	return 0;
}