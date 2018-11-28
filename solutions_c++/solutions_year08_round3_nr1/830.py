#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;


 typedef vector<string> vs;
 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
//Take the Input.
 // for the number of keys Do:
 //-->Submit a Letter to a key to such that the Sum of Frequencies at this key is minimum of all.
 // Calculate all presses.
 vector<int> freq;
 vector<int> op;
 class Key
 {
 public:
	 vector<int> letters;
	  int sum;
	  bool full;
	 Key()
	 {
		 sum=0;
		 full = false;
	 }
	 /*int Sum()
	 {
		 int t=0;
		 for(int i=0;i<sz(letters);i++)
			t+=letters[i];
		 return t;
	 }*/
	 
 };
int min(vector<Key>& k,int max)
{
	int m=0;
	for(int i=0;i<k.size();i++)
	{
		if((k[i].sum<k[m].sum)&& k[i].letters.size()<max)
			m=i;
	}
	return m;
}
 void process(int max,int keys,int numLet)
 {
	 vector<Key> keyPad(keys);
	 
	for(int i=0;i<freq.size();i++)
	{	
		int m=min(keyPad,max);
		keyPad[m].sum+=freq[i];
		keyPad[m].letters.push_back(freq[i]);	
	}
	int s=0;
	for(int i=0;i<sz(keyPad);i++)
	{
		for(int j=0;j<keyPad[i].letters.size();j++)
		{
			s+=keyPad[i].letters[j]*(j+1);
		}
	}

	op.push_back(s);
 }

 int main()
 {
	 ifstream cin("A-small-attempt0.in");
	 ofstream cout("small.out");
	 int n=0,i=0,maxKeyLet=0,keys=0,let=0,f=0;
	 cin>>n;
	 for(i=0;i<n;i++)
	 {
		cin>>maxKeyLet>>keys>>let;
		for(int j=0;j<let;j++)
		{
			cin>>f;
			freq.push_back(f);
		}
		std::sort(freq.rbegin(),freq.rend());
		process(maxKeyLet,keys,let);
		freq.clear();
	 }
	 for(i=0;i<sz(op);i++)
	 {
		 cout<<"Case #"<<i+1<<": "<<op[i]<<endl; 
	 }
	 return 0;
 }