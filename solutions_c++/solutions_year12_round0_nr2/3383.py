#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int dance(int googlers, int sup, int best, vector<int> v)
{
    int counter = 0;
    for(int i=0; i<v.size(); i++)
    {
         if(v[i]!=0)
         {
             int d = v[i]/3;
             int r = v[i]%3;
             if(d>=best)
                  counter++;
             else if (d==best-1 && r>0)
                  counter++;
             else if ( ((d==best-1 && r==0) || (d==best-2 && r==2)) && sup>0 )
                  {
                       counter++;
                       sup--;
                  }
         }
         else if(best==0) counter++;
    }
    return counter;
}

int main()
{
	ifstream infile ("B-large.in");
	ofstream outfile("B.out");

	int N, x,y,z;
	infile >> N;
	string line;
	getline (infile,line);
	for(int i=0; i<N; i++)
	{
        outfile << "Case #" << i+1 << ": ";
        infile >> x >> y >> z;
        vector<int> v;
        for(int j=0; j<x; j++)
        {
              int tmp=0;
              infile >> tmp;
              v.push_back(tmp);
        }
        outfile << dance(x,y,z,v);
        outfile << "\n";
    }


	infile.close();
	outfile.close();
	system("pause");
}
