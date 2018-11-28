#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void Bubble_Sort(int a[], int n)
{int tmp;
  for (int i=0; i < n-1; i++)
    for (int j=0; j < n-1-i; j++)
      if (a[j+1] < a[j]) //compare adjacent elements
      { //swap a[j] and a[j+1]
        tmp = a[j];
        a[j] = a[j+1];
        a[j+1] = tmp;
      }
}// end bubbleSort

void display (int a[], int n)
{
  for (int i = 0; i <n; i++)
    {
      cout << a[i]<<endl;
    }
}

void remove( int a[], int& n, int i)
{
  for (int j = i; j < n - 1; j++)
  {
    a[j] = a[j+1];
  }
  n--;
}  

int main()
{
  ifstream infile;
  int questions;
  int turnovertime;
  int NA;
  int NB;
  infile.open ("Input.in");
  infile >>questions;
  string s;
  int current_question = 1;
  while (questions >= current_question)
  {
	  infile >> turnovertime;
    //cout <<"turnovertime" <<turnovertime<< endl;
	  infile >> NA;
	  infile >> NB;
	  int NA_departure[NA];
	  int NA_arrival[NA];
	  int NA_departure_size = 0;
	  int NA_arrival_size = 0;
	  int NB_departure[NB];
	  int NB_arrival[NB];
	  int NB_departure_size = 0;
	  int NB_arrival_size = 0;
	  int count = 0;
	  while ( NA  > count)
	  {
         infile >> s;
		     string ns = s.substr(0,2) + s.substr(3,2);
		     //cout << ns<<endl;
		     NA_departure[NA_departure_size] = atoi(ns.c_str()); 
		     infile >> s;
		     ns = s.substr(0,2) + s.substr(3,2);
		     NA_arrival[NA_arrival_size] = atoi(ns.c_str()); 
         NA_arrival[NA_arrival_size] = NA_arrival[NA_arrival_size] + turnovertime;
        // cout <<NA_arrival[NA_arrival_time]<<endl;
		     NA_departure_size++;
         NA_arrival_size++;
         
		 count++;
	  }
	  //cout <<"NA_departure_time" <<NA_departure_size<<endl;
	  //cout <<"NA_arrival_time" <<NA_arrival_size<<endl;
	  count = 0;
	  while ( NB  > count)
	  {
         infile >> s;
		 string ns = s.substr(0,2) + s.substr(3,2);
		// cout << ns<<endl;
		 NB_departure[NB_departure_size] = atoi(ns.c_str()); 
		 infile >> s;
		 ns = s.substr(0,2) + s.substr(3,2);
		 NB_arrival[NB_arrival_size] = atoi(ns.c_str());
     NB_arrival[NB_arrival_size] = NB_arrival[NB_arrival_size] + turnovertime; 
      //cout <<NB_arrival[NB_arrival_time]<<endl;
		 NB_departure_size++;
         NB_arrival_size++;
         
		 count++;
	  }
	  //cout <<"NB_departure_time" <<NB_departure_size<<endl;
	  //cout <<"NB_arrival_time" <<NB_arrival_size<<endl;
    Bubble_Sort(NA_departure, NA_departure_size);
    Bubble_Sort(NB_departure, NB_departure_size);
    //display(NA_departure, NA_departure_size);
    //display(NB_departure, NB_departure_size);
    int trainA = NA;
    int trainB = NB;
    for (int i =0; i < NA_departure_size; i++)
    {
      for (int j =0; j < NB_arrival_size; j++)
      {
        if( NA_departure[i] >= NB_arrival[j])
        {
          remove(NB_arrival, NB_arrival_size, j);
          j = NB_arrival_size + 1;
          trainA--;
        }
      }
    }
    //calculate how many train we need from B to A
    for (int i =0; i < NB_departure_size; i++)
    {
      for (int j =0; j < NA_arrival_size; j++)
      {
        if( NB_departure[i] >= NA_arrival[j])
        {
          remove(NA_arrival, NA_arrival_size, j);
          j = NA_arrival_size + 1;
          trainB --;
        }
      }
    }
    cout << "Case #"<<current_question<<": "<<trainA<<" "<<trainB<<endl;
	  current_question++;
  }
  
}