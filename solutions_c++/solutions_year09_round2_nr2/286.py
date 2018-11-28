#include <iostream>  
#include <string>  
#include <vector>  
#include <set>  
#include <map>  
#include <algorithm>  
#include <math.h>  
#include <sstream>  
#include <ctype.h>  
#include <queue>  
#include <stack>  
#include <fstream>
using namespace std;  

template<class Item>  
void display(vector<Item> v)  
{  
  for(int i=0; i<v.size(); i++)  
    cout << v[i] << ' ';  
  cout << '\n';  
}   


int main()
{

int L, D, N;

fstream In("b-large.in", ios::in);
fstream Out("b-large.out", ios::out);

int T;

In >> T;

for(int h=0; h<T; h++)
{
Out << "Case #" << h+1 << ": ";
string cur;

In >> cur;

vector<int> nums(10, 0);

char c = cur.size()-1;
int i;
for(i=cur.size()-1; i>-1; i--)
{
	nums[cur[i]-'0']++;
	if(cur[i] < c) break;
	c = max(c, cur[i]);
}
if(i==-1)
{
	i++;
	cur = "0" + cur;
	nums[0]++;
}

int n = cur[i]-'0';
int j;
for(j=n+1; nums[j] ==0; j++);
cur[i] = j+'0';
nums[j]--;

i++;
for(int j=0; j<10; j++)
{
	while(nums[j])
	{
		nums[j]--;
		cur[i++] = '0' + j;
	}
}

Out << cur << endl;


}


In.close();

Out.close();

return 0;

}
