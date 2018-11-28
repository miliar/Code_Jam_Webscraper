#include <iostream>
#include <cstdio>

using namespace std;

int
main()
{
	int T, ca=0;
	char c;
	char vet[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	
	cin >> T;
	while(getchar() != '\n');
	while(T--)
	{
		cout << "Case #" << ++ca << ": ";
		while((c = getchar()) != '\n')
			cout << ((c == ' ') ? ' ' : vet[c-'a']);
		cout << endl;
	}
	
	return 0;
}

