
#include <vector>
#include <list>
#include <ctime>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define ll  long long
#define pb push_back
#define mp make_pair
#define size(v) (int)(v.size())
#define loop(i,n) for(i=0;i<n;i++)
#define all(v) v.begin(), v.end()
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define vi vector<int>

using namespace std;

int main() {

    int i,j,k;
    int t;
    cin>>t;
    for(int numt=0;numt<t;numt++){
    	int K;
    	string str;
    	cin>>K;
    	cin>>str;
    	vector<int> vec(K,0);
    	for(i=0;i<K;i++) vec[i]=i;
    	int s=size(str);
    	ll mi=100000000;
    	do{
    		string nstr="";
    		for(j=0;j<s;j+=K){

    			for(i=j;i<j+K;i++){
    				nstr+=str[vec[i-j]+j];
    			}

    		}
    		int cnt=1;
    		char prev=nstr[0];
    		for(i=0;i<size(nstr);i++){
    			if(prev==nstr[i]) continue;
    			else{
    				prev=nstr[i];
    				cnt++;
    			}
    		}
    		mi<?=cnt;
    		//cout<<nstr<<endl;

    	}while(next_permutation(all(vec)));




     cout<<"Case #"<<numt+1<<": "<<mi<<endl;
    }

    return 0;
}
