#include<iostream>
#include<vector>
#include<queue>
#include<cmath>
#include<numeric>
#include<functional>
#include<algorithm>
using namespace std;
class park
{
	long long int temp,R,K,N,result;
	vector<int> v;
	public:
	park(){
   result=0;

	}
	void getdata(){
		cin>>R>>K>>N;
    for(int i=0;i<N;i++){
            cin>>temp;
            v.push_back(temp);
	 }
	 solve();
    }
    void solve(){
 	if(N==1){
	result=R;
	return;
	}
    for(int i=0;i<R;i++){
	  long long int tsum=0,it=0; 
 while(((tsum+v[0])<=K)&&(it<v.size())){
                           tsum+=v[0];
                           it++;
                           v.push_back(v[0]);
			//for(int j=0;j<v.size();j++)
	//cout<<v[j]<<" ";cout<<endl;
                         v.erase(v.begin());
			//cout<<"tsum:"<<tsum;
                     }
//cout<<"tsu2m:"<<tsum;
    result+=tsum;
    }
    }

	int print()
	{
	
	return result;

	}
};
int main()
{
	int Testcases,i;
	cin>>Testcases;
	park *ob;
	ob=new park[Testcases+1];
	for(i=1;i<Testcases+1;i++)
	{
		ob[i].getdata();
	}
	for(i=1;i<=Testcases;i++)
	{
		cout<<"Case #"<<i<<": "<<ob[i].print()<<endl;
	}
	return 0;
}
