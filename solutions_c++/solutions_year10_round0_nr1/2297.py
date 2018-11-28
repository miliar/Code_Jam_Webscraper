#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ofstream out;
ifstream in;

vector<int> ans;
void print_ans()
{
     int sz = ans.size();
     for(int i=1;i<=sz;i++)
     {
	  string temp;
	  if(ans[i-1] == 1) { temp = "ON"; }
	  else { temp = "OFF"; }
	  out<<"Case #"<<i<<": "<<temp<<"\n";
     }
}



int calc(long long N, long long K)
{
     int ret = 0;
     long long temp = 1; 
     temp = temp << N;
     temp--;
     if((K & temp) == temp) { ret = 1; }
     return ret;
}



int main()
{

     in.open("A-large.in");
     out.open("A-small.out");
     int T;
     in>>T;
     for(int i=0;i<T;i++) {
	  long long N;
	  long long K;
	  in>>N;
	  in>>K;
	  int on = calc(N,K);
	  ans.push_back(on);

     }
     print_ans();
     in.close();
     out.close();
     return 0;
}
