#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;

string input[50000];


int d,l,n;

int main(void){

	
	cin>>l>>d>>n;

	int i,j;

	for(i=0;i<d;i++)
		cin>>input[i];

	int c;
	string temp;
	for(c=0;c<n;c++){

		string str[15];
		cin>>temp;

		i=0;
		j=0;
		while(i<l){

			if(temp[j]!='('){
				str[i]=temp[j];
				j++;
				i++;
				continue;
			}
			int first=j+1;

			while(temp[j]!=')')
				j++;
			for(int k=first;k<j;k++)
				str[i]+=temp[k];
			i++;
			j++;
			
		}
		int ans=0;
		for(i=0;i<d;i++){

			for(j=0;j<l;j++)
				if(str[j].find(input[i][j])==string::npos)
					break;
			if(j==l)
				ans++;
		}
		cout<<"Case #"<<c+1<<": "<<ans<<endl;
	}
	
	return 0;
}
				
				






