//============================================================================
// Name        : A.cpp
// Author      : Toqa Osama
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;
vector<int> b ,o,all;
int BotTrust()
{
	int sec = 0;
	int i = 1,j = 1 ,a = 0,k =0,q = 0;
	while(true)
	{
		bool f = false;
		if(a>=all.size())break;
		if(k < b.size()){
		if(all[a]==1&&b[k]==i)
		{
			a++;
			k++;
			f = true;
		}
		else if(all[a]==0&&b[k]==i);
		else
		{
			if(i<b[k])
				i++;
			else
				i--;
		}
		}
		if(q < o.size()){
		if(all[a]==0&&o[q]==j&&f==false)
		{
					a++;
					q++;
		}
		else if(all[a]==0&&o[q]==j&&f==true);
		else if(all[a]==1&&o[q]==j);
		else
				{
					if(j<o[q])
						j++;
					else
						j--;
				}
		}
		sec++;
	}
	return sec;
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n,l,temp;
	cin>>n;
	char c;
	for(int t = 0 ; t < n ; t++)
	{
		cin>>l;
		for(int i = 0 ; i<l;i++){
			cin>>c>>temp;
			if(c=='O'){
				o.push_back(temp);
				all.push_back(0);
			}
			else if(c=='B'){
				b.push_back(temp);
				all.push_back(1);
			}
		}
		cout<<"Case #"<<t+1<<": "<<BotTrust();
		if(t!=n-1)cout<<endl;
		b.clear();
		o.clear();
		all.clear();
	}
	return 0;
}
