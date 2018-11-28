#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int i;
char alphabet[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	char c; int test;
	cin>>test;
	c=getchar();
	for (i=1;i<=test;i++){
		cout<<"Case #"<<i<<": ";
		while (1){
		  c = getchar();
		  if (c == '\n') 
		  {
		    cout << endl;  
		    break;
		  }
		  if (c==' ')
		    cout<<c; 
		  else
		    cout<<alphabet[c-'a'];
		}
	}
	return 0;
}
