#include <iostream>
#include <queue>
#include <vector>
#include <fstream>


using namespace std;

ofstream out;
ifstream in;

queue<int> orig;
queue<int> curr;
vector<int> profit;

vector<vector<int> > ans;



string tostring(vector<int> a)
{
     string ans;       
     int sz = a.size();
     for(int i=0;i<sz;i++)
     {

	  ans.push_back( '0' + a[i]);
     }
     reverse(ans.begin(),ans.end());       
     return ans;       
}
void print_ans()
{
     int sz = ans.size();
     for(int i=1;i<=sz;i++)
     {
	  out<<"Case #"<<i<<": "<<tostring(ans[i-1])<<"\n";
     }
}

void add (int k)
{
     int i = 0;     
     while(k>0)
     {     
	  if(i>= profit.size()) {profit.push_back(k%10); k = k/10; }
	  else { k = profit[i]+k ; profit[i] = k%10; k = k/10; }     
	  i++;
     }
}



void mul (int k)
{
     int i = 0;     
     int carry = 0;
     while(i<profit.size() || carry != 0)
     {
	  if(profit.size() == i ) { profit.push_back(carry%10); carry = carry/10; }                           
	  else { carry = profit[i]*k + carry ; profit[i] = carry%10; carry = carry/10; }
	  i++;
     }

}




void calc(unsigned long long R, unsigned long long k)
{

     unsigned int i = 0;   
     vector<int> temp; 
     do
     {    
	  i++;
	  int f;
	  int capacity = k;
	  int count = 0;
	  int sz = curr.size();
	  while(count<sz){
	       f = curr.front();
	       //cout<<capacity<<" "<<f<<"\n";
	       if(capacity>=f) { capacity -= f ; curr.pop();curr.push(f);}
	       else { break; }
	       add(f);
	       count++;
	  }
	  temp.push_back(k-capacity);
	  //cout<<tostring(profit)<<"\n";
     }while(i<R && curr!=orig);




     int multiply = R / i;
     R= R%i;
     if(multiply>0) { mul(multiply); }
     for(int j=0;j<R;j++)
     {
	  add(temp[j]);
     }
}


void cl(queue<int> &q)
{
while(!q.empty()) q.pop();     
}


int main()
{
     in.open("C-small-attempt2.in");
     out.open("C-small.out");
     int T;
     in>>T;
     for(int i=0;i<T;i++) {
      profit.clear();
      cl(orig);
      cl(curr);             
	  unsigned long long R;
	  unsigned long long k;
	  unsigned long long N;
	  in>>R;
	  in>>k;
	  in>>N;
	  for(int j=0;j<N;j++)
	  {
	       int temp;
	       in>>temp;
	       orig.push(temp);         
	       curr.push(temp);
	  }
	  calc(R,k);
	  ans.push_back(profit);

     }
     print_ans();
     in.close();
     out.close();
     return 0;
}
