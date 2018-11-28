#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void Bubble_Sort(int a[], int n)
{int tmp;
  for (int i=0; i < n-1; i++)
    for (int j=0; j < n-1-i; j++)
      if (a[j+1] > a[j]) //compare adjacent elements
      { //swap a[j] and a[j+1]
        tmp = a[j];
        a[j] = a[j+1];
        a[j+1] = tmp;
      }
}// end bubbleSort

int main()
{
  ifstream infile;
  string names;  
  int questions;
  infile.open ("Input.in");
  //cout <<"START"<<endl;
  infile >> questions;
  int current_question = 1;
  int P;
  int K;
  int L;
  while (questions >= current_question)
  {
     infile >> P;
	 infile >> K;
	 infile >> L;
	 int num[L];
	 int num_size = 0;
	 long int total = 0;
	 //cout <<P<<K<<L<<endl;
	 while (num_size < L)
	 {
	    ///cout <<"Read"<<endl;
	    infile >> num[num_size];
		//cout <<num[num_size]<<endl;
		num_size++;
		
	 }
	// cout <<"HI"<<endl;
	 Bubble_Sort(num, num_size);
	 int cycle = 1;
	 int count = 1;
	 for (int i =0; i < num_size; i++)
	 {
	    total = total + num[i] * cycle;
		count ++ ;
		if ( count > K)
		{
		   cycle ++;
		   count =1;
		}
		//cout<<"run"<<endl;
	 }
	
	cout << "Case #"<<current_question<<": "<<total<<endl;
    current_question++;
  }
  
  
  }
