#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define f(i,x) for(int i=0;i<x;i++)
#define fo(i,x,y) for(int i=x;i<y;i++)
#define pb push_back
#define vi vector<int>
#define all(x) x.begin(),x.end()
#define vs vector<string>
#define ss stringstream
#define ll long long
using namespace std;
int main(){
	int num;
	cin>>num;
	f(lp,num){
		int n,m;
		cin>>n>>m;
		string s;
		string s1;
		vector<vector<string> >fir;
		vector<vector<string> >sec;
		vs temp;
		f(i,n){
			cin>>s;
			f(j,s.size()){
				if(s[j]=='/'){
					if(s1!=""){
						temp.pb(s1); s1="";}
					}
				else s1+=s[j];
				}
				temp.pb(s1);
				s1="";
				fir.pb(temp);
				temp.erase(all(temp));
		}
		f(i,m){
			cin>>s;
			f(j,s.size()){
				if(s[j]=='/'){
					if(s1!=""){
						temp.pb(s1); s1="";
						}}
				else s1+=s[j];
				}
				temp.pb(s1);	
				s1="";
				sec.pb(temp);
				temp.erase(all(temp));
			}
		int count=0;
		int max1=0;
/*		f(i,n){
			f(j,fir.size()){
				cout<<fir[i][j]<<" ";
			}
			cout<<endl;
		}
		cout<<endl<<endl<<endl;
		f(i,m){
			f(j,sec.size()){
				cout<<sec[i][j]<<" ";
			}cout<<endl;
		}
		cout<<endl<<endl;*/
		int sol[m];
		f(i,sec.size()){
			max1=0;
			f(j,fir.size()){
				count=0;
				if(sec[i][0]==fir[j][0]){
					for(int k=0;k<min(sec[i].size(),fir[j].size());k++){
						if(sec[i][k]==fir[j][k]) count++;
						else break;
					}
				}
				max1=max(max1,count);
				}
			sol[i]=sec[i].size()-max1;
			fir.pb(sec[i]);
		}
		int solu=0;
//		f(i,sec.size()) cout<<sol[i]<<endl;
		f(i,sec.size()) solu+=sol[i];
		cout<<"Case #"<<lp+1<<": "<<solu<<endl;}}
