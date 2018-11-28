#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#define ll long long
#define pb push_back
using namespace std;

int findValue(vector<int> v, int value, int start)
{
	int i;
	for(i=start;i<v.size();i++)
	{
		if (v.at(i)==value) return i;
	}
	return -1;
}

void swap(vector<int>& v, int n, int m)
{
	if(n>=m)
	{
		int temp,i;
		temp = v.at(n);
		for(i=n;i>m;i--)
			v.at(i) = v.at(i-1);
		v.at(m) = temp;
	}
	else
	{
		cout << "ERROR!" << n << " " << m;
	}
}

string getNext(string N)
{
	int d,i,j,min,flag=0;
	string ret = "";
	vector<int> v;
	for(i=0;i<N.length();i++)
	{
		v.pb(N[i]-'0');
	}
	flag = 0;
	for(i=v.size()-1;i>-1;i--)
	{
		min = 10;
		d = v.at(i);
		
			for(j=i+1;j<v.size();j++)
			{
				//cout << "j = " << j << " value = " << v.at(j) << endl;
				if(v.at(j)>d)
					if(v.at(j)<min)
						min = v.at(j);
				//cout << "min = " << min << endl;
			}
			
		if (min!=10)
		{
			//cout << "swap " <<  "findValue(" << min << "," << i+1 << ") " << i << endl;
			swap(v,findValue(v,min,i+1),i);
			sort(v.begin()+i+1,v.end());
			flag = 1;
			break;
		}
	}
	if(flag!=1)
	{
		sort(v.begin(),v.end());
		i=0;
		while(v.at(i)==0) i++;
		swap(v,i,0);
		v.pb(0);
		swap(v,v.size()-1,1);
	}
	
	for(i=0;i<v.size();i++)
			ret.pb(v.at(i)+'0');
	return ret;
	
}

int main()
{
	int nc,cc;
	string res,N;
	cin >> nc;
	for(cc=0;cc<nc;cc++)
	{
		cin >> N;
		res = getNext(N);
		cout << "Case #" << cc+1 << ": " << res << endl;
	}
}


