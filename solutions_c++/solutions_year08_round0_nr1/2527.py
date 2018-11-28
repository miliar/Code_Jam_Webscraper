/*
ID: rohanso1
PROG: checker
LANG: C++
*/

#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<string>
#include<conio.h>

using namespace std;

char se[101][101];
bool full_se[101];
char q[1001][101];
int num_se, num_q;

//ofstream fout ("A-small.out");

int putAndCheck(int j) {
	for(int i=0;i<num_se;i++) {
		if(strcmp(se[i],q[j])==0) {
			full_se[i]=1;
			break;
		}
	}
	for(int i=0;i<num_se;i++) {
		if(full_se[i]==0) {
			return 0;
		}
	}
	return 1;
}

int main() {
//	ifstream fin ("A-small.in");
	
	int n;
	cin>>n;
	for(int i=0;i<n;i++) {
		for(int j=0;j<num_se;j++)
		    full_se[j]=0;

		//take input
		
		cin>>num_se;
//		fflush(stdin);
		getc(stdin);
		for(int j=0;j<num_se;j++)
			cin.getline(se[j],101);

		
		cin>>num_q;
		getc(stdin);
		for(int j=0;j<num_q;j++)
			cin.getline(q[j],101);

		//process data

		int switches=0;
		for(int j=0;j<num_q;j++) {
		//	cout<<q[j]<<" "<<switches<<"\n";
		//	getch();
			if(putAndCheck(j)) {
				switches++;
				for(int k=0;k<num_se;k++)
		    		full_se[k]=0;
				j--;
            }
		}
		cout<<"Case #"<<i+1<<": "<<switches;
		if(i<n-1)
		    cout<<"\n";
  	}
	return 0;
}
