#include<iostream>
using namespace std;
#include<vector>
#include<fstream>
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("A-small-attempt0.in");
	cout.open("output.txt");
	int a,t;
	double b;
	double temp,result=0,mult=1;
	vector<double> prob;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		result=0;
		mult=1;
		cin>>a>>b;
		for(int j=0;j<a;j++){
			cin>>temp;
			mult=mult*temp;
			prob.push_back(temp);
		}
		result=mult*(b-a+1)+(1-mult)*(2*b-a+2);
		for(int k=1;k<=a;k++){
			mult=1;
			for(int h=0;h<a-k;h++){
				mult=mult*prob[h];
			}
			result=min(result,mult*(2*k+b-a+1)+(1-mult)*(2*k+2*b-a+2));
		}
		result=min(result,2+b);
		cout<<"Case #"<<i+1<<": "<<result<<endl;
		prob.clear();
	}
}



		

		


