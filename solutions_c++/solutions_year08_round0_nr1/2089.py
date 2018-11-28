#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <malloc.h>
using namespace std;

template <class T>
void printVector(const vector <T> &vec)
{
	vector<T>::const_iterator p1;
	for(p1=vec.begin();p1!=vec.end();++p1)
		cout<<*p1<<'\n';
}

template <class T>
bool findEngine(const vector <T> &vec,string temp)
{
	vector<T>::const_iterator p1;
	for(p1=vec.begin();p1!=vec.end();++p1)
		if(*p1==temp)
			return true;
		return false;
}
void deal(int iTimes)
{
	int number1,number2, i;
    int times=0;
	string temp;
    vector<string> engines,queries;
	cin>>number1;
	getline(cin,temp);
	for(i=0;i<number1;++i){
	    getline(cin,temp);
		engines.push_back(temp);
	}
	cin>>number2;
	getline(cin,temp);
	int localtime=0;
	for(i=0;i<number2;++i)
	{
	    getline(cin,temp);
	//	cout<<temp;
	//	cout<<"\n----------------------\n";
		// printVector(queries);
		// cout<<"\n----------------------\n";
	//	 cout<<findEngine(queries,temp);
		if(!findEngine(queries,temp)){
		   ++localtime;
		  // cout<<localtime;
		   if(localtime==number1)
		   {
			  // cout<<"\n"<<localtime<<"-----------------------\n";
			   localtime=1;
			  // printVector(queries);
			   queries.clear();
			   ++times;
			   //cout<<"\n----------------------\n";
			   //printVector(queries);
		   } 
		}
	//	cout<<temp;
		queries.push_back(temp);
	}
	cout<<"Case #"<<iTimes<<": "<<times;
	//cout<<"\n----------------------\n";
//	printVector(queries);
}
int main(){
	int cases;
	cin>>cases;
	for(int i=0;i<cases;++i)
	{
		if(i!=0) cout<<"\n";
		deal(i+1);
	}
	return 0;
}

