#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
template<class T>
ostream& operator<<(ostream& out, const vector<T>& nums)
{
	out<<"[";
	for(vector<T>::const_iterator i=nums.begin(); i!=nums.end(); i++)
		out<<"\""<<(*i)<<"\""<<", ";
	out<<"]";
	return out;
}
typedef vector<int> ints;

inline int pow_int(int C, int n)
{
	int sum=1;
	while(n-->0)
		sum*=C;
	return sum;
}

int cj(int L, int P, int C)
{
	if (L*C>=P)
		return 0;
	int times = 1;
	int times2 = 0;
	while((L=L*C)<P)
		times2++;
	while((times2=times2/2)>=1)
		times++;
	/*
	while(true){
		times++;
		for (int l=L+1; l<P; l++){
			int Ctimes = pow_int(C+times-1, times);
			if (l*Ctimes>P && L*Ctimes>l)
				goto out;
		}
	}
	*/
out:return times;
}

int main()
{
	int T;
	cin>>T;
	int count=1;
	int L, P, C;
	for (; count<=T; count++)
	{
		cin>>L>>P>>C;
		cout<<"Case #"<<(count)<<": "<<cj(L, P, C)<<endl;
	}
	return 0;
}

