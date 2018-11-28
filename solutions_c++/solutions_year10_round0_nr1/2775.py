#include<iostream>
#include<vector>
#include<cmath>
#include<numeric>
#include<functional>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
class snapper
{	vector<int> v,v2;
	long long int n,k;
	public:
	snapper(){}
	void getdata(){
		cin>>n>>k;
	    }
    string snap(){
	int fl=1,temp;
	vector <int> v;
	k = k%(long long int)(pow(2, n));	
	
	while(k)
	{
      		temp=k%2;
	  	v.push_back(temp);
		k/=2;
	}

	for(int i=0;i<v.size();i++)
	{
		 if(!v[i])
		 {
			fl=0;
		          break;
		 }
	}
	if(fl && v.size()==n)
	return "ON";else
 	return "OFF";
}
};
int main()
{
	int Testcases,i;
	cin>>Testcases;
	snapper *ob;
	for(int i=0;i<30;i++)
	ob=new snapper[Testcases+1];
	for(i=1;i<Testcases+1;i++)
	{
		ob[i].getdata();
	}
	for(i=1;i<=Testcases;i++)
	{
		cout<<"Case #"<<i<<": "<<ob[i].snap()<<endl;
	}
	return 0;
}
