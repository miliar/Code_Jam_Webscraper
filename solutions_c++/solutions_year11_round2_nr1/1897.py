
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
  const char filein[] = "A-large.in";
  const char fileout[] = "A-large.out";
  ifstream i_file;
  ofstream o_file;
  int num_case = 0;

  i_file.open(filein);
  o_file.open(fileout);
  if(i_file.is_open())
    {
      i_file>>num_case;
      for(int i=0; i<num_case; i++)
	{
	  int N;
	  i_file>>N;
	  char** matrix = new char*[N];
	  for(int j=0; j<N; j++) {
	    matrix[j] = new char[N];
	    for(int k=0; k<N; k++)
	      i_file>>matrix[j][k];
	  }
	  float* WP = new float[N];
	  int* win = new int[N];
	  int* total = new int[N];
	  for(int j=0; j<N; j++) {
	    int win1=0, total1=0;
	    for(int k=0; k<N; k++) {
	      if(matrix[j][k] == '1') {
		total1++;
		win1++;
	      }
	      else if(matrix[j][k] == '0') {
		total1++;
	      }
	    }
	    win[j]=win1;
	    total[j]=total1;
	    WP[j]=(float)win1/total1;
	  }
	  float* OWP = new float[N];
	  for(int j=0; j<N; j++) {
	    float temp = 0;
	    for(int k=0; k<N; k++) {
	      if(matrix[j][k] == '0') {
		temp += (float)(win[k]-1)/(total[k]-1);
	      }
	      else if(matrix[j][k] == '1') {
		temp += (float)(win[k])/(total[k]-1);
	      }
	    }
	    OWP[j] = temp/total[j];
	  }
	  float* OOWP = new float[N];
	  for(int j=0; j<N; j++) {
	    float temp = 0;
	    for(int k=0; k<N; k++) {
	      if(matrix[j][k] == '0' || matrix[j][k] == '1') {
		temp += OWP[k];
	      }
	    }
	    OOWP[j] = temp/total[j];
	  }
	  o_file<<"Case #"<<(i+1)<<":"<<endl;
	  for(int j=0; j<N; j++) {
	    o_file<<(0.25*WP[j] + 0.50*OWP[j] + 0.25*OOWP[j])<<endl;
	  }
	  for(int j=0; j<N; j++) {
	    delete []matrix[j];
	  }
	  delete []matrix;
	  delete []WP;
	  delete []OWP;
	  delete []win;
	  delete []total;
	}
    }
    i_file.close();
    o_file.close();
  return 0;
}
