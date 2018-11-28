#include <string>
#include <cstdio>
#include <iostream>
using namespace std;

string a[31]= { "",
		"005",
		"027",
		"143",
		"751",
		"935",
		"607",
		"903",
		"991",
		"335",
		"047",
		"943",
		"471",
		"055",
		"447",
		"463",
		"991",
		"095",
		"607",
		"263",
		"151",
		"855",
		"527",
		"743",
		"351",
		"135",
		"407",
		"903",
		"791",
		"135",
		"647"
};

int main()
{
  int T, n;
  cin>>T;
  for(int t = 0 ; t < T; ++t) {
    cin>>n;
    cout<<"Case #"<<(t+1)<<": "<<a[n]<<endl;
  }
}
