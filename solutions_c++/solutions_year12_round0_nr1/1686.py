#include <vector>
#include <list>
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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

void doit(){
	char tr[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	string str;
	getline(cin,str);
	for(int i=0;i<str.size();i++)
	if(str[i]>='a' && str[i]<='z')str[i]=tr[str[i]-'a'];
	cout<<str<<endl;
	return;
}
int main(){
    int tc;
	string dummy;
    cin>>tc;
	getline(cin,dummy);
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}
