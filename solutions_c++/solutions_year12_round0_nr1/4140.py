#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cmath>
#include <map>
using namespace std;


string translate(map<char, char> dict, string inStr)
{
	string outStr;
    for(int i=0; i<inStr.size(); i++)
	{
		if(inStr[i] != ' ') 
		{
		   outStr += dict[inStr[i]];
		}
		else
		{
		   outStr +=" ";
		}
	}
    return outStr;
}

int main()
{
  int num_case;
  string line;
  string inFileName, outFileName;
  cout<<"input data file name:"<<endl;
  cin>>inFileName;
  cout<<"input output file name:"<<endl;
  cin>>outFileName;
  
  ifstream in_file(inFileName.c_str());
  ofstream out_file(outFileName.c_str());

  in_file>>num_case;
  getline(in_file, line);//ignore 1st line
  //cout<<num_case<<" test cases "<<endl;
  map<char, char> dict;
  dict['a']='y';
  dict['b']='h';
  dict['c']='e';
  dict['d']='s';
  dict['e']='o';
  dict['f']='c';
  dict['g']='v';
  dict['h']='x';
  dict['i']='d';
  dict['j']='u';
  dict['k']='i';
  dict['l']='g';
  dict['m']='l';
  dict['n']='b';
  dict['o']='k';
  dict['p']='r';
  dict['q']='z';
  dict['r']='t';
  dict['s']='n';
  dict['t']='w';
  dict['u']='j';
  dict['v']='p';
  dict['w']='f';
  dict['x']='m';
  dict['y']='a';
  dict['z']='q';

  int caseNum=1;
  while (getline(in_file, line))
    {
        out_file<<"Case #"<<caseNum<<": "<<translate(dict, line)<<endl;
		caseNum++;
    }    
    return 1;    
}
