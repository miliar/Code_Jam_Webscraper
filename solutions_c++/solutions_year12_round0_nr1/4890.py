#include "iostream"
#include "sstream"
#include "vector"
#include "cstdio"
using namespace std;
int main()
{
	int test,t,i;
	string str;
	vector<string> A;
	int M[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
	cin>>test;
	scanf("\n");
	for(t=1;t<=test;t++)
	{
		A.clear();
		printf("Case #%d: ",t);
		getline(cin,str);
		stringstream ss(str);
		while(ss>>str){
			for(i=0;i<str.size();i++)
			{
				cout<<char(M[str[i]-'a']+'a');
			}
			cout<<" ";
		}
		cout<<endl;
	}
	return 0;
}
