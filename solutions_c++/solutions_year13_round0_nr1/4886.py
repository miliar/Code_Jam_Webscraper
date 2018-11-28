#include <string>
#include <set>
#include <iostream>
#include <vector>
#include <typeinfo>
#include <algorithm>
#include <functional>
#include <numeric>
#include <list>
#include <sstream>
#include <map>
#include<unordered_map>
#include<fstream>
using namespace std;


 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 typedef vector<pair<int,int> > vii;
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end() 
 #define tr(c,i)  for(auto i = (c).begin(); i != (c).end(); i++) 
 #define tre(c,i)  for(auto i = (c).rbegin(); i != (c).rend(); i++) 
 #define present(c,x) ((c).find(x) != (c).end()) 
 #define cpresent(c,x) (find(all(c),x) != (c).end()) 
 
 typedef vector<pair<pair<int,int>,int> > viii; 
 
template<class T>
vector<T> split(string& str)
{

	T word;
	istringstream iss(str, istringstream::in);
	vector<T> v;
	while( iss >> word )     
	{

		v.push_back(word);

	}
	return v;
}

string res;


string tic_solve(vector<vector<char> > &tic_matrix)
{
	string ret;
	//check rows 
	for(int i=0;i<4;i++)
	{
		char to_check=tic_matrix[i][0];
		if(to_check=='T')
		{
			 to_check=tic_matrix[i][1];
		}
		if(to_check=='.')
		{
			continue;
		}
		int j;
		for(j=0;j<4;j++)
		{
			if((tic_matrix[i][j]!='T')&& (to_check!=tic_matrix[i][j]))
			{
				break;
			}
		}

		if(j==4)
		{

			ret+=to_check;
			ret+=" won";
			return ret;
		}
	}

	//check columns


	for(int j=0;j<4;j++)
	{
		char to_check=tic_matrix[0][j];
		if(to_check=='T')
		{
			 to_check=tic_matrix[1][j];
		}
		if(to_check=='.')
		{
			continue;
		}
		int i;
		for(i=0;i<4;i++)
		{
			if((tic_matrix[i][j]!='T')&& (to_check!=tic_matrix[i][j]))
			{
				break;
			}
		}

		if(i==4)
		{

			ret+=to_check;
			ret+=" won";
			return ret;
		}
	}


	//check diagonals
	for(int i=0;i<4;i++)
	{
		char to_check=tic_matrix[0][0];
		if(to_check=='T')
		{
			 to_check=tic_matrix[1][1];
		}
		if(to_check=='.')
		{
			break;
		}
		if((tic_matrix[i][i]!='T') && (to_check!=tic_matrix[i][i]))
		{
			break;
		}
		
		if(i==3)
		{

			ret+=to_check;
			ret+=" won";
			return ret;
		}	
	}
	
	for(int i=3;i>=0;i--)
	{
		char to_check=tic_matrix[0][3];
		if(to_check=='T')
		{
			 to_check=tic_matrix[1][2];
		}
		if(to_check=='.')
		{
			break;
		}
		if((tic_matrix[i][3-i]!='T')&& (to_check!=tic_matrix[i][3-i]))
		{
			break;
		}
		
		if(i==0)
		{

			ret+=to_check;
			ret+=" won";
			return ret;
		}	
	}


	//no body wins
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(tic_matrix[i][j]=='.')
				return "Game has not completed";
		}
	}
	

	return "Draw";
}

int main()
{

	string givenS;
	
	int testcases;
	cin>>testcases;
	vector<vector<char> > tic_matrix(4,vector<char>(4));
	char x;
	int testcase_no=1;
	while(testcases--)
	{
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>x;
				tic_matrix[i][j]=x;
			}
		}


		cout<<"Case #"<<testcase_no<<": "<<tic_solve(tic_matrix)<<endl;
		testcase_no++;
	}
	return 0;
}