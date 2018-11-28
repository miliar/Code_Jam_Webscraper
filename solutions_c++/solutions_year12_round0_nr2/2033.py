using namespace std;

#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

int max_not_suprising(int num)
{
	int temp=num/3;
	if(num == 0) return 0;
	if(num == 1) return 1;
	if(num == 2) return 1;
	if(num%3 !=0) 
		temp++;
	return temp;
}

int max_suprising(int num)
{
	int temp=num/3;
	if(num == 0) return 0;
	if(num == 1) return 1;
	if(num == 2) return 2;
	if(num%3 == 0 || num%3 == 1) 
		temp++;
	else 
		temp+=2;
	return temp;
}

int max_ge_p(vector<int> total_pts, int s, int p)
{
	int res=0, s_temp=0;
	sort(total_pts.rbegin(), total_pts.rend());
	for(int i=0; i < total_pts.size(); i++)
	{
		int ms, mns;
		ms=max_suprising(total_pts[i]);
		mns=max_not_suprising(total_pts[i]);
		if(mns >= p) res++;
		else if(ms >= p && s_temp < s) {res++; s_temp++;}
		else break;
	}
	return res;
}

int main()
{
	ofstream fout ("dancing.out");
	ifstream fin ("dancing.in");
	int T, n, s, p, temp;
	fin>>T;
	for(int i=0; i < T; i++)
	{
		fin>>n>>s>>p;
		vector<int> total_pts;
		for(int j=0; j<n; j++)
		{
			fin>>temp;
			total_pts.push_back(temp);
		}
		temp = max_ge_p(total_pts, s, p);
		fout<< "Case #" << i+1 << ": " << temp << endl;
	}
	return 0;
}
