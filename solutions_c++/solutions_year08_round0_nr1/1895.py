
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>

using namespace std;

const int ss=102;
const int qq=1002;
int mydp[qq][ss];
string str[ss],que[qq];
bool flag[qq];
int main()
{
	int myN;
	cin>>myN;
	for(int cases=1;cases<=myN;cases++)
	{

		int s,q;
		cin>>s;
		
		string tmp;
		getline(cin,tmp);
		for(int i=0;i<s;i++)
		{
			getline(cin,str[i]);
			
		}
		cin>>q;
		getline(cin,tmp);
		
		for(int i=0;i<q;i++)		
		getline(cin,que[i]);

		for(int i=0;i<s;i++)
		{
			mydp[0][i]=0;
		}

		for(int k=1;k<q;k++)
		{
			for(int m=0;m<s;m++)
			{
				if(que[k]!=str[m])
				{
					int minv=1000000,tmp;
					for(int j=0;j<s;j++)
					{
						
						if(que[k-1]!=str[j]){
							if(j!=m) tmp=mydp[k-1][j]+1;
							else tmp=mydp[k-1][j];
							minv=min(minv,tmp);}
					}
					mydp[k][m]=minv;
				}
			}
		}

		int myminv=1000000;
		if(q==0) myminv=0;
		else
			for(int i=0;i<s;i++)
			{
				if(que[q-1]==str[i]) continue;
				myminv=min(myminv,mydp[q-1][i]);
			}
			cout<<"Case #"<<cases<<": "<<myminv<<endl;
	}
	return 0;
}


