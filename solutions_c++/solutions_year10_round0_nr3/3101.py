#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cmath>

using namespace std;

int main() 
{
  int no_args;
  int R,K,N;
  int gi[1000];
  int steps[1000];
  int amount[1000];
  int euros;
  int loc;
  int total_pass=0;
  
  ifstream in_stream;
  ofstream out_stream;

  in_stream.open("/home/se/Downloads/C-small-attempt0.in");
  out_stream.open("file_theme.out");

  if (in_stream.fail() || out_stream.fail())
  {
      cout << "Agh file couldn't be opened, exiting now" << endl;
      exit(1);
  }

  in_stream >> no_args;

  for (int i=0; i<no_args; i++)
  {

    in_stream >> R;
    in_stream >> K;
    in_stream >> N;


    total_pass=0;
    for (int j=0; j<N; j++) {
      in_stream >> gi[j];
      total_pass+=gi[j];

    }

    for (int j=0; j<N; j++) {
      int point=1;
      int tot = gi[j];
      
      while ( (gi[(j+point)%N]+tot) <= K && (gi[(j+point)%N]+tot)<=total_pass)
	{
	  tot=tot+gi[(j+point)%N];
	  point++;
	  
	}

      steps[j]=(j+point)%N;
      amount[j]=tot;


    }
    
    euros=0;
    loc=0;
    for (int j=0; j<R; j++) {
      euros = euros+ amount[loc];
      loc = steps[loc];
      
    }
    
    out_stream << "Case #" << i+1 << ": " << euros << endl;

    
  }
 

  in_stream.close();
  out_stream.close();

}
  
