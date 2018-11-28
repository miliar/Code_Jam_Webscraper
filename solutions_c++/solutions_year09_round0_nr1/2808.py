#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <ctime>
#include <utility>

using namespace std;


#define PB push_back
#define mset(x,a) memset(x,(a),sizeof(x))
#define SIZE(X) ((int)X.size())


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	string data;
	string dic[5005];
    int l;
	int d;
	int cases;
	int k=1,i;
    cin>>l>>d>>cases;
	for (i=0;i<d ;i++ )
	{
		cin>>dic[i];
	}

    while (cases--)
    {
		int count=0,f=0;
		string form[16];		
	    string t;
		int j,g=0,q=0,z;
        cin>>data;

		for (i=0;i<d ;i++ )
		{
			if(dic[i]==data) {count++;f++;}
		}
		if(f==1){cout<<"Case #"<<k<<": "<<count<<endl;k++;continue;}
		for (i=0;i<data.size() ;i++ )
		{
			if(data[i]!='(') {form[g]+=1;form[g][0]=data[i];g++;}
			else {
				   i++;
				   while (data[i]!=')')
				   {
                         form[g]+=1;
                         form[g][q]=data[i];
						 i++;q++;
				   }
				   g++;q=0;
			     }
		}
        for (i=0;i<d ;i++ )
        {
               for (j=0;j<l ;j++ )
               {
				   for (z=0;z<form[j].size() ;z++ )
				   {
					   if(dic[i][j]==form[j][z]) {f++;break;}
				   }
               }
			   if(f==l) count++;
			   f=0;
        }
		cout<<"Case #"<<k<<": "<<count<<endl;k++;
    }
	return 0;
}
