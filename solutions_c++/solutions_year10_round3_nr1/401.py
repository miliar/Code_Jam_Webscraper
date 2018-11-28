#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

struct xy
{
    long int A;
    long int B;
};
bool compare(const xy& e1,const xy& e2)
{
    // compare the two structures
    return e1.A < e2.A;
}

int main()
{
	//ofstream fout ("milk.out");
    //ifstream cin ("milk.in");
    
    long int N,i,j,T,ans;
    long int A=0,B=0;
  
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>N;
		ans=0;
		vector<xy> a;
		vector<xy>::iterator iter,iter1;
		xy temp;
		for(j=0;j<N;j++)
		{
			cin>>temp.A>>temp.B;
			a.push_back(temp);
		}
		sort(a.begin(), a.end(), compare );
		for(iter=a.begin();iter<a.end();iter++)
		{
			for(iter1=iter+1;iter1<a.end();iter1++)
			{
			if ((*(iter)).B>(*iter1).B)
			{
				ans++;
			}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}
