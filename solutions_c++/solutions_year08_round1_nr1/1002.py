#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;

void main()
{
	ifstream ifile("A-small-attempt2.in.txt");
	ofstream ofile("output.txt");
	int caseNum,vNum;
	ifile>>caseNum;
	//	cout<<caseNum<<endl;
	int i,j,k;
    for(i=0;i<caseNum;++i)
	{
		int res =0;
		int product;
		int temp;
		vector<int> v1,v2;
		
		ifile>>vNum;
		//cout<<vNum<<endl;
		for(j=0;j<vNum;++j)
		{
			ifile>>temp;
		//cout<<temp<<endl;
			v1.push_back(temp);
		}

		for(j=0;j<vNum;++j)
		{
			ifile>>temp;
		//cout<<temp<<endl;
			v2.push_back(temp);
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end(),greater<int>());
		for(j=0;j<vNum;j++)
			res += v1[j] * v2[j];
		//do {
		//			do {
		//				product = 0;
		//				for(j=0;j<vNum;++j)
		//				{
		//					product += v1[j] * v2[j];
		//					//	if (product>res) break;	
		//				}
		//				if (res>product) res=product;
		//				
		//			} while(next_permutation(v2.begin(),v2.end()));     		
		//		} while(next_permutation(v1.begin(),v1.end()));
		
		
		cout<<"Case #"<<i+1<<":"<<res<<endl;
		string output("Case #");
		ostringstream s,s1;
		s<<i+1;
		output+=s.str();
		output+=": ";
		s1<<res;
		output+=s1.str();
		ofile<<output<<endl;
		v1.clear();
		v2.clear();

	}
}