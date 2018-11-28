#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cmath>

using namespace std;


/*
typedef pair<char, int> botP;
typedef vector<int> intV;
typedef vector<botP>  pairV;
typedef pairV::iterator pairVIter;
typedef intV::iterator intVIter;
*/



string getAlg()
{
	string alg;
	int flag[26] = {0};
	vector<int> index;

	string inStr= ("qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
	string outStr=("zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");


	 for(int i=0; i< 26; i++)
	{
		alg.push_back('?');
	}

	for(int i=0; i< inStr.size(); i++)
	{
		if(inStr[i]!=' ')
		{
			alg[inStr[i]-'a']=outStr[i];
			flag[outStr[i]-'a']=1;
		}
	}
	
	for(int i=0; i< 26; i++)
	{
		if (flag[i]==0)
		{
			index.push_back(i);
		}
	}

	if(index.size()==1)
	{
		int i=0;
		while(alg[i]!='?' && i<26)
			i++;
		alg[i]=(char)(index[0]+'a');
	}
	else
	{
		cout<<"More than one characters undefined"<<endl;
	}

	return alg;

	/*
    for(int i=0; i< 26; i++)
	{
		cout<<alg[i];
	}
    cout<<endl;
	*/
 
}




string translate(string alg,  string cVec)
{
	for(int i=0; i<cVec.size(); i++)
	{
		if(cVec[i]!=' ')
		{
			cVec[i]=alg[cVec[i]-'a'];
		}
	}  
	return cVec;
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
  
  string alg=getAlg();

  ifstream in_file(inFileName.c_str());
  ofstream out_file(outFileName.c_str());

  in_file>>num_case;
  getline(in_file, line);//ignore 1st line
  //cout<<num_case<<" test cases "<<endl;
    
  int caseNum=1;
  while (getline(in_file, line))
  {
      line=translate(alg, line);
      out_file<<"Case #"<<caseNum<<": "<<line<<endl;        
      line.clear(); 
      caseNum++;       
  }    
    return 1;    
}
