#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> fwin (int n)
{
    int chasnoe = n;
    int ostatok = 0;
    
    vector<int>v;
    while (chasnoe != 0) {
	ostatok = chasnoe%2;
	v.insert(v.begin(),ostatok);
	chasnoe = chasnoe/2;
    }
    
    /*for (int i = 0; i < v.size(); i++) {
	cout << v[i] << " ";
    }
    
    cout << endl;*/
    
    
    return v;
}

vector<int> summ (vector<int> one,vector<int> two)
{
    if (two.size() == 0) { 
	//cout << "tyt" << endl;
	return one;
    }
    
    if (one.size() > two.size()) swap (one,two);

    for (int i = one.size()-1,j = two.size()-1; i >= 0 && j >= 0; i--,j--) {
	if (one[i] == 0 && two[j] == 0) {
	    two[j] = 0;
	}
	else if (one[i] == 1 && two[j] == 1) {
	    two[j] = 0;
	}
	else {
	    two[j] = 1;
	}
    }
    
    return two;
}

int main()
{
    int T = 0;
    cin >> T;
    int kol = 1;
    while (T > 0) {
    int n;
    cin >> n;
    
    int max = 0;
    
    vector<int> w(n);
    
    for (int i = 0; i < n; i++) {
	cin >> w[i];
    }
    
    sort(w.begin(),w.end());
    
    vector<int> oh[n];
    for (int i = 0; i < n; i++) {
        oh[i] = fwin(w[i]);
    }
    

    int otv = 0;
    int otv2 = 0;
    for (int one = 0; one < n-1; one++) {
	otv = otv2  = 0;
	vector<int> a;
	vector<int> b;
	
	for (int q = 0; q <= one; q++) {
	    a = summ(oh[q],a);
	    otv += w[q];
	}
	
	//cout << "otv : " << otv << endl;
	
	for (int e = one+1; e < n; e++) {
	    b = summ (oh[e],b);
	    otv2 += w[e];
	}
	
	//cout << "otv2 : " << otv2 << endl;
	
	double edik = 0;
	double kirill = 0;
	
	for (int i = 0; i < a.size(); i++) {
	    edik *= 10;
	    edik += a[i];
	}
	
	for (int i = 0; i < b.size(); i++) {
	    kirill *= 10;
	    kirill += b[i];
	}
	
	if (edik == kirill) {
	    if (otv > otv2) {
		if (max < otv) {
		    max = otv;
		}
	    }
	    else {
		if (max < otv2) {
		    max = otv2;
		}
	    }
	}
    }
    if (max != 0) {
	cout << "Case #" << kol << ": " << max << endl;
    }
    
    else {
	cout << "Case #" << kol << ": NO" << endl;
    }
    
    T--;
    kol++;
    }
    
    return 0;
}