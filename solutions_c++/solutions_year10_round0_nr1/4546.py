////ID: mamdouh2
////PROG: smount
////LANG: C++
//#include<iostream>
//#include<string>
//#include<algorithm>
//#include<cmath>
//#include<vector>
//#include<set>
//#include<fstream>
//using namespace std;
//int main()
//{
//	ifstream cin("smount.in");
//	ofstream cout("smount.out");
//	int n;
//
//	cin>>n;
//
//	int p;
//
//	cin>>p;
//
//	bool inc=true;
//	int maxi = 0;
//	int current = 1;
//	int old = 0;
//	for(int i=1; i<n ; i++)
//	{
//		int t;
//		cin>>t;
//
//
//		if(t>p)
//		{
//			if(inc)
//				current++;
//			else
//			{
//				maxi = max(maxi, current);
//				current=old+1;
//				old=1;
//
//			}
//
//			inc=true;
//
//		}
//		else if (t<p)
//		{	
//			inc = false;
//			current++;
//			old = 1;
//		}
//		else
//		{
//			current++;
//			old++;
//		}
//		swap(t,p);
//
//	}
//	maxi = max(maxi, current);
//	cout<<maxi<<endl;
//	return 0;
//}