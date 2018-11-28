#include <stdio.h>
#include <iostream>
using namespace std;
#include <algorithm>
#include <map>


int main()
{
	int nol;
	scanf("%d\n",&nol);
	int c=0;
	while(nol--)
	{	
		c++;
		int N,S,p;
		int np = 0;
		int google[101];
		cin>>N;
		cin>>S;
		cin>>p;
		for(int i=1;i<=N;i++)
			cin>>google[i-1];

		//cout<<p<<endl;
 		for(int i=0;i<N;i++){
			if(google[i]%3==0){
				if(google[i]/3>=p){
					np++;
					//cout<<google[i]/3<<endl;
				}
				else if( (google[i]/3)+1>=p and S>=1 and google[i]!=0)
				{	np++;
					S--;
				}
			}
			else if(google[i]%3==1){
				if((google[i]/3)+1>=p )
					np++;
				else if((google[i]/3 + 1)>=p and S>=1)
				{	np++;
					S--;
				}
			}
			else if(google[i]%3==2){
				if((google[i]/3)+1>=p)
					np++;
				else if((google[i]/3 + 2)>=p and S>=1)
				{	np++;
					S--;
				}
			}
			//cout<<google[i]<<","<<np<<","<<S<<endl;
		}
			cout<<"Case #"<<c<<": "<<np<<endl;
	} 
}