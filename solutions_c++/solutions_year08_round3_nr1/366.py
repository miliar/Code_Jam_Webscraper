#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <bitset>
#include <stack>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <memory>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <fstream>

#define ALL(c) c.begin(),c.end()
#define pb push_back
#define For_iter(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end();++BB)
long long letter[2000];
using namespace std;
int main()
{
     ifstream fin;
     ofstream fout;
     fin.open("A-large.in");
     fout.open("result");
     int n;
     fin>>n;
     for(int i=0;i<n;i++){
		int p,k,l;
		fin>>p>>k>>l;
		memset(letter,0,sizeof(letter));
		for(int j=0;j<l;j++){
			fin>>letter[j];	
		}
		for(int x=0;x<l;x++){
			int max=x;
			for(int y=x;y<l;y++){
				if(letter[y]>letter[max]){
					max=y;
				}
			}
			int temp;
			temp=letter[max];
			letter[max]=letter[x];
			letter[x]=temp;
		}
		for(int j=0;j<l;j++){
			//cout<<letter[j]<<' ';
		}
	//	cout<<endl;
		long long result=0,pos=0;
		for(long long x=0;x<p&&pos<l;x++){
			for(int y=0;y<k&&pos<l;y++){
				result+=letter[pos++]*(x+1);
			}
		}
		cout<<result<<endl;
		fout<<"Case #"<<i+1<<": "<<result<<endl;
	 }

     if(!fin) cout<<"Cannot open!"<<endl;
     system("PAUSE");
     return 0; 
}
