#include <iostream>

using namespace std;

int main(int argc, char** argv) 
{
	int N,a,b;
	int cont = 1;
	cin >> N;cin.ignore();
	
	
	while(N--)
	{

			cin >> a;
			cin >> b;
			cin.ignore();
	
			a = (1 << a)-1;
			b = a & b;
	
			cout << "Case #" << cont++<<": ";
			if(a == b)
				cout << "ON" << endl;
			else
				cout << "OFF"<< endl;
	}
	
	return 0;
}
