#include <iostream>
#include <fstream>
using namespace std;

void main(){
	ifstream cin;
	ofstream cout;
	cin.open("C-small-attempt0.in");
	cout.open("C-small.out");
int g[1000];
int t;
cin>>t;
	for(int o=1;o<=t;o++){
		long long profit[1000];
		int remaining[100];
		for(int i=0;i<100;i++)
			remaining[i]=-1;
		int R,k,N;
		cin>>R>>k>>N;
		int start=0,i=0;
		long long pr=0;
		for(int i=0;i<N;i++)
			cin>>g[i];

		while(R>0){
		//cout<<"R is "<<R<<" and profit is "<<pr<<" and start is "<<start<<endl;
		int l;
		l=k;
		if(remaining[start] !=-1)
		{
		pr=pr+(pr-profit[start])*(R/(remaining[start]-R));
		int temp;
		temp=R-(remaining[start]-R)*(R/(remaining[start]-R));
		R=R-(remaining[start]-R)*(R/(remaining[start]-R));
		remaining[start]=temp;
		profit[start]=pr;
		}
		else
		{
		profit[start]=pr;
		remaining[start]=R;
		}

		if(R>0){
			while(true){
			if(l-g[i]>=0) 
				{
					pr=pr+g[i];
					l=l-g[i];
					if((i+1)%N == start)
					{start = (i+1)%N;
					R--;
					break;
					}
					else
					i=(i+1)%N;
				}
			else
				{
					start=i;
					R--;
					break;
				}

			}
		}
		}
		cout<<"Case #"<<o<<": "<<pr<<endl; 
	}
}