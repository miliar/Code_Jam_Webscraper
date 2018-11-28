#include <iostream>
#include <fstream>
#include <vector>
#include <list>

using namespace std;

int calculation(int credit, vector<int>price,int i);

int main()
{
	ifstream inFile;
	int caseSize=0;
	inFile.open("A-small-practice.in");
	inFile>>caseSize;
	int credit,itemNum,price;
	vector<int> priceV,position;
	int y=0;
	while(!inFile.eof())
	{
		int i;
		inFile>>credit>>itemNum;
		for( i=0;i<itemNum;i++)
		{
			inFile>>price;
			priceV.push_back(price);
		}
		calculation(credit,priceV,y++);
		cout<<endl;
		priceV.clear();
	}
	return 0;
}

int calculation(int credit, vector<int> price,int m)
{
	vector<int>::iterator iter,iter2;
	list<int> p;
	for(int i=0;i<price.size();i++)
	{
		if(price[i]<credit)
		{
			for(int j=0;j<price.size();j++)
			{
				if(price[j]<credit && price[i]+price[j] == credit && i!=j)
				{
					p.push_back(i+1);
					p.push_back(j+1);
					p.sort();
					cout<<"Case #"<<++m<<": ";
					for(list<int>::iterator iter=p.begin();iter!=p.end();iter++)
						cout<<*iter<<" ";
					return 1;
				}		
			}
		}
	}
	
	
	
	
	
}

