#include <iostream>
using namespace std;


void solveproblem(int); //duh
int main()
//ditto on the duh
{
int T;
cin>>T;
for(int i = 0; i<T; i++)
solveproblem(i+1);
}
void solveproblem(int x)
{
	int N, L, H;
	cin >> N >> L >> H;
	int freq[10000];
	for(int i = 0; i < N; i++) cin >> freq[i];
	
	bool found = false;
	while(!found&&L<=H)
	{
		found = true;
		for(int i = 0; i < N&&found; i++)
		{
			int mod;
			if(L>freq[i]) mod = L%freq[i];
			else mod = freq[i]%L;
			if(mod>0) found=false;
		}
		L++;
	}
	L--;
	
cout << "Case #" << x << ": ";
if(found) cout << L << endl;
else cout << "NO" << endl;

}
