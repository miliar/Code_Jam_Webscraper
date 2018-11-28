// gcj_2.cpp : Defines the entry point for the console application.
//

#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
  int t;
  ifstream in("B-large.in");
  ofstream out("output2.txt");
  in>>t;
  int c=t;
  while(t--){
    int n;
    in>>n;
    int s;
    in>>s;
    int p;
    in>>p;
    int count=0;
    while(n--){
      int tscore;
      in>>tscore;
      int s1 = tscore/3;
      int s2 = (tscore-s1)/2;
      int s3 = tscore-s1-s2;
      if(s3>=p || (s>0 && (s1>0 || s2>0) && (s3-s2<1) && (s3+1)>=p)){
        count++;
        if(s3<p){
          s--;
        }
      }
    }
    out<<"Case #"<<c-t<<": "<<count<<endl;
  }
	return 0;
}

