
#include <iostream>
#include <queue>
using namespace std;

int main()
{
	int N,r,lugares,grupos;
	int cont = 1;
	cin >> N;cin.ignore();
	
	
	while(N--)
	{
			queue<int> cola;
			int euro =0;
			cin >> r;
			cin >> lugares;
			cin >> grupos;
			cin.ignore();
			int suma=0;
			while(grupos--)
				{
					int temp;
					cin >> temp;
					suma +=temp;
					cola.push(temp);
				}
			cin.ignore();
			
		
		if(suma > lugares)
		  while(r--)
			{
				int temp = lugares;
				while(cola.front()<=temp)
					{
						int a = cola.front();
						cola.pop();
						temp -= a;
						euro += a;
						cola.push(a);
					}
			}
			else
				euro = suma*r;
			cout << "Case #" << cont++<<": " << euro << endl;
	}
	
	return 0;
}
