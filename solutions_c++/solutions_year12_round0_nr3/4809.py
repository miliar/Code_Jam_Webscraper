#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <map>

using namespace std;

vector<int> itov(int a)
{
	vector<int> r;
	while(true)
		{
			if(a <= 9)
				{
					r.push_back(a);
					break;
				}
			else 
				{
					r.push_back(a % 10);
					a /= 10;
				}
		}
	reverse(r.begin(), r.end());
	return r;
}

int vtoi(vector<int> a)
{
	int ans=0;
	reverse(a.begin(), a.end());
	for(int i=0; i<a.size(); i++)
		ans += a[i]*pow(10.0, i);
	return ans;
}

bool zero(vector<int> a)
{
	if(a[0] == 0) return false;
	else return true;
}

int small(int X, int A)
{
	vector<int> r = itov(X);
	int ans = 0;	
	vector<int> m(r);
	int t = r.size();
	for(int i=1; i<t; i++)
		{
			for(int j=0; j<t; j++)
				m[j] = r[(j+i)%t];
			int a = vtoi(m);
			if(a >= A && X > a && zero(m)) ans++;
			// for(int j=0; j<t; j++)
			// 	cout << r[j];
			// cout << " " << a << " ";
			// for(int j=0; j<t; j++)
			// 	cout << m[j];
			// cout << " " << ans << endl;
		}
	return ans;
}

int count(int A, int B)
{
	int ans = 0;
	for(int i = A; i <= B; i++)
		ans += small(i, A);
	return ans;
}

int main(){
	int T, A, B;
	fstream ps("statement.txt");
	fstream output("output.txt",fstream::trunc | fstream::out);
	ps>>T;
	int i=1;
	while(i!=T+1){
		string str;
		do {
			getline(ps,str);
		}while(str=="");
		stringstream ss(str);
		ss >> A >> B;
		int ans = count(A, B);
		output << "Case #" << i << ": " << ans << endl;
		//cout<<"Case #"<<i<<": "<<solve(str,str1,N)<<endl;
		i++;	
	}
	return 0;
}	
