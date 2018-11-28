#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<int> primes;

int solve()
{
    int A, B, P;
    cin >> A >> B >> P;
    cerr << endl << endl << "-----" << endl << A << " " << B << " " << P << endl;
    
    int a[B][2];
    for(int i=A; i<=B; i++) {
	a[i][0] = i;
	a[i][1] = i;
    }

    for(int i=A; i<=B; i++)
	for(int j=i+1; j<=B; j++)
	    for(int k=0; k<primes.size(); k++)
		if(primes[k]>=P && a[i][0]%primes[k]==0 && a[j][0]%primes[k]==0) {
		    int f = a[j][1];
		    int t = a[i][1];
		    for(int l=A; l<=B; l++)
			if(a[l][1]==f)
			    a[l][1]=t;
		}
    
    cerr << endl;
    for(int i=A; i<=B; i++)
	cerr << a[i][1] << " ";

    map<int,bool> result;
    for(int i=A; i<=B; i++)
	result[a[i][1]] = true;
    return result.size();
}

int main()
{
    primes.push_back(2);
    for(int i=3; i<=550; i++) {
	bool prime = true;
	for(int k=2;k<i;k++)
	    if(i%k==0) {
		prime = false;
		break;
	    }
	if(prime) {
	    primes.push_back(i);
	    cerr << i << " ";
	}
    }
	
    int C;
    cin >> C;
    for(int i=1; i<=C; i++)
	cout << "Case #" << i << ": " << solve() << endl; 
    return 0;
}
