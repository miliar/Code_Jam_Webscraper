// code_contest.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <cstdio>

using namespace std;

typedef struct __CASE
{
        __CASE(): n(0),A(0), B(0), C(0),
		D(0), x_0(0),y_0(0),M(0){};
        int n;
        int A;
        int B;
        int C;
		int D;
		int x_0;
		int y_0;
		int M;
}TEST_CASE;

typedef struct __POT
{
//        __POT() : x(0), y(0){};
        int x;
        int y;
}POT;

typedef map<int, POT> POTS;

void get_pots(int n, int A, int B, int C, int D, int x_0,int y_0, int M, POTS & pots)
{
	POT co;
	co.x = x_0;
	co.y = y_0;
	pots.insert(make_pair(0,co));
	for (int i = 1; i <= (n-1); i++)
	{
		POT tmp;
		tmp.x = (A*co.x + B)%M;
		tmp.y = (C*co.y + D)%M;
		co.x = tmp.x;
		co.y = tmp.y;
		pots.insert(make_pair(i,tmp));
	}
}


int main()
{
	string tmp;
	ifstream inFile("1.txt");
	map<int, TEST_CASE> diff_case;
	int N = 0;
	getline(inFile,tmp);
    N = atoi(tmp.c_str());

	int case_no = 1;

	while((!inFile.eof()) && (case_no <= N))
	{
	  TEST_CASE test;
      tmp.clear();
	  getline(inFile,tmp);
	  char * cstr;
      cstr = new char [tmp.size()+1];
      strcpy (cstr, tmp.c_str());
	  char * p = strtok(cstr," ");
	  if (p != NULL)
	  {
		  test.n = atoi(p);
		  p = strtok(NULL," ");
	  }
   
	  if (p != NULL)
	  {
		  test.A = atoi(p);
		  p = strtok(NULL," ");
	  }

	  if (p != NULL)
	  {
		  test.B = atoi(p);
		  p = strtok(NULL," ");
	  }
	  
	  if (p != NULL)
	  {
		  test.C = atoi(p);
		  p = strtok(NULL," ");
	  }

	  if (p != NULL)
	  {
		  test.D = atoi(p);
		  p = strtok(NULL," ");
	  }

	  if (p != NULL)
	  {
		  test.x_0 = atoi(p);
		  p = strtok(NULL," ");
	  }

	  if (p != NULL)
	  {
		  test.y_0 = atoi(p);
		  p = strtok(NULL," ");
	  }

	  if (p != NULL)
	  {
		  test.M = atoi(p);
		  p = strtok(NULL," ");
	  }

	  delete [] cstr;
      diff_case.insert(make_pair(case_no,test));
      case_no++;
     }
    
	 map<int, TEST_CASE>::iterator case_it;
     for(case_it = diff_case.begin();
      case_it != diff_case.end(); case_it++)
     {
		
		POTS pots;
		pots.clear();
		get_pots(case_it->second.n, case_it->second.A,
			case_it->second.B,case_it->second.C,case_it->second.D,
			case_it->second.x_0,case_it->second.y_0,case_it->second.M,pots);
		int num = 0;
		POT * set = new POT [(int)pots.size()];
		
		
		POTS::iterator it1;
//		POTS::iterator it2;
//		POTS::iterator it3;
                int cnt = 0;
		for (it1 = pots.begin(); it1 != pots.end(); it1++)
		{
			set[cnt].x = it1->second.x;
			set[cnt].y = it1->second.y;
//                        cout<<set[cnt].x<<" "<<set[cnt].y<<endl;
                        cnt++;
		}

		int limit = ((int)pots.size());

		for(int i = 0; i < (limit-2); i ++)
			for(int j = (i+1); j < (limit-1); j++)
				for(int k= (j+1); k < limit; k++)
				{
					int x1 = set[i].x;
					int x2 = set[j].x;
					int x3 = set[k].x;
					int y1 = set[i].y;
					int y2 = set[j].y;
					int y3 = set[k].y;
					if (((x1+x2+x3)%3 == 0)&&((y1+y2+y3)%3 == 0))
					{
						num ++;
				//		cout<<num<<" "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "
                                //                <<x3<<" "<<y3<<endl;
                                                  
					}
				}
/*
		for(it1 = pots.begin(); it1 != pots.end(); it1++)
		{
			int x1 = it1->second.x;
			int y1 = it1->second.y;
			for(it2 = it1; it2 != pots.end(); it2++)
			{
				if(it2 == it1)
				{
					it2++;
				}
				int x2 = it2->second.x;
				int y2 = it2->second.y;
				if((x2 != x1)&&(y2 != y1))
				{
					for(it3 = it2; it3 != pots.end(); it3++)
					{
						if(it3 == it2)
						{
							it3++;
						}
						int x3 = it3->second.x;
						int y3 = it3->second.y;
						if((x3 != x2) && (x3 != x1) && (y3 != y2) && (y3 != y1))
						{
							if (((x1+x2+x3)%3 == 0)&&((y1+y2+y3)%3 == 0))
							{
								num ++;
							}
						}
					}
				}
			}
		}
*/
		cout<<"Case #"<<case_it->first<<": "<<num<<endl;
		delete [] set;
/*

		 cout << "Case #"<< case_it->first<<case_it->second.n<<" "
			 <<case_it->second.A<<" "<<case_it->second.B<<" "
			 <<case_it->second.C<<" "<<case_it->second.D<<" "
			 <<case_it->second.x_0<<" "<<case_it->second.y_0<<" "
			 <<case_it->second.M<<endl;
*/
//		cout<<"Case #"<<case_it->first<<": "<<switch_no<<endl;
//			cout<<"query: "<<tmp.query[i]<<endl;
     }

	return 0;
}

