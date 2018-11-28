#include<iostream>
#include<vector>
#include<queue>
#include<cmath>
#include<numeric>
#include<functional>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;

class file
{	
	vector<int> s1,s2;
	public:
	file(){

	}
	void getdata(){
		int a,b,n;
		cin>>n;
		for(int i=0;i<n;i++){
		cin>>a>>b;
		 s1.push_back(a);
 		s2.push_back(b);
		}
   	 }
   	   int function()
	{

	  	 int count=0,j,kk;
	 	for(int i=0;i<s1.size() && i<s2.size();i++)
		{
			for(kk=i+1;kk<s1.size() && kk<s2.size();kk++)
			{	
		 		if(s1[i]<s1[kk] && s2[i]>s2[kk])
		  		count++;
				if(s1[i]>s1[kk] && s2[i]<s2[kk])
				count++;
			}
	
		}

	return count;
	}
		
};int main()
{
	int Testcases,i;
	cin>>Testcases;
	file *ob;
	ob=new file[Testcases+1];
	for(i=1;i<Testcases+1;i++)
	{
		ob[i].getdata();
	}
	for(i=1;i<=Testcases;i++)
	{
		cout<<"Case #"<<i<<": "<<ob[i].function()<<endl;
	}
	return 0;
}
