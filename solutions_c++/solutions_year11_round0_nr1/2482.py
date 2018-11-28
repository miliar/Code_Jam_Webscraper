#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

int main(void)
{
	char robot,robotp;
	int	nrtest,nrbutton,button,buttonp,buttono,t,ttotal,taccum;
	string s;
	
	getline(cin,s);
	istringstream ss(s);
	ss >> nrtest;
	
	for(int i=0;i<nrtest;i++)
	{
		getline(cin,s);
		istringstream ss(s);
		ss >> nrbutton;
		
		ttotal=0;
		taccum=0;
		buttonp=1;
		buttono=1;
		
		for(int j=0;j<nrbutton;j++)
		{
			ss >> robot >> button;
			
			if((j==0)||(robot==robotp))
			{
				t=abs(button-buttonp)+1;
				ttotal+=t;
				taccum+=t;
				robotp=robot;
				buttonp=button;
			}
			else
			{
				t=max(abs(button-buttono)-taccum,0)+1;
				ttotal+=t;
				taccum=t;
				robotp=robot;
				buttono=buttonp;
				buttonp=button;
			}
		}
		
		cout << "Case #" << i+1 << ": " << ttotal << endl;
	}
}
