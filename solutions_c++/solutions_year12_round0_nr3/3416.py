#include <iostream>
#include <fstream>
#include <math.h>
#include <vector>
using namespace std;

int string2int(string x)
{
    int z = 0;
    for(int i=0; i<x.length(); i++)
    {
            z*=10;
            z+=(int)x[i]-48;
    }
    return z;
}

string int2string(int z)
{
    string y;
    while(true)
    {
         int r = z % 10;
         z = z/10;
         y+=r+48;
         if(z==0)
              break;
    }
    for(int i=0; i<y.length()/2; i++)
    {
         char tmp = y[i];
         y[i] = y[y.length()-1-i];
         y[y.length()-1-i] = tmp;
    }
    return y;
}

int recycled(string x, string y)
{
    int counter=0;
    if(x.length()<2)
        return 0;
    //else return 1;
    int a = string2int(x);
    int b = string2int(y);
    vector< pair<int,int> > result;
    for(int i=a; i<b; i++)
    {
         string tmp = int2string(i);
         for(int j=1; j<tmp.length(); j++)
         {
              string tmp2;
              int k=j;
              while(tmp2.length()!=tmp.length())
              {
                   tmp2+=tmp[k]; k++;
                   if(k==tmp.length())
                   k=0;
              }
              // i, ii
              int ii = string2int(tmp2);
              //if(ii<=b && ii>=a && i<ii)
              if(ii<=b && ii>=a && i<=b && i>=a && i<ii)
              {
                       counter++;
                   pair<int,int> p (i,ii);
                   //cout << endl << i << "-" << ii;
                   //pair<int,int> pp (ii,i);
                  /* if(i>ii)
                   {
                        int temp = i;
                        i = ii;
                        ii = temp;
                   }*/
                   result.push_back(p);
                   //result.push_back(pp);
              }
         }
    }
              
    vector< pair<int,int> >::iterator it;
    it = unique(result.begin(), result.end());
    result.resize( it - result.begin() );        
    
    
    return result.size();
}

int main()
{
	ifstream infile ("C-small-attempt2.in");
	ofstream outfile("C.out");

	int N;
    string x, y;
	infile >> N;
	string line;
	getline (infile,line);
	for(int i=0; i<N; i++)
	{
        outfile << "Case #" << i+1 << ": ";
        infile >> x;
        infile >> y;
        //infile >> line;
        //cout << line << endl;
        //getline (infile,line);
        //cout << line[1] << endl;
        //cout << tab << endl;
        outfile << recycled(x,y);
        outfile << "\n";
    }


	infile.close();
	outfile.close();
	system("pause");
}
