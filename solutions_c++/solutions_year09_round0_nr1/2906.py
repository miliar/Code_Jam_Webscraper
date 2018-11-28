#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include<iterator>

using namespace std;

using namespace std;
#define SOLN

int GiveWater(int y1, int x1);

int T, x, y, L, D, N;
int A[100][100];
int Out[100][100];
char OutPut[100][100];
int i,j,t;

int main()
{
  cin>>L>>D>>N;
  string str[D];
  string casestr[N];

  for (t=0; t<D; t++)
  {
    cin>>str[t];
	}
  for (t=0; t<N; t++)
  {
    cin>>casestr[t];
	}
  for (t=0; t<D; t++)
  {
    //cout <<str[t] << endl;
	}
  for (t=0; t<N; t++)
  {
   // cout << casestr[t]<< endl;
	}

	for(int i = 0 ; i < N ; i++)
	{
		vector<string> strtok;
		int count = 0;
	//	cout << "str : " <<casestr[i] << endl;
		int start = 0, stop = 1;
		for (int j = 0 ; j < casestr[i].length(); j++)
		{
			if(casestr[i].c_str()[j] == '(')
			{
				start = j+1;
				int k = j+1 ;
				for(; k < casestr[i].length();k++)
				{
					if(casestr[i].c_str()[k] == ')')
					{	
						stop = k;
						stop -= start ;
		//				cout << "sub str : " <<casestr[i].substr(start,stop) << endl;
						strtok.push_back(casestr[i].substr(start,stop));

						break;	
					}
				}
				j = k;
			}
			else
			{
		//		cout << "sub str : " <<casestr[i].substr(j,1) << endl;
				strtok.push_back(casestr[i].substr(j,1));
			}
		//	start = j;//start +stop;
		//	stop = 1;
		}
		//cout <<"Case #:" <<i << endl;

		vector<string>::iterator It = strtok.begin();

//	    while ( It != strtok.end() )
//		{
			//cout << *It++ <<endl;
//		}
	//	cout << "checking : " << endl;;
		for(int ii = 0 ; ii < D ; ii++)
		{
			int ccount = 0;
			for(int jj = 0 ; jj < L ; jj++)
			{
				string mains = strtok[jj];
				char chr= 	str[ii].c_str()[jj];
	//			cout << "check " << chr << " in " << mains << endl;
				int found=mains.find(chr);
				   if (found!=string::npos)
				   {
				  //     cout << "Period found at: " << int(found) << endl;
					   ccount +=1;
					   }


			}
			if(ccount == L)
				count+= 1;
	//		cout << "ccount : " << ccount << endl;
		//cout <<"Case #" << i <<": " <<count << endl;
		
		}
		//cout <<"Case #" << i <<": " <<count << endl;
		cout <<"Case #" << i+1 <<": " <<count << endl;






		}
	}
	/*map<int,char> valTochar;
	char prev='a';
	int previnp = Out[0][0];
	valTochar[previnp] = prev;
	OutPut[0][0] = prev;
    for(i=0; i<y; ++i)
	{
    	for(j=0; j<x; ++j)
		{
			map<int,char>::iterator iter_map =  valTochar.find(Out[i][j]);
			if(iter_map == valTochar.end())
			{
				prev +=1;
				valTochar[Out[i][j]] = prev;
			}
				OutPut[i][j] = valTochar[Out[i][j]];
		}
	}
	*/
