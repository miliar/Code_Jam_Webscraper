//============================================================================
// Name        : m.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <vector>
#include<numeric>
#include <fstream>
 using namespace std;

int main () {
  vector <int> tab;
  ifstream myfile ("A-large.in");
  if (myfile.is_open())
  {
   // while ( myfile.good() )
    {
    	int T; //ilosc danych
    	myfile >> T;
    	tab.resize(T);
    	int N;
    	for(int i=0;i<T;i++)
    	{
    	myfile>>N;
    	vector <int> P (N);
    	vector <char> R (N);
    	for (int j=0;j<N;j++) myfile>>R[j]>>P[j];

    	int posO =1, posB=1;
    	int time=0;
    	int wO=0, wB=0;
    	for (int j=0;j<N;j++)
    	{
    	if (R[j]=='O')
			{
    		int temp= abs(P[j]-posO)+1-wO;
    		if (temp>0) time+=temp;
    		else time++;


    		wB+=abs(P[j]-posO)+1-wO;
    		if(wB<1) wB=1;
    		wO=0;
    		posO=P[j];
			}
    	else
			{
    		int temp= abs(P[j]-posB)+1-wB;
    		if (temp>0) time+=temp;
    		else time++;


    		wO+=abs(P[j]-posB)+1-wB;
    		if (wO<1) wO=1;
    		wB=0;
    		posB=P[j];
			}

    	}
    	tab[i]=time;
    	}
    }
    myfile.close();


  }

  else cout << "Unable to open file";

  ofstream file2 ("A-large.out");
    if (file2.is_open())
    { for(int i=0;i<tab.size();i++)
     file2<<"Case #"<<i+1<<": "<<tab[i]<<endl;
      file2.close();
    }
    else cout << "Unable to open file";

  return 0;
}
