
#include<iostream>
#include<fstream> 
#include<string>
using namespace std;

int main(){
	int T;
	string txt = "A-large";
	ofstream cout(txt + ".out.txt");
    ifstream cin(txt + ".in"); 

	cin >> T;

	for(int t = 1; t <= T; t++)
	{
		int N, K;
		cin >> N >> K;
		
		int a = 2 << (N-1);
		
		bool b = false;
		if( (K % a) == (a - 1) )
		{
			b = true;
		}
		cout << "Case #" << t << ": " << (b ? "ON" : "OFF") << endl;
	}
}
