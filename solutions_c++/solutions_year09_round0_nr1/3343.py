#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <strstream> 


using namespace std;

struct testcasealienC
{
	char* possiblechar;
	int possiblecharlen;
	int posinword;
};

void CheckInDic(testcasealienC* testC, int L, string* dic, int D);

int possiblecount = 0;

int main(int argc, char *argv[])
{
  ifstream filein("A-small-attempt0.in");
  ofstream oFile("A-small-attempt0.out");

  int L;
  int D;
  int N;
  filein >> L;
  filein >> D;
  filein >> N;

  string *dic = new string[D];
  for(int i = 0; i < D; i++)
  {
	filein >> dic[i];
  }

  for(int i = 0; i < N; i++)
  {
	  possiblecount = 0;
	  string testcase; 
	  filein>> testcase;//(ab)(bc)(ca)
	  testcasealienC* testC = new testcasealienC[L];
	  for(int jj = 0 ; jj < L; jj++)
	  {
		  testC[jj].possiblechar = new char[testcase.length()];
	  }
	  //for(int j = 0; j < L; j++)
	  int j = 0;
	  int possiblecharcount = 0;
	  {
		  char* testCchar = new char[testcase.length()];
		  memcpy(testCchar, testcase.c_str(), testcase.length());
		  bool hold = false;

			for(int k = 0; k < testcase.length(); k++)
			{
				if(testCchar[k] == '(')
				{
					hold = true;
					continue;
				}
				if(testCchar[k]  == ')')
				{
					hold = false;				
					testC[j].posinword = j;
					testC[j].possiblecharlen = possiblecharcount;
					possiblecharcount = 0;
					j++;
					continue;
				}
				testC[j].possiblechar[possiblecharcount] =testCchar[k];
				if(hold)
				{
					possiblecharcount++;
				}
				else
				{
					possiblecharcount = 1;
					testC[j].posinword = j;
					testC[j].possiblecharlen = possiblecharcount;
					possiblecharcount = 0;
					j++;
				}
			}
	  }
 ////init done


	  CheckInDic(&testC[0], L, dic, D);
	  oFile << "Case #"<< i + 1 << ": " << " " << possiblecount << endl;
  }



  
  system("pause");
   filein.close();
   oFile.close();

}


void CheckInDic(testcasealienC* testC, int L, string* dic, int D)
{
	  string* dictionary = new string[D];
	  int* dicreserv = new int [D];

	  int diclen = D;
	  
	  for(int di = 0; di < D; di++)
	  {
//			dictionary[di] = dic[di];
			dicreserv[di] = 0;
	  }

	  for(int lk = 0; lk < testC[0].possiblecharlen; lk++)
	  {
		  int diclennew = 0;
		  for(int dicout = 0; dicout < diclen; dicout++)
		  {
			  char* testdic = new char[dic[dicout].length()];
			  memcpy(testdic, dic[dicout].c_str(), dic[dicout].length());
			  if(testC[0].possiblechar[lk] == testdic[0])
			  {
				  if(dic[dicout].length() == 1)
				  {
					  possiblecount++;
					  return;
				  }
				  else
				  {
					  dictionary[diclennew] = dic[dicout].substr(1,dic[dicout].length() -1);
					  diclennew++;
					  //dicreserv[dicout] = 1;
				  }
			  }
			  //else
			  //{
					//dicreserv[dicout]= -1;
			  //}
		  }
		  //int dicr = 0;
		  
		 //for(int dicout = 0; dicout < diclen; dicout++)
		 //{
			// if(dicreserv[dicout] == 0)
			// {
			//	 diclennew++;
			//	 dicr = dicout + 1;
			//	 continue;
			// }
			// if(dicreserv[dicout] == 0)
			//	 break;
			//while(dicreserv[dicr] == -1) dicr++;
			//if(dicr >= diclen)
			//	break;
			//dictionary[dicout] = dictionary[dicr];		
			//diclennew++;
		 //}
		  if(diclennew > 0)
			 CheckInDic(&testC[1], L - 1, dictionary, diclennew);
	  }
	  return;
}