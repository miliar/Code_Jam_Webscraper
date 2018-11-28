#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
    vector<long long> a;
	int cases=0,caseCnt=1,p=0,k=0,l=0;
	long long ans =0,temp=0;
	in>>cases;
	while(caseCnt<=cases)
	{
	    ans=0;
	    a.clear();
		// stuff for reading in the input
		in>>p>>k>>l;
		if(p*k<l)goto next;
		for(int i=0;i<l;i++)
		{
		    in>>temp;
		    a.push_back(temp);
		}
		sort(a.begin(),a.end());
		reverse(a.begin(),a.end());
		long long t1=0;
		for(int i=0;i<l;i++)
		{
		    t1=(i/k)+1;
		    ans+=a[i]*((i/k)+1);
		}
		// stuff for formatting the output
next:
        out<<"Case #"<<caseCnt<<": "<<ans<<endl;
        caseCnt++;
	}
	return 0;
}
