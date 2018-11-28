#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cmath>

using namespace std;

int main() 
{
  int no_args;
  int N, N2;
  int K;
  bool on;


  ifstream in_stream;
  ofstream out_stream;

  in_stream.open("/home/se/Downloads/A-large.in");
  out_stream.open("file.out");

  if (in_stream.fail() || out_stream.fail())
  {
      cout << "Agh file couldn't be opened, exiting now" << endl;
      exit(1);
  }

  in_stream >> no_args;

  cout << "no_args is: " << no_args << endl;

  for (int i=0; i<no_args; i++)
  {
    in_stream >> N;
    in_stream >> K;
    
    N2 = pow(2,N);

    on = false;

    if ( K < N)
      on = false;
    else if ((K & 1) == 0)
      on = false;
    else if ((N2 - K%N2)==1)
      on = true;


    


      

    out_stream << "Case #" << i+1 << ": ";
 
   if (on)
      out_stream << "ON";
   else
      out_stream << "OFF";
   
   out_stream << endl;

  }

  in_stream.close();
  out_stream.close();

}
  
