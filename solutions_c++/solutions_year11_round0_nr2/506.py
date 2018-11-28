#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;
int f[30][30];
int g[30][30];
char ch1,ch2,ch3;
string input;
int test_comb(){
	if (input.size()<2)
		return(0);
	char last = input[input.size() -1];
	char before = input[input.size()-2];
	if (f[before-'A'][last-'A']!= -1)
	{
		input.erase(input.size()-2,2);
		input+=(char)f[before-'A'][last-'A'] + 'A';
		return (1);
	}
	return(0);
}
void test_cont(){
	char last = input[input.size() -1];
	for (int i=0;i<26;i++){
		if (g[last-'A'][i] == 1 && input.find_first_of(i+'A')!=-1)
		{
			input.clear();
			return;
		}
	}
}
int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int test;
	cin>>test;
	int cnt =0;
	while (test--){
		//cout <<test<<endl;
		cnt++;
		int comb;
		cin >> comb;
		for (int i=0;i<30;i++)
			for (int j=0;j<30;j++)
				f[i][j] = -1;
		for (int i=0;i<comb;i++){
			cin >> ch1;
			cin >> ch2;
			cin >> ch3;
			f[ch1-'A'][ch2-'A'] = ch3-'A'; 
			f[ch2-'A'][ch1-'A'] = ch3-'A';
		}
		for (int i=0;i<30;i++)
			for (int j=0;j<30;j++)
				g[i][j] = -1;
		int cont;
		cin>>cont;
		for (int i=0;i<cont;i++){
			cin>>ch1;
			cin>>ch2;
			g[ch1-'A'][ch2-'A'] = 1;
			g[ch2-'A'][ch1-'A'] = 1;
		//	cout <<"g for "<<ch1 << "is "<< ch2<<endl;
		}
		int size;
		cin>>size;
		input = "";
		for (int i=0;i<size;i++)
		{
			cin>>ch1;
			input += ch1;
			while(test_comb());
			test_cont();
		}
		//cout<<input.size()<<endl;
		cout<<"Case #"<< cnt<<": [";
		if (input.size()>0)
			for (int i=0;i<input.size()-1;i++)
				cout<<input[i]<<", ";
		if (input.size()>0)
			cout<<input[input.size()-1];
		cout<<"]"<<endl;
		
	}
}