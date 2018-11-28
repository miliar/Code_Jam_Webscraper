#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <stdio.h>

using namespace std;

int main(int argc, char ** argv)
{
	int N;
	ifstream f(argv[1]);
	f >> N ;
		
	for(int n=0; n<N; ++n)
	{
        string num;
        f>>num;
        int base=0;
        for(int i=0;i<num.length();++i)
        {
            bool diff=true;
            for(int j=0;j<i && diff==true;++j)
                if(num[i]==num[j]) diff=false;

            if(diff==true) ++base;
        }
        if(base<2) base=2;
        //cout << base << endl;
        vector<int> val(num.length());
        map<char,int> dict;
        bool first=true;
        int max=2;
        for(int i=0;i<num.length();++i)
        {
            if(i==0) {
                val[i]=1; 
                dict[num[i]]=1;
            }
            else if(dict.find(num[i])==dict.end() && first==true) {
                first=false; 
                val[i]=0;
                dict[num[i]]=0;
            }
            else if(dict.find(num[i])==dict.end() && first==false) 
            {
                val[i]=max;
                dict[num[i]]=max;
                ++max;
            }
            else
            {
                val[i]=dict[num[i]];
            }
        }
        long long int res=0;
        long long int pow=1;
for(int i=0;i<num.length();++i)
        {
      //      cout << val[i];
        }
        for(int i=num.length()-1;i>=0;--i)
        {
            res+=val[i]*pow;
            pow*=base;
        }

		cout << "Case #" << n+1 << ": " <<  res << endl;
	}


	return 0;
}
